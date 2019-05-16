from sqlalchemy import Column, String, Text, Integer, BigInteger, Enum, Table, ForeignKey, DateTime, LargeBinary, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from settings import SQLALCHEMY_DATABASE_URI

Base = declarative_base()
if 'sqlite' in SQLALCHEMY_DATABASE_URI:
    BigInteger = BigInteger().with_variant(Integer, "sqlite")


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))

    def __repr__(self):
        return "<User : [{}]>".format(self.id, self.name)
