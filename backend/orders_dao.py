from datetime import datetime
import pytz


def get_all_orders(connection):
    with connection.cursor() as cursor:
        query = (
            "SELECT * FROM orders"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        response = []
        for record in result:
            response.append({
                "order_id": record[0],
                "customer_name": record[1],
                "total": record[3],
                "datetime": record[2]
            })
    return response


def insert_order(connection, o_details):
    with connection.cursor() as cursor:
        order_time = datetime.now()
        # insert order
        query = (
            "INSERT INTO orders (customer_name, total, datetime) "
            "VALUES (%s, %s, %s);"
        )
        order_data = (o_details["customer_name"], o_details["total"], order_time)
        cursor.execute(query, order_data)
        order_id = cursor.lastrowid

        # insert order details
        order_details_query = (
            "INSERT INTO order_details (order_id, product_id, quantity, total_price) "
            "VALUES (%s, %s, %s, %s);"
        )
        appendable_data = []
        for record in o_details["order_details"]:
            appendable_data.append([
                order_id,
                int(record["product_id"]),
                float(record["quantity"]),
                float(record["total_price"])
            ])
        cursor.executemany(order_details_query, appendable_data)
    connection.commit()
    return order_id


if __name__ == '__main__':
    from sql_connection import DatabaseConnection

    db = DatabaseConnection().connect()
    print(insert_order(db, {
        "customer_name": "Jonny Doe",
        "total": 350,
        "order_details": [
            {
                'product_id': 4,
                'quantity': 2,
                'total_price': 200
            },
            {
                'product_id': 8,
                'quantity': 5,
                'total_price': 150
            },
        ]
    }))
