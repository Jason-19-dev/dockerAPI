from . import *
from schemas.schemas import Product
from pydantic import BaseModel, ConfigDict
import datetime as dt
from typing import List


class Product(Base):
    __tablename__ = "products"
    
    id_product = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer)
    image_url = Column(String(255))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
    
    def serialize(self):
        return{
            "id_product": self.id_product,
            "name": self.name,  
            "description": self.description,
            "price": self.price,
            "image_url":self.image_url,
            "stock": self.stock,
            "created_at": self.created_at
        }
    
        
        
class ProductScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_product: int
    name: str
    description: str
    price: float
    stock: int
    image_url: str
    created_at: dt.datetime
    