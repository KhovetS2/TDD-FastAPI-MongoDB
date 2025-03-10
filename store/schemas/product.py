from decimal import Decimal
from typing import Annotated

from bson import Decimal128
from pydantic import AfterValidator, BaseModel, Field

from store.schemas.base import BaseSchemasMixin, OutMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemasMixin):
    pass


class ProductOut(ProductIn, OutMixin):
    pass


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemasMixin):
    quantity: int | None = Field(None, description="Product quantity")
    price: Decimal_ | None = Field(None, description="Product price")
    status: bool | None = Field(None, description="Product status")


class ProductUpdateOut(ProductOut):
    pass
