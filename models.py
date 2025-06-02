from sqlalchemy import Column, Integer, String, Float
from database import Base


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    qnt_products = Column(Integer)
    price = Column(Float)
    image = Column(String)