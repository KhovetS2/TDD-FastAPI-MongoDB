from pydantic import Field

from store.schemas.base import BaseSchemasMixin


class ProductIn(BaseSchemasMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")
