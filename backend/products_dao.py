from sql_connection import DatabaseConnection


class ProductDAO:
    def __init__(self, connection):
        self.connection = connection

    def get_all_products(self):
        with self.connection.cursor() as cursor:
            query = (
                "SELECT products.product_id, products.name, uom.uom_name, "
                "products.price_per_unit "
                "FROM products "
                "inner join uom "
                "on uom.uom_id=products.uom_id "
                "order by products.product_id asc; "
            )
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def get_product_by_id(self, product_id):
        with self.connection.cursor() as cursor:
            query = (
                "SELECT products.product_id, products.name, uom.uom_name, products.price_per_unit "
                "FROM products "
                "inner join uom "
                "on uom.uom_id=products.uom_id "
                "WHERE products.product_id = %s;"
            )
            cursor.execute(query, (product_id,))
            result = cursor.fetchall()
        return result

    def insert_product(self, product):
        with self.connection.cursor() as cursor:
            query = (
                "INSERT INTO products (name, uom_id, price_per_unit) "
                "VALUES (%s, %s, %s)"
            )
            cursor.execute(query, (product["product_name"], product["uom_id"], product["price_per_unit"]))
            self.connection.commit()
            last_row_id = cursor.lastrowid
        return last_row_id

    def delete_product(self, product_id):
        with self.connection.cursor() as cursor:
            query = (
                "DELETE FROM products "
                "WHERE product_id = %s"
            )
            cursor.execute(query, (product_id,))
            self.connection.commit()

    def update_product(self, product_id, product_name, uom_id, price_per_unit):
        with self.connection.cursor() as cursor:
            query = (
                'UPDATE products '
                'SET name = %s, uom_id = %s, price_per_unit = %s '
                'WHERE product_id = %s'
            )
            cursor.execute(query, (product_name, uom_id, price_per_unit, product_id))
            self.connection.commit()


if __name__ == '__main__':
    db = DatabaseConnection()
    cnx = db.connect()

    product_dao = ProductDAO(cnx)
    # Use product_dao for product operations
    # print(product_dao.get_all_products())

    db.disconnect()
