from . import *
from utils.Controller import HandlerProducts

product_route = Blueprint('product',__name__)


@product_route.route("/product", methods=['GET'])
def getProducts():
    products = HandlerProducts.get_products(db)
    return jsonify([product.serialize() for product in products]),200


@product_route.route("/product", methods=['POST'])
def createProducts():
    HandlerProducts.create_product(db, request.json)
    return jsonify({"message": 'Product Created'}),201


@product_route.route("/product/<int:id_product>", methods=['GET'])
def getProductsById(id_product):
    return jsonify(HandlerProducts.getProductById(db,id_product).serialize()),200


