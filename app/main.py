from fastapi import FastAPI
from app.schemas import GrantCreate
from app.crud import create_grant, get_grants

app = FastAPI(title="Funding Aggregator KZ")

# GET: показать все гранты
@app.get("/grants")
def read_grants():
    return get_grants()

# POST: добавить грант вручную
@app.post("/grants")
def add_grant(grant: GrantCreate):
    return create_grant(grant)

# Тестовый collect (пока возвращает 0)
@app.get("/collect")
def collect_grants():
    return {"saved": 0}
