from sqlalchemy.orm import Session
from models.UsersModel import User,Order
from models.ProductModel import Product 
from flask import jsonify
import uuid
import datetime
import logging

logs = logging.getLogger(__name__)

class AuthController():
    def generate_token():
        return f"{datetime.datetime.now().strftime("%y%m%d")}{uuid.uuid4().hex}"
        
    def login(db:Session, resquest):
        pass
    
    def register(db:Session, request_data):
        
        existing_user = db.query(User).filter((User.username == request_data["username"]) | (User.email == request_data["email"])).first()

        if existing_user:
            conflict_field = "username" if existing_user.username == request_data["username"] else "email"
            logs.warning(f"{conflict_field.capitalize()} ya registrado")
            return jsonify({"message": f"El {conflict_field} ya está en uso", "field": conflict_field}), 409  
        try:
            new_user = User(**request_data)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            logs.info("Usuario creado exitosamente")
            return jsonify({"message": "Usuario creado exitosamente","user_id": new_user.id}), 201
        except Exception as e:
            db.rollback() 
            logs.error(f"Error al crear usuario: {str(e)}")
            return jsonify({"message": "Error interno al crear usuario", "error": str(e)}), 500
        
    

class UsersController():
    def get_user(db:Session):
        return db.query(User).all()

    def create_user(db:Session, user):
        db_user =User(**user.model_dump())
        print(db_user)
        # db.add(db_user)
        # db.commit()
        # db.refresh(db_user)
        # return db_user

class ProductsController():
    
    def get_products(db:Session):
        product = db.query(Product).all()
        return jsonify([product.serialize() for product in product]),200
    
    def getProductById(db:Session,id_product:int):
        return db.query(Product).filter(Product.id_product == id_product).first()
    
    def create_product(db:Session, product):
        db_product =Product(**product)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product



class OrderController():
    
    def get_order(db:Session):
        return db.query(Order).all()

    def create_order(db:Session, order):
        db_order =Order(**order)
        db.add(db_order)    
        db.commit()
        db.refresh(db_order)    
        return db_order
    
    def getOrderById(db:Session,id_user):
        
        orders= db.query(Order).filter(Order.id_user == id_user).first()
        response = [o.serialize() for o in orders]
        print(len(response))
        if not (len(response)):
            return jsonify({"message":"Order no encntrada","order":response}),200
        return jsonify(response), 200