import pytest
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Pizza Finder' in response.data

def test_get_restaurants_route(client):
    restaurant = Restaurant(name="Test Restaurant", address="123 Test St")
    db.session.add(restaurant)
    db.session.commit()

    response = client.get('/restaurants')
    assert response.status_code == 200
    assert b'Test Restaurant' in response.data

def test_get_nonexistent_restaurant(client):
    response = client.get('/restaurants/1')
    assert response.status_code == 404
    assert b'Restaurant not found' in response.data

 