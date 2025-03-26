"""
    Rutas para manejar loos usuarios 
"""
from . import *
from models.UsersModel import User, Order
user_route = Blueprint('users',__name__) 


@user_route.route("/users",methods=['GET'])
def getUsers():
    users= db.query(User).all()
    users_list = [user.serialize() for user in users]
    return jsonify(users_list), 200

@user_route.route("/users/<id_user>",methods=['GET'])
def getUserById(id_user):
    user= db.query(User).where(User.id_user == id_user).first()
    return jsonify(user.serialize()), 200


@user_route.route("/users/<id_user>/order",methods=['POST'])
def getUserOrderById(id_user):
    orderUser= db.query(Order).where(User.id_user == id_user).all()
    users_list = [user.serialize() for user in orderUser]
    return jsonify(users_list), 200

