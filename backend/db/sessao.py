from enum import auto
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.config import configuracoes

motor = create_engine(configuracoes.DB_URL, pool_pre_ping = True)
sessao = sessionmaker(bind=motor, autoflush= False, autocommit = False)
