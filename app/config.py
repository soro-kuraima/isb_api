from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./call_blocker.db"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()