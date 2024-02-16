"""Input&Output Intefaces definition"""

#from be_ecommerce.db.tables import Product
from typing import List

from pydantic import UUID4, BaseModel


class Product(BaseModel):
    id:str
    name:str
    price:float
    description:str
    
#Ricerca Prodotto
class ProductSearchInput(BaseModel):
    query: str
    
class ProductSearchOutput(BaseModel):
    products: List[str]
    
#Aggiungi Carrello
class ProductAddCartInput(BaseModel):
    user_id: UUID4
    product_id: UUID4
    quantity: int = 1
    
class ProductAddCartOutput(BaseModel):
    added: bool
    
#Dettaglio Prodotti
class ProductDetailsInput(BaseModel):
    product_id : UUID4
    
class ProductDetailsOutput(BaseModel):
    product_name: str
    product_decription: str
    product_price: float

#Rimozione Carrello
class ProductRemovalInput(BaseModel):
    product_id : UUID4
    
class ProductRemovalOutput(BaseModel):
    removed: bool