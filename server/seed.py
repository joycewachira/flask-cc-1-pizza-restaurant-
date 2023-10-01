from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Create some restaurants
    dominion_pizza = Restaurant.query.filter_by(name="Dominion Pizza").first()
    if not dominion_pizza:
        dominion_pizza = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")

    pizza_hut = Restaurant.query.filter_by(name="Pizza Hut").first()
    if not pizza_hut:
        pizza_hut = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")
    italian_delight = Restaurant(name="Italian Delight", address="123 Main Street, Downtown")
    pizza_king = Restaurant(name="Pizza King", address="456 Elm Street, Suburbia")

    # Create some pizzas
    cheese_pizza = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni_pizza = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    veggie_pizza = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Mixed Vegetables")
    chicken_pizza = Pizza(name="Chicken BBQ", ingredients="Dough, BBQ Sauce, Cheese, Grilled Chicken")

    # Add the restaurants and pizzas to the database
    db.session.add(dominion_pizza)
    db.session.add(pizza_hut)
    db.session.add(italian_delight)
    db.session.add(pizza_king)
    db.session.add(cheese_pizza)
    db.session.add(pepperoni_pizza)
    db.session.add(veggie_pizza)
    db.session.add(chicken_pizza)
    db.session.commit()

    # Create some RestaurantPizza instances
    dominion_cheese_pizza = RestaurantPizza.create(price=12, restaurant_id=dominion_pizza.id, pizza_id=cheese_pizza.id)
    dominion_pepperoni_pizza = RestaurantPizza.create(price=14, restaurant_id=dominion_pizza.id, pizza_id=pepperoni_pizza.id)
    pizza_hut_cheese_pizza = RestaurantPizza.create(price=10, restaurant_id=pizza_hut.id, pizza_id=cheese_pizza.id)
    pizza_hut_pepperoni_pizza = RestaurantPizza.create(price=12, restaurant_id=pizza_hut.id, pizza_id=pepperoni_pizza.id)
    italian_delight_cheese_pizza = RestaurantPizza.create(price=11, restaurant_id=italian_delight.id, pizza_id=cheese_pizza.id)
    italian_delight_veggie_pizza = RestaurantPizza.create(price=15, restaurant_id=italian_delight.id, pizza_id=veggie_pizza.id)
    pizza_king_chicken_pizza = RestaurantPizza.create(price=16, restaurant_id=pizza_king.id, pizza_id=chicken_pizza.id)

if __name__ == '__main__':
    with app.app_context():
        seed_data()
