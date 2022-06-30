from pydantic import BaseSettings, conint

class Config(BaseSettings):
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"

configuracoes = Config()