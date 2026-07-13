import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.config import CORS_ORIGINS, settings
from app.routers.users import router as user_router
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.include_router(user_router)


@app.get("/health")
def health():
    return {"Status": "ok", "port": os.environ.get("PORT", "NOT SET")}
