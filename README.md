# flask-wk1-cc


This is a web application that allows users to discover and explore various pizza restaurants and their menu items. This project is built using Flask, a Python web framework, and SQLAlchemy for database management.

## Features

- View a list of pizza restaurants with their names and addresses.
- View a list of available pizza menu items, including their names and ingredients.
- Retrieve detailed information about a specific restaurant and its menu.
- Create new pizza menu items for restaurants.
- Delete a restaurant and its associated menu items.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x: This project is written in Python, so make sure you have a compatible Python version installed.
- Flask: You'll need to install Flask, a Python web framework. You can do this using pip:

    
    pip install Flask
    

- SQLAlchemy: This project uses SQLAlchemy to manage the database. You can install it with pip:

    
    pip install SQLAlchemy
    

## Installation

1. Clone the repository to your local machine:

    
    git clone https://github.com/joycewachira/flask-cc-1-pizza-restaurant-
    

2. Change into the project directory:

    
    cd code-challenge
    

3. Create a virtual environment (optional but recommended):

    
    python -m venv venv


4. Activate the virtual environment:

    - On Windows:


    venv\Scripts\activate


    - On macOS and Linux:


    source venv/bin/activate


5. Install project dependencies:

    
    pip install -r requirements.txt
    

6. Create the SQLite database and seed it with sample data:


    python3 server/seed.py
    

## Usage

1. Start the Flask development server:


    python3  server/app.py


2. Open a web browser and navigate to `http://localhost:5555/` to access the Pizza Finder application.

3. You can now browse the list of restaurants, view their menus, and create/delete menu items.

## API Endpoints

The following API endpoints are available:

- `GET /restaurants`: Get a list of all restaurants.
- `GET /restaurants/<int:id>`: Get details about a specific restaurant.
- `DELETE /restaurants/<int:id>`: Delete a restaurant and its menu items.
- `GET /pizzas`: Get a list of all pizza menu items.
- `POST /restaurant_pizzas`: Create a new pizza menu item.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, please feel free to contact me through github.

Happy Pizza Finding!
