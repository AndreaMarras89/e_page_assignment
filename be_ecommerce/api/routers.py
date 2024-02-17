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
from be_ecommerce.db.tables import User, UserCart, UserData
from be_ecommerce.db.utils import AsyncDatabaseSession

router = APIRouter()  # invoco costruttore default


# Funzione check user
async def check_user_exists(user_id: str) -> bool:
    session_maker = AsyncDatabaseSession()
    async with session_maker.get_session() as session:
        my_query = select(User).where(user_id == User.uid)
        result = await session.execute(my_query)
        return_value = result.first()
        if return_value and len(return_value) > 0:
            return True
        return False


# Funzione check product
async def check_product_exists(product_id: str) -> bool:
    session_maker = AsyncDatabaseSession()
    async with session_maker.get_session() as session:
        my_query = select(ProductTable.id).where(ProductTable.id == product_id)
        result = await session.execute(my_query)
        return_value = result.first()
        if return_value and len(return_value) > 0:
            return True
        return False


@router.post(
    "/search", responses={200: {"model": ProductSearchOutput, "description": ""}}
)
async def search_product(payload: ProductSearchInput) -> dict:
    session_maker = AsyncDatabaseSession()
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
        return {"products": result_list}


@router.post(
    "/add_product", responses={200: {"model": ProductAddCartOutput, "description": ""}}
)
async def add_to_cart(payload: ProductAddCartInput) -> ProductAddCartOutput:
    session_maker = AsyncDatabaseSession()
    async with session_maker.get_session() as session:
        if await check_user_exists(payload.user_id) and await check_product_exists(
            payload.product_id
        ):
            my_sql = select(UserCart).where(
                and_(
                    UserCart.uid == payload.user_id, UserCart.pid == payload.product_id
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
    return {"added": True}


@router.post(
    "/product_details",
    responses={200: {"model": ProductDetailsOutput, "description": ""}},
)
async def product_details(payload: ProductDetailsInput) -> ProductDetailsOutput:
    session_maker = AsyncDatabaseSession()
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


@router.post(
    "/product_removal_all",
    responses={200: {"model": ProductRemovalAllOutput, "descrption": ""}},
)
async def product_removal_all(
    payload: ProductRemovalAllInput,
) -> ProductRemovalAllOutput:
    if not check_user_exists(payload.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    session_maker = AsyncDatabaseSession()
    async with session_maker.get_session() as session:
        my_sql = delete(UserCart).where(UserCart.uid == payload.user_id)
        compile = my_sql.compile()
        result = await session.execute(my_sql)
        await session.commit()
        return {"removed": True}


@router.post(
    "/product_removal_quantity",
    responses={200: {"model": ProductRemovalWithQuantityOutput, "descrption": ""}},
)
async def product_removal_quantity(
    payload: ProductRemovalWithQuantityInput,
) -> ProductRemovalWithQuantityOutput:
    session_maker = AsyncDatabaseSession()
    if not check_user_exists(payload.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    async with session_maker.get_session() as session:
        my_sql = select(UserCart).where(
            and_(UserCart.uid == payload.user_id, UserCart.pid == payload.product_id)
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
            return {"removed": False}
        return {"removed": True}
