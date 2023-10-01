from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask-RESTful API
api = Api(app)



# Initialize SQLAlchemy
db.init_app(app)
migrate = Migrate(app, db)

# Define the index route for rendering the HTML template
@app.route('/', methods=['GET'])
def index():
    restaurants = Restaurant.query.all()
    pizzas = Pizza.query.all()
    return render_template('index.html', restaurants=restaurants, pizzas=pizzas)

# Define your resources
class RestaurantListResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
            restaurant_list.append(restaurant_data)
        return jsonify(restaurant_list)

class RestaurantResource(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            restaurant_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": [{
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                } for pizza in restaurant.pizzas]
            }
            return jsonify(restaurant_data)
        return {"error": "Restaurant not found"}, 404

class PizzaListResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizza_list = []
        for pizza in pizzas:
            pizza_data = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            pizza_list.append(pizza_data)
        return jsonify(pizza_list)

class CreateRestaurantPizzaResource(Resource):
    def post(self):
        data = request.json
        price = data.get("price")
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")

        if not (price and pizza_id and restaurant_id):
            return {"errors": ["Missing required fields"]}, 400

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not (pizza and restaurant):
            return {"errors": ["Invalid pizza or restaurant"]}, 400

        price = int(price)
        if not (1 <= price <= 30):
            return {"errors": ["Price must be between 1 and 30"]}, 400

        restaurant_pizza = RestaurantPizza.create(price, restaurant_id, pizza_id)
        if restaurant_pizza:
            pizza_data = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            return jsonify(pizza_data)
        else:
            return {"errors": ["RestaurantPizza creation failed"]}, 500

# Add your resources to the API with their respective routes
api.add_resource(RestaurantListResource, '/restaurants')
api.add_resource(RestaurantResource, '/restaurants/<int:id>')
api.add_resource(PizzaListResource, '/pizzas')
api.add_resource(CreateRestaurantPizzaResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
