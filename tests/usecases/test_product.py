from uuid import UUID

import pytest

from store.core.exceptions import NotFoundExcpection
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase


async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_not_fount():
    with pytest.raises(NotFoundExcpection) as err:
        await product_usecase.get(id=UUID("b2ef2f3c-0e2c-4692-918f-31b7ad074b84"))

    assert (
        err.value.message
        == "Product not found with filter: b2ef2f3c-0e2c-4692-918f-31b7ad074b84"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, list)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_inserted, product_up):
    product_up.price = "7.500"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundExcpection) as err:
        await product_usecase.delete(id=UUID("b2ef2f3c-0e2c-4692-918f-31b7ad074b84"))

    assert (
        err.value.message
        == "Product not found with filter: b2ef2f3c-0e2c-4692-918f-31b7ad074b84"
    )
