"""Endpoint Definition"""

from uuid import uuid4

from fastapi import APIRouter, HTTPException
from sqlalchemy import and_, delete, func, insert, or_, select, update

from be_ecommerce.api.models import (Product, ProductAddCartInput,
                                     ProductAddCartOutput, ProductDetailsInput,
                                     ProductDetailsOutput,
                                     ProductRemovalAllInput,
                                     ProductRemovalAllOutput,
                                     ProductRemovalWithQuantityInput,
                                     ProductRemovalWithQuantityOutput,
                                     ProductSearchInput, ProductSearchOutput)
from be_ecommerce.db.tables import Product as ProductTable
from be_ecommerce.db.tables import User, UserCart
from be_ecommerce.db.utils import DatabaseSessionMaker

router = APIRouter()  # invoco costruttore default
session_maker = DatabaseSessionMaker()


async def check_user_exists(user_id: str) -> bool:
    """Utility function to check if the user_id exists in the database"""

    async with session_maker.get_session() as session:
        my_query = select(User).where(user_id == User.uid)
        result = await session.execute(my_query)
        return_value = result.first()
        if return_value and len(return_value) > 0:
            return True
        return False


async def check_product_exists(product_id: str) -> bool:
    """Utility function to check if the product_id exists in the database"""

    async with session_maker.get_session() as session:
        my_query = select(ProductTable.id).where(ProductTable.id == product_id)
        result = await session.execute(my_query)
        return_value = result.first()
        if return_value and len(return_value) > 0:
            return True
        return False


@router.post("/search")
async def search_product(payload: ProductSearchInput) -> ProductSearchOutput:
    """Logic of the search endpoint"""

    try:
        async with session_maker.get_session() as session:
            my_sql = select(ProductTable).where(
                or_(
                    ProductTable.name.ilike(f"%{payload.query}%"),
                    ProductTable.description.ilike(f"%{payload.query}%"),
                )
            )
            result = await session.execute(my_sql)
            result_list: list = []
            for record in result.fetchall():
                result_list.append(
                    Product(
                        id=str(record[0].id),
                        name=record[0].name,
                        price=record[0].price,
                        description=record[0].description,
                    )
                )
            return ProductSearchOutput(products=result_list)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/add_product")
async def add_to_cart(payload: ProductAddCartInput) -> ProductAddCartOutput:
    """Logic of the add_product endpoint"""

    try:
        async with session_maker.get_session() as session:
            if await check_user_exists(payload.user_id) and await check_product_exists(
                payload.product_id
            ):
                my_sql = select(UserCart).where(
                    and_(
                        UserCart.uid == payload.user_id,
                        UserCart.pid == payload.product_id,
                    )
                )
                result = await session.execute(my_sql)
                record = result.first()
                if record and len(record) > 0:
                    my_sql = (
                        update(UserCart)
                        .where(
                            and_(
                                UserCart.pid == payload.product_id,
                                UserCart.uid == payload.user_id,
                            )
                        )
                        .values(quantity=record[0].quantity + payload.quantity)
                    )
                    compile = my_sql.compile()
                    result = await session.execute(my_sql)
                    await session.commit()
                else:
                    my_query = insert(UserCart).values(
                        pid=payload.product_id,
                        uid=payload.user_id,
                        quantity=payload.quantity,
                    )
                    compile = my_query.compile()
                    result = await session.execute(my_query)
                    await session.commit()
            else:
                raise HTTPException(
                    status_code=404,
                    detail=f"Product ID or UserID not found in the database",
                )
        return ProductAddCartOutput(added=True)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/product_details")
async def product_details(payload: ProductDetailsInput) -> ProductDetailsOutput:
    """Logic of the product_details endpoint"""

    try:
        async with session_maker.get_session() as session:
            my_sql = select(ProductTable).where(ProductTable.id == payload.product_id)
            result = await session.execute(my_sql)
            record = result.first()
            if record and len(record) > 0:
                return ProductDetailsOutput(
                    product_name=record[0].name,
                    product_description=record[0].description,
                    product_price=record[0].price,
                )
            else:
                raise HTTPException(
                    status_code=404,
                    detail=f"product with ID {payload.product_id} not found",
                )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/product_removal_all")
async def product_removal_all(
    payload: ProductRemovalAllInput,
) -> ProductRemovalAllOutput:
    """Logic of the product_removal_all endpoint"""

    try:
        if not check_user_exists(payload.user_id):
            raise HTTPException(status_code=404, detail="User not found")

        async with session_maker.get_session() as session:
            my_sql = delete(UserCart).where(UserCart.uid == payload.user_id)
            compile = my_sql.compile()
            result = await session.execute(my_sql)
            await session.commit()
            return ProductRemovalAllOutput(removed=True)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/product_removal_quantity")
async def product_removal_quantity(
    payload: ProductRemovalWithQuantityInput,
) -> ProductRemovalWithQuantityOutput:
    """Logic of the product_removal_quantity endpoint"""

    try:
        if not check_user_exists(payload.user_id):
            raise HTTPException(status_code=404, detail="User not found")
        async with session_maker.get_session() as session:
            my_sql = select(UserCart).where(
                and_(
                    UserCart.uid == payload.user_id, UserCart.pid == payload.product_id
                )
            )
            result = await session.execute(my_sql)
            record = result.first()
            if record and len(record) > 0:
                quantity = record[0].quantity - payload.quantity
                if quantity <= 0:
                    quantity = 0
                    my_query = delete(UserCart).where(
                        and_(
                            UserCart.uid == payload.user_id,
                            UserCart.pid == payload.product_id,
                        )
                    )
                else:
                    my_query = (
                        update(UserCart)
                        .where(
                            and_(
                                UserCart.uid == payload.user_id,
                                UserCart.pid == payload.product_id,
                            )
                        )
                        .values(quantity=quantity)
                    )
                compile = my_query.compile()
                result = await session.execute(my_query)
                await session.commit()
            else:
                return ProductRemovalWithQuantityOutput(removed=False)
            return ProductRemovalWithQuantityOutput(removed=True)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
