from . import *
from controller.Controller import AuthController


user_route = Blueprint('auth',__name__)

@user_route.route('/login', methods=['POST'])
def crear_usuario():
    data = request.json
    token = AuthController.generate_token()
    
    return jsonify({"token": token}), 201

