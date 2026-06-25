from sqlalchemy import Column, Float, Integer, String

from app.database.connection import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)