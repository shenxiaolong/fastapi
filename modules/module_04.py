# 请求体
# https://fastapi.tiangolo.com/zh/tutorial/body/

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/module_04/items/")
async def create_item(item: Item):
    return item
