from fastapi import FastAPI
from modules import get_routers

app = FastAPI()

for router in get_routers():
    app.include_router(router)
