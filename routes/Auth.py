# import uuid
# from main import app
# from utils.db  import db
# from flask import request, jsonify, Blueprint

# user_route = Blueprint('users',__name__)

# @app.route('/users', methods=['POST'])
# def crear_usuario():
#     data = request.json
#     user_id = str(uuid.uuid4())
#     nuevo_usuario = db.User(user_id=user_id, nombre=data["nombre"], email=data["email"])
#     db.session.add(nuevo_usuario)
#     db.session.commit()
    
    # return jsonify({"user_id": user_id}), 201