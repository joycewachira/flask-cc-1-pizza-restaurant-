from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', backref='restaurants')

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, price, restaurant_id, pizza_id):
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id

    @staticmethod
    def create(price, restaurant_id, pizza_id):
        try:
            restaurant_pizza = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id)
            db.session.add(restaurant_pizza)
            db.session.commit()
            return restaurant_pizza
        except IntegrityError:
            db.session.rollback()
            return None
