import pytest
from fastapi import status
from httpx import AsyncClient

from tests.factories import product_data


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.json()
    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Iphone 14 Pro Max",
        "quantity": 18,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    content = response.json()
    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 18,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_not_found(
    client,
    products_url,
):
    response = await client.get(f"{products_url}b2ef2f3c-0e2c-4692-918f-31b7ad074b84")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: b2ef2f3c-0e2c-4692-918f-31b7ad074b84"
    }


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_success(
    client,
    products_url,
):
    response = await client.get(products_url)

    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response_json, list)
    assert len(response_json) > 1


async def test_controller_patch_should_return_success(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"price": "7.500"}
    )

    content = response.json()
    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 18,
        "price": "7.500",
        "status": True,
    }


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(
    client: AsyncClient,
    products_url: str,
):
    response = await client.delete(
        f"{products_url}b2ef2f3c-0e2c-4692-918f-31b7ad074b84"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: b2ef2f3c-0e2c-4692-918f-31b7ad074b84"
    }
