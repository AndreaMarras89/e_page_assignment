"""Input&Output Intefaces definition"""

# from be_ecommerce.db.tables import Product
from typing import List

from pydantic import UUID4, BaseModel


class Product(BaseModel):
    id: str
    name: str
    price: float
    description: str


# Ricerca Prodotto
class ProductSearchInput(BaseModel):
    query: str


class ProductSearchOutput(BaseModel):
    products: List[str]


# Aggiungi Carrello
class ProductAddCartInput(BaseModel):
    user_id: UUID4
    product_id: UUID4
    quantity: int = 1


class ProductAddCartOutput(BaseModel):
    added: bool


# Dettaglio Prodotti
class ProductDetailsInput(BaseModel):
    product_id: UUID4


class ProductDetailsOutput(BaseModel):
    product_name: str
    product_description: str
    product_price: float


# Rimozione tutti Carrello
class ProductRemovalAllInput(BaseModel):
    user_id: UUID4


class ProductRemovalAllOutput(BaseModel):
    removed: bool


# Rimozione Carrello con quantità
class ProductRemovalWithQuantityInput(BaseModel):
    user_id: UUID4
    product_id: UUID4
    quantity: int


class ProductRemovalWithQuantityOutput(BaseModel):
    removed: bool
