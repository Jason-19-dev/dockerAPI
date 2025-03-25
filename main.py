from flask import Flask
from flask_cors import CORS
from routes import Orders,Product, User 

app = Flask(__name__)
CORS(app)
app.register_blueprint(User.user_route)
app.register_blueprint(Product.product_route)     
app.register_blueprint(Orders.order_route)     

if __name__ == "__main__":
    app.run(debug=True)
