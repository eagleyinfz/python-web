from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from settings import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_POOL_RECYCLE

db_engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=SQLALCHEMY_POOL_RECYCLE, pool_size=100,
                          convert_unicode=True, echo=False, encoding='utf-8')
db_session = scoped_session(sessionmaker(bind=db_engine))
