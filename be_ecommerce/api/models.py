"""Input&Output Intefaces definition"""

# from be_ecommerce.db.tables import Product
from typing import List

from pydantic import UUID4, BaseModel


class Product(BaseModel):
    """Model for Product"""

    id: str
    name: str
    price: float
    description: str


# Ricerca Prodotto
class ProductSearchInput(BaseModel):
    """Input model for search endpoint"""

    query: str


class ProductSearchOutput(BaseModel):
    """Output model for search endpoint"""

    products: List[str]


# Aggiungi Carrello
class ProductAddCartInput(BaseModel):
    """Input model for add_product endpoint"""

    user_id: UUID4
    product_id: UUID4
    quantity: int = 1


class ProductAddCartOutput(BaseModel):
    """Output model for add_product endpoint"""

    added: bool


# Dettaglio Prodotti
class ProductDetailsInput(BaseModel):
    """Input model for product_details endpoint"""

    product_id: UUID4


class ProductDetailsOutput(BaseModel):
    """Output model for product_details endpoint"""

    product_name: str
    product_description: str
    product_price: float


class ProductRemovalAllInput(BaseModel):
    """Input model for product_removal_all endpoint"""

    user_id: UUID4


class ProductRemovalAllOutput(BaseModel):
    """Output model for product_removal_all endpoint"""

    removed: bool


class ProductRemovalWithQuantityInput(BaseModel):
    """Input model product_removal_quantity endpoint"""

    user_id: UUID4
    product_id: UUID4
    quantity: int


class ProductRemovalWithQuantityOutput(BaseModel):
    """Output model product_removal_quantity endpoint"""

    removed: bool
