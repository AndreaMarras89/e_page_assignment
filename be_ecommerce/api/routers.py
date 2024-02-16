"""Endpoint Definition"""

from uuid import uuid4

from fastapi import APIRouter

from be_ecommerce.api.models import (Product, ProductAddCartInput,
                                     ProductAddCartOutput, ProductSearchInput,
                                     ProductSearchOutput,ProductDetailsInput, ProductDetailsOutput,
                                     ProductRemovalInput, ProductRemovalOutput)

#from be_ecommerce.db.tables import Product, User, UserCart, UserData

router = APIRouter() #invoco costruttore default

@router.post(
    "/search",
    responses={200: {"model": ProductSearchOutput,"description" : ""}}
)
async def search_product(payload: ProductSearchInput) -> dict:
    return {"products": [Product(id=str(uuid4()),name="scarpe",price=50, description="scarpe Nike fatte da bambini del bangladesh")]}
    

@router.post(
    "/add_product",
    responses={200: {"model":ProductAddCartOutput,"description" : ""}}
)
async def add_to_cart(payload: ProductAddCartInput) -> ProductAddCartOutput:
    return {"added": True}

@router.post(
    "/product_details",
    responses={200: {"model": ProductDetailsOutput,"description" : ""}}
)
async def product_details(payload:ProductDetailsInput) -> ProductDetailsOutput:
    return {"product_name": "Scarpe", "product_decription" : "indossate dal cavaliere", "product_price" : 23}

@router.post(
    "/product_removal",
    responses={200: {"model": ProductRemovalOutput, "descrption" : ""}}
)
async def product_removal(payload:ProductRemovalInput) -> ProductRemovalOutput:
    return {"removed": True}


