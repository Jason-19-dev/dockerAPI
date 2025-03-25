import datetime
from pydantic import BaseModel, ConfigDict
from typing import List, Optional

    
class UserSchema(BaseModel):
    id_user: int
    first_name: str
    last_name : str
    usernama: str
    email : str
    password_hash : str
    phone : str
    created_at : str
    auth_provider : str
    is_guest : bool
    

class PaymentMethod(BaseModel):
    id_payment : int
    id_user : int
    card_number :str
    card_holder :str
    expiration_date: str
    cvv: str
    created_at: str 
    
    user : List[UserSchema]



class Product(BaseModel):
    id_product: int
    name : str
    description: str 
    price :float
    stock :int
    created_at :str
    
class Order(BaseModel):
    id: int
    date: str
    delivery_type: str
    total: float
    state: str
    items: List[Product]
    # items: List[item]