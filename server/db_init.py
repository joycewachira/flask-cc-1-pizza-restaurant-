from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Restaurant, Pizza, RestaurantPizza


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
db = SQLAlchemy(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
