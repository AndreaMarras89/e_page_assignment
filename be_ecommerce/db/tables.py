"""Definition of the tables"""

from sqlalchemy import UUID, Column, Float, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "Product"

    id = Column("ID", UUID, primary_key=True)
    name = Column("Name", String)
    price = Column("Price", Float)
    description = Column("Description", Text)


class User(Base):
    __tablename__ = "User"

    uid = Column("UID", UUID, primary_key=True)
    username = Column("Username", String)
    password = Column("Pass", String)


class UserCart(Base):
    __tablename__ = "User_Cart"

    pid = Column("PID", UUID, primary_key=True)
    uid = Column("UID", UUID, primary_key=True)
    quantity = Column("Quantity", Integer)


class UserData(Base):
    __tablename__ = "User_Data"

    cod_u = Column("CodU", UUID, primary_key=True)
    card_num = Column("Card_Num", Integer)
