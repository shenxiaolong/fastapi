# 返回各种数据类型

from fastapi import APIRouter

router = APIRouter()

# http://127.0.0.1:8000/type
@router.get("/type")
def type():
    return {
        "int": 24,
        "float": 3.141592653,
        "bool": False,
        "str": "string",
        "list": [1,2,3,'a','b','c'],
        # 元组，与列表类似，但元组是不可变的。
        "tuple": (1,2,3),
        # 字典，无序的键值对集合。
        "dict": {'name': 'Alice', 'age': 30},
        # 集合，无序且不包含重复元素的序列。
        "set": {1, 2, 3}
    }
