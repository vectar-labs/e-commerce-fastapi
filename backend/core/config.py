from pydantic_settings import BaseSettings


class Settings(BaseSettings): # type: ignore
    # The format is postgresql+ASYNC_DRIVER://user:password@postgresserver/db
    DATABASE_URL: str = "postgresql+asyncpg://postgres:kitindi@localhost/e_commerce_db"
    
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()



