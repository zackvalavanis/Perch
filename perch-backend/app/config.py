from pydantic_settings import BaseSettings
from pydantic import ConfigDict


CORS_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    "https://cue-finder-acqq.vercel.app",
    "https://cue-finder-acqq.vercel.app/",
]


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
