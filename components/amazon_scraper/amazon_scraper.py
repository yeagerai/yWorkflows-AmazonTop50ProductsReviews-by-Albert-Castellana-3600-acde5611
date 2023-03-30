
import os
from typing import List, Dict, Union

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import requests

from core.abstract_component import AbstractComponent


class AmazonScraperInputDict(BaseModel):
    product_name: str


class AmazonScraperOutputDict(BaseModel):
    product_results: List[Dict[str, Union[str, int]]]


class AmazonScraper(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.api_key: Optional[str] = os.environ.get(
            yaml_data["parameters"]["api_key"]
        )
        self.search_results_limit: int = yaml_data["parameters"]["search_results_limit"]

    def transform(
        self, args: AmazonScraperInputDict
    ) -> AmazonScraperOutputDict:
        search_url = f"https://example-amazon-api.com/search?query={args.product_name}&limit={self.search_results_limit}"
    
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.get(search_url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error calling the Amazon API: {response.text}")

        search_results = response.json()
        
        products = [
            {
                "url": product["url"],
                "name": product["name"],
                "asin": product["asin"],
            }
            for product in search_results["products"]
        ]

        out = AmazonScraperOutputDict(
            product_results=products
        )
        return out


load_dotenv()
amazon_scraper_app = FastAPI()


@amazon_scraper_app.post("/transform/")
async def transform(
    args: AmazonScraperInputDict,
) -> AmazonScraperOutputDict:
    amazon_scraper = AmazonScraper()
    return amazon_scraper.transform(args)
