from sql_connection import DatabaseConnection


def get_all_products(cnx):
    cursor = cnx.cursor()
    query = (
        "SELECT products.id_products, products.p_name, uom.uom_name, products.price_per_unit "
        "FROM products "
        "inner join uom "
        "on uom.id_uom=products.um_id; "
    )
    #query = (
     #   "SELECT * FROM products;"
    #)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


if __name__ == '__main__':
    db = DatabaseConnection()
    cnx = db.connect()
    products = get_all_products(cnx)
    for product_id, product_name, uom_name, price in products:
        print(f"{product_id}: {product_name} ({uom_name}) - ₹{price}")
    db.disconnect()
