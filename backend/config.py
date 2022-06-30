from pydantic import BaseConfig

class config(BaseConfig):
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"