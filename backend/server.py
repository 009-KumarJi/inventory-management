import json
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
    # print("Getting all products")
    result = product_dao.get_all_products()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')  # This is to allow the frontend to access the backend
    return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
    from uom_dao import get_uoms
    result = get_uoms(db)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    # This is to convert the JSON string to a Python dictionary
    request_payload = json.loads(request.form['data'])
    inserted_product_id = product_dao.insert_product(request_payload)
    response = jsonify({"product_id": inserted_product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    product_dao.delete_product(request.form['product_id'])
    response = jsonify({"status": "success"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    from orders_dao import insert_order
    order_id = insert_order(db, json.loads(request.form['data']))
    response = jsonify({"order_id": order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    logging.info("Starting Flask app")
    app.run(port=5000)
