
from . import *
from sqlalchemy import select
from models.UsersModel import Order, User, OrderItem
order_route = Blueprint('order',__name__)

@order_route.route('/order',methods=['GET'])
def getorder():
    orders= db.query(Order).all()
    return jsonify([o.serialize() for o in orders]), 200



@order_route.route('/order',methods=['POST'])
def createOrder():
    
    data = request.json
    # id_order = data.get("id_order")
    id_user = data.get("id_users")
    id_payment = data.get("id_payment")
    total =data.get("total")
    # created_at =data.get("create_at")
    status = data.get("status")
    order_items = data.get("order_items")
                    
    order = Order()
    db.session.add(order)
    db.session.commit()
    return make_response( {"message": 'User Created'},201 )
    # return jsonify(), 200


@order_route.route('/order/<int:id_user>',methods=['GET'])
def getOrderById(id_user:int):
    print("id_user",id_user)
    orders= db.query(Order).where(Order.id_user == id_user)
    response = [o.serialize() for o in orders]
    
    if not (len(response)):
        return jsonify({"message":"Order no encntrada","order":response}),200
    return jsonify([o.serialize() for o in orders]), 200


@order_route.route('/order/<int:id_user>/items',methods=['GET'])
def getOrderItem(id_user:int):
    print(id_user)
    orders= db.query(OrderItem).where(OrderItem.id_order_item == id_user)
    response = [o.serialize() for o in orders]
    print(len(response))
    if not (len(response)):
        print("es mayor")
        return jsonify({"message":"Orde  no encntrada","order":response}),200
    return jsonify([o.serialize() for o in orders]), 200

