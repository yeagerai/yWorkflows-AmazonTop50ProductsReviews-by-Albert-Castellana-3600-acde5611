
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow

class ProductNameModel(BaseModel):
    product_name: str

class FileModel(BaseModel):
    file_path: str

class AmazonTop50ProductsReviews(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: ProductNameModel, callbacks: typing.Any
    ) -> FileModel:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        file_path = results_dict[0].file_path
        out = FileModel(
            file_path=file_path
        )
        return out

load_dotenv()
amazon_top50_products_reviews_app = FastAPI()

@amazon_top50_products_reviews_app.post("/transform/")
async def transform(
    args: ProductNameModel,
) -> FileModel:
    amazon_top50_products_reviews = AmazonTop50ProductsReviews()
    return await amazon_top50_products_reviews.transform(args, callbacks=None)

