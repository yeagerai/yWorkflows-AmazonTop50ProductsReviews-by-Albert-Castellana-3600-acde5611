
import os
import pytest
from dotenv import load_dotenv

from fastapi.testclient import TestClient
from pydantic import ValidationError

from components.path_to_your_component import AmazonScraper, AmazonScraperInputDict, AmazonScraperOutputDict
from components.path_to_your_component import amazon_scraper_app

load_dotenv()
client = TestClient(amazon_scraper_app)


@pytest.mark.parametrize(
    "input_data, expected_output_data",
    [
        (
            {"product_name": "test product 1"},
            {
                "product_results": [
                    {
                        "url": "https://amazon.com/test-product-url-1",
                        "name": "Test Product 1",
                        "asin": 123456789,
                    },
                    {
                        "url": "https://amazon.com/test-product-url-2",
                        "name": "Test Product 2",
                        "asin": 987654321,
                    },
                ]
            },
        ),
        (
            {"product_name": "test product 2"},
            {
                "product_results": [
                    {
                        "url": "https://amazon.com/test-product-url-3",
                        "name": "Test Product 3",
                        "asin": 123123123,
                    },
                    {
                        "url": "https://amazon.com/test-product-url-4",
                        "name": "Test Product 4",
                        "asin": 789789789,
                    },
                ]
            },
        ),
    ],
)
def test_amazon_scraper_transform(input_data, expected_output_data, mocker):
    # Mock requests.get to return a custom response
    response_content = {"products": expected_output_data["product_results"]}
    mocker.patch("requests.get", return_value=mocker.Mock(ok=True, json=lambda: response_content))

    # Use TestClient to call transform() API endpoint
    response = client.post("/transform/", json=input_data)
    
    # Assert the status code and response content
    assert response.status_code == 200
    assert response.json() == expected_output_data


@pytest.mark.parametrize(
    "invalid_data",
    [
        {"product_name": ""},
        {"invalid_key": "test product"},
    ],
)
def test_amazon_scraper_transform_invalid_data_invalid(invalid_data):
    with pytest.raises(ValidationError):
        AmazonScraperInputDict(**invalid_data)


def test_amazon_scraper_transform_unauthorized(mocker):
    # Mock requests.get to return an unauthorized response
    mocker.patch("requests.get", return_value=mocker.Mock(ok=False, text="Unauthorized"))

    # Use TestClient to call the transform() API endpoint with an example input
    input_data = {"product_name": "test product"}
    response = client.post("/transform/", json=input_data)

    # Assert the status code and error message
    assert response.status_code == 500
    assert response.text == "Error calling the Amazon API: Unauthorized"
