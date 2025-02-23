import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    CELERY_BROKER: str = os.getenv("CELERY_BROKER", "redis://localhost:6379/0")
    CELERY_BACKEND: str = os.getenv("CELERY_BACKEND", "redis://localhost:6379/1")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    ACCESS_KEY : str = os.getenv("ACCESS_KEY")
    SECRET_KEY : str = os.getenv("SECRET_KEY")
    BUCKET_NAME : str = os.getenv("BUCKET_NAME")
    FOLDER_NAME : str = os.getenv("FOLDER_NAME")
    REGION : str = os.getenv("REGION")


settings = Settings()
