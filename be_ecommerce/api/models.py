"""Input&Output Intefaces definition"""

from pydantic import BaseModel
#from be_ecommerce.db.tables import Product
from typing import List

class Product(BaseModel):
    id:str
    name:str
    price:float
    description:str

class ProductSearchInput(BaseModel):
    query:str
    
    
    
class ProductSearchOutput(BaseModel):
    products:List[Product]