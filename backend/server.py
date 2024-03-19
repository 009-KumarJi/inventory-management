import logging
from sql_connection import DatabaseConnection
from products_dao import ProductDAO
from flask import Flask, request, jsonify

db = DatabaseConnection().connect()
product_dao = ProductDAO(db)

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# '/' is the root or entry point of the website
@app.route('/getProducts')
def home():
    logging.info("Getting all products")
    result = product_dao.get_all_products()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*') # This is to allow the frontend to access the backend
    return response


if __name__ == '__main__':
    logging.info("Starting Flask app")
    app.run(port=5000)
