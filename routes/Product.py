from . import *
from controller.Controller import ProductsController
product_route = Blueprint('product',__name__)


@product_route.route("/product", methods=['GET'])
def getProducts():
   return ProductsController.get_products(db) 


@product_route.route("/product", methods=['POST'])
def createProducts():
    ProductsController.create_product(db, request.json)
    return jsonify({"message": 'Product Created'}),201


@product_route.route("/product/<int:id_product>", methods=['GET'])
def getProductsById(id_product):
    return jsonify(ProductsController.getProductById(db,id_product).serialize()),200


