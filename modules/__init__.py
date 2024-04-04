# modules/__init__.py

import importlib
import os

# 获取当前目录的绝对路径
current_directory = os.path.dirname(os.path.abspath(__file__))

# 创建一个空列表来存储所有的路由器
routers = []

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 检查文件是否是一个 Python 文件并且不是 __init__.py
    if filename.endswith('.py') and filename != '__init__.py':
        # 构造模块的完整名称
        module_name = 'modules.' + filename[:-3]  # 去掉 .py 后缀

        # 尝试导入模块
        try:
            module = importlib.import_module(module_name)

            # 假设每个模块都定义了一个名为 'router' 的变量
            router = getattr(module, 'router', None)

            # 如果找到了 router，则添加到路由列表中
            if router is not None:
                routers.append(router)
        except ImportError as e:
            # 打印导入错误，但不影响其他模块的加载
            print(f"Failed to import {module_name}: {e}")

        # 提供一个方便的方式来获取所有的路由器


def get_routers():
    return routers

# from .module_02 import router as module_02_router
# from .module_03 import router as module_03_router
# from .module_04 import router as module_04_router
#
# routers = [
#     module_02_router,
#     module_03_router,
#     module_04_router,
# ]
