# 查询参数
# https://fastapi.tiangolo.com/zh/tutorial/query-params/

from fastapi import APIRouter

router = APIRouter()


fake_items_db = [{"item_name": "Apple"}, {"item_name": "Banana"}, {"item_name": "Cat"},
                 {"item_name": "Dog"}, {"item_name": "Egg"}, {"item_name": "Fly"},
                 {"item_name": "Green"}, {"item_name": "High"}]

# http://127.0.0.1:8000/read_items/?skip=1&limit=5
@router.get("/module_03/read_items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# http://127.0.0.1:8000/read_user_item/1?needy=needy&skip=3
@router.get("/module_03/read_user_item/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
