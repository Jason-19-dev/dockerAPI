
from . import *

class User(Base):
    __tablename__ = "users"
    
    id_user = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(20))
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    # auth_provider = Column(Enum('email', 'google', 'facebook'), nullable=False)
    is_guest = Column(Boolean, default=False)
    avatar = Column(String(255))
    birth_date = Column(Date), 
    # payment_methods = relationship("PaymentMethod", back_populates="user")
    # orders = relationship("Order", back_populates="user")
    # wallet = relationship("Wallet", back_populates="user")
    # savings = relationship("Saving", back_populates="user")
    # user_saving_plans = relationship("UserSavingPlan", back_populates="user")
    # shopping_cart = relationship("ShoppingCart", back_populates="user")
    
    def serialize(self):
        
        return {
            "id_user": self.id_user,
            "avatar": self.avatar,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "phone": self.phone,
            "create_at": self.created_at,
            "is_guest": self.is_guest,
            # "payment_methods": [pm.serialize() for pm in self.payment_methods],
            # "orders": [o.serialize() for o in self.orders],
            # "auth_provider": self.auth_provider,
            # "wallet": [w.serialize() for w in self.wallet],
            # "savings": self.savings, 
            # "shopping_cart": self.shopping_cart,
            # "user_saving_plans": self.user_saving_plans,
        }




class PaymentMethod(Base):
    __tablename__ = "payment_methods"
    
    id_payment = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    card_number = Column(String(16), nullable=False)
    card_holder = Column(String(255), nullable=False)
    expiration_date = Column(Date, nullable=False)
    cvv = Column(String(4), nullable=False)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    
    # user = relationship("User", back_populates="payment_methods")
    
    def serialize(self):
        return {
            "id_payment ": self.id_payment,
            "id_user ": self.id_user,
            "card_number ": self.card_number,
            "card_holder ": self.card_holder,
            "expiration_date ": self.expiration_date,
            "cvv ": self.cvv,
            "created_at ": self.created_at,
            # "user ": self.user.serialize() if self.user else None   
        }


class Order(Base):
    __tablename__ = "orders"
    
    id_order = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    id_payment = Column(Integer)
    total = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    status = Column(Enum('pending', 'completed', 'cancelled'), default='pending')

    # user = relationship("User", back_populates="orders")
    # payment_method = relationship("PaymentMethod")
    # order_items = relationship("OrderItem", back_populates="order")

    def serialize(self):
        return {
            "id_order": self.id_order,
            "id_user": self.id_user,
            "id_payment": self.id_payment,
            "total": self.total,
            "created_at": self.created_at,
            "status": self.status,
            # "user":  self.user.serialize() if self.user else None,
            # "payment_method": self.payment_method.serialize() if self.payment_method else None,
            # "order_items": [item.serialize() for item in self.order_items]
        }
    


class OrderItem(Base):
    __tablename__ = "order_items"
    
    id_order_item = Column(Integer, primary_key=True)
    id_order = Column(Integer)
    id_product = Column(Integer)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    # order = relationship("Order", back_populates="order_items")
    # product = relationship("Product")

    def serialize(self):
        return {
            "id_order_item": self.id_order_item,
            "id_order": self.id_order,
            "id_product": self.id_product,
            "quantity": self.quantity,
            "price": self.price,
            "product": self.id_product
        }


class Wallet(Base):
    
    __tablename__ = "wallet"
    
    id_wallet = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    balance = Column(Float, default=0.00)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    
    # user = relationship("User", back_populates="wallet")
    # interest_history = relationship("InterestHistory", back_populates="wallet")

    def serialize(self):
        return {
            "id_wallet": self.id_wallet,
            "id_user": self.id_user,
            "balance": self.balance,
            "created_at": self.created_at,
            "user": self.user.serialize() if self.user else None,
            "interest_history": [ih.serialize() for ih in self.interest_history] if self.interest_history else []
        }
        
class Saving(Base):
    __tablename__ = "savings"
    
    id_saving = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    id_order = Column(Integer, ForeignKey('orders.id_order'), nullable=False)
    amount_saved = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    # user = relationship("User", back_populates="savings")
    # order = relationship("Order")

    def serialize(self):
        return {
            "id_saving": self.id_saving,
            "id_user": self.id_user,
            "id_order": self.id_order,
            "amount_saved": self.amount_saved,
            "created_at": self.created_at,
            # "user": self.user,
            # "order": self.order
        }


class SavingPlan(Base):
    __tablename__ = "saving_plans"
    
    id_plan = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    min_amount = Column(Float, nullable=False)
    min_transactions = Column(Integer, nullable=False)
    annual_interest = Column(Float, nullable=False)

    def serialize(self):
        return {
            "id_plan": self.id_plan,
            "name": self.name,
            "min_amount": self.min_amount,
            "min_transactions": self.min_transactions,
            "annual_interest": self.annual_interest
        }


class UserSavingPlan(Base):
    __tablename__ = "user_saving_plans"
    
    id_user = Column(Integer, ForeignKey('users.id_user'), primary_key=True, nullable=False)
    id_plan = Column(Integer, ForeignKey('saving_plans.id_plan'), primary_key=True, nullable=False)
    start_date = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    # user = relationship("User", back_populates="user_saving_plans")
    # saving_plan = relationship("SavingPlan")

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_plan": self.id_plan,
            "start_date": self.start_date,
        #     "user": self.user,
        #     "saving_plan": self.saving_plan
        }

class ShoppingCart(Base):
    __tablename__ = "shopping_cart"
    
    id_cart = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    products = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    
    # user = relationship("User", back_populates="shopping_cart")

    def serialize(self):
        return {
            "id_cart": self.id_cart,
            "id_user": self.id_user,
            "products": self.products,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # "user": self.user.serialize() if self.user else None
        }


class InterestHistory(Base):
    __tablename__ = "interest_history"
    
    id_interest = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    id_wallet = Column(Integer, ForeignKey('wallet.id_wallet'), nullable=False)
    interest_amount = Column(Float, nullable=False)
    calculated_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    # user = relationship("User")
    # wallet = relationship("Wallet", back_populates="interest_history")

    def serialize(self):
        return {
            "id_interest": self.id_interest,
            "id_user": self.id_user,
            "id_wallet": self.id_wallet,
            "interest_amount": self.interest_amount,
            "calculated_at": self.calculated_at,
            # "user": self.user.serialize() if self.user else None,
            # "wallet": self.wallet.serialize() if self.wallet else None
        }

    
