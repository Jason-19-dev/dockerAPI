from . import *
from models.ProductModel import Product


product_route = Blueprint('product',__name__)

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
        # db.refresh(db_product)
        return db_product


@product_route.route("/product", methods=['GET'])
def getProducts():
   return ProductsController.get_products(db) 


@product_route.route("/product", methods=['POST'])
def createProducts():
    ProductsController.create_product(db, request.json)
    return jsonify({"message": 'Product Created'}),201


@product_route.route("/product/<id_product>", methods=['GET'])
def getProductsById(id_product):
    return jsonify(ProductsController.getProductById(db,id_product).serialize()),200


