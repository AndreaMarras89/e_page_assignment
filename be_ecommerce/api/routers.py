"""Endpoint Definition"""

from uuid import uuid4
from fastapi import APIRouter
from be_ecommerce.api.models import ProductSearchInput, ProductSearchOutput, Product
#from be_ecommerce.db.tables import Product, User, UserCart, UserData

router = APIRouter() #invoco costruttore default

@router.post(
    "/search",
    responses={200: {"model": ProductSearchOutput,"description" : ""}}
)
async def search_product(payload:str) -> ProductSearchOutput:
    return []
    #return [Product(id=str(uuid4()),name="scarpe",price=50, description="scarpe Nike fatte da bambini del bangladesh")]
    
    

