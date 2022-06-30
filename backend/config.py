from pydantic import BaseConfig, conint

class Config(BaseConfig):
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"

configuracoes = Config()