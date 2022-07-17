from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Satisfactory Planner"
    mongo_db: str

    class Config:
        env_file = ".env"


settings = Settings()
