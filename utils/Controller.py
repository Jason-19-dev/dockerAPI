from sqlalchemy.orm import Session
from models.UsersModel import User,Order
from models.ProductModel import Product 
from flask import jsonify

class HandlerUsers():

    def get_user(db:Session):
        return db.query(User).all()

    def create_user(db:Session, user):
        db_user =User(**user.model_dump())
        print(db_user)
        # db.add(db_user)
        # db.commit()
        # db.refresh(db_user)
        # return db_user
from pydantic import BaseModel, validator

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
class HandlerProducts():
    
    def get_products(db:Session):
        return db.query(Product).all()
    
    def getProductById(db:Session,id_product:int):
        return db.query(Product).filter(Product.id_product == id_product).first()
    
    def create_product(db:Session, product):
        db_product =Product(**product)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product



class HandlerOrder():
    
    def get_order(db:Session):
        return db.query(Order).all()

    def create_order(db:Session, order):
        db_order =Order(**order)
        db.add(db_order)    
        db.commit()
        db.refresh(db_order)    
        return db_order
    
    def getOrderById(db:Session,id_user:int):
        orders= db.query(Order).filter(Order.id_user == id_user).first()
        response = [o.serialize() for o in orders]
        print(len(response))
        if not (len(response)):
            return jsonify({"message":"Order no encntrada","order":response}),200
        return jsonify(response), 200