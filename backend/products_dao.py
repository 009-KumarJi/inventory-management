from sql_connection import DatabaseConnection


def get_all_products(connection):
    cursor = connection.cursor()
    query = (
        "SELECT products.id_products, products.p_name, uom.uom_name, products.price_per_unit "
        "FROM products "
        "inner join uom "
        "on uom.id_uom=products.um_id "
        "order by products.id_products asc; "
    )
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def get_product_by_id(connection, product_id):
    cursor = connection.cursor()
    query = (
        "SELECT products.id_products, products.p_name, uom.uom_name, products.price_per_unit "
        "FROM products "
        "inner join uom "
        "on uom.id_uom=products.um_id "
        "WHERE products.id_products = %s;"
    )
    cursor.execute(query, (product_id,))
    result = cursor.fetchall()
    cursor.close()
    return result


def insert_product(connection, product_name, um_id, price_per_unit):
    cursor = connection.cursor()
    query = (
        "INSERT INTO products (p_name, um_id, price_per_unit) "
        "VALUES (%s, %s, %s)"
    )
    cursor.execute(query, (product_name, um_id, price_per_unit))
    connection.commit()
    last_row_id = cursor.lastrowid
    cursor.close()
    return last_row_id


def _print_all_products(connection):
    products = get_all_products(connection)
    for product in products:
        print(product)


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = (
        "DELETE FROM products "
        "WHERE id_products = %s"
    )
    cursor.execute(query, (product_id,))
    connection.commit()
    cursor.close()


def update_product(connection, product_id, product_name, um_id, price_per_unit):
    cursor = connection.cursor()
    query = (
        'UPDATE products '
        'SET p_name = %s, um_id = %s, price_per_unit = %s '
        'WHERE id_products = %s'
    )
    cursor.execute(query, (product_name, um_id, price_per_unit, product_id))
    connection.commit()
    cursor.close()


if __name__ == '__main__':
    db = DatabaseConnection()
    cnx = db.connect()
    # all code below is for testing purposes

    db.disconnect()
