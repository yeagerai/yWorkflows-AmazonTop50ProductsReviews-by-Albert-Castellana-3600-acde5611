
# Import necessary libraries and the component
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from your_module_here import (
    AmazonTop50ProductsReviews,
    ProductNameModel,
    FileModel,
    amazon_top50_products_reviews_app,
)

# Define test cases with mocked input and expected output data
test_data = [
    (
        {"product_name": "Test Product 1"},
        {"file_path": "/path/to/test-product1-reviews.csv"},
    ),
    (
        {"product_name": "Test Product 2"},
        {"file_path": "/path/to/test-product2-reviews.csv"},
    ),
]

# Test cases with edge cases for product names
edge_cases = [
    # Empty product name
    (
        {"product_name": ""},
        {},
    ),
    # Product name containing only spaces
    (
        {"product_name": "   "},
        {},
    ),
]


@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_amazon_top50_products_reviews(input_data, expected_output):
    # Create an instance of the AmazonTop50ProductsReviews class
    amazon_top50_products_reviews = AmazonTop50ProductsReviews()

    # Call the transform() method with mocked input data
    input_model = ProductNameModel(**input_data)
    result = amazon_top50_products_reviews_app(input_model)

    # Assert that the output matches the expected output
    assert result == FileModel(**expected_output)


@pytest.mark.parametrize("input_data, expected_output", edge_cases)
def test_amazon_top50_products_reviews_edge_cases(input_data, expected_output):
    # Test edge cases in input data
    with pytest.raises(ValidationError):
        # Create an instance of the ProductNameModel with invalid input
        ProductNameModel(**input_data)


def test_amazon_top50_products_reviews_endpoint():
    # Test the FastAPI endpoint using TestClient
    client = TestClient(amazon_top50_products_reviews_app)

    # Define an example request data
    request_data = {"product_name": "Test Product"}

    # Call the /transform/ endpoint
    response = client.post("/transform/", json=request_data)

    # Assert that the response contains the expected data
    assert response.status_code == 200
    assert "file_path" in response.json()
