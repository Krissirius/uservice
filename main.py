from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.v1 import user
from api.endpoints import auth
from db.session import init_db

import uvicorn

app = FastAPI(
    title="U-Service для централизованного предоставления услуг пользователям"
)
@app.on_event("startup")
def on_startup():
    init_db()

# Подключаем роуты для аутентификации
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

