from sql_connection import DatabaseConnection


class ProductDAO:
    def __init__(self, connection):
        self.connection = connection

    def get_all_products(self):
        with self.connection.cursor() as cursor:
            query = (
                "SELECT products.id_products, products.p_name, uom.uom_name, products.price_per_unit "
                "FROM products "
                "inner join uom "
                "on uom.id_uom=products.um_id "
                "order by products.id_products asc; "
            )
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def get_product_by_id(self, product_id):
        with self.connection.cursor() as cursor:
            query = (
                "SELECT products.id_products, products.p_name, uom.uom_name, products.price_per_unit "
                "FROM products "
                "inner join uom "
                "on uom.id_uom=products.um_id "
                "WHERE products.id_products = %s;"
            )
            cursor.execute(query, (product_id,))
            result = cursor.fetchall()
        return result

    def insert_product(self, product_name, um_id, price_per_unit):
        with self.connection.cursor() as cursor:
            query = (
                "INSERT INTO products (p_name, um_id, price_per_unit) "
                "VALUES (%s, %s, %s)"
            )
            cursor.execute(query, (product_name, um_id, price_per_unit))
            self.connection.commit()
            last_row_id = cursor.lastrowid
        return last_row_id

    def delete_product(self, product_id):
        with self.connection.cursor() as cursor:
            query = (
                "DELETE FROM products "
                "WHERE id_products = %s"
            )
            cursor.execute(query, (product_id,))
            self.connection.commit()

    def update_product(self, product_id, product_name, um_id, price_per_unit):
        with self.connection.cursor() as cursor:
            query = (
                'UPDATE products '
                'SET p_name = %s, um_id = %s, price_per_unit = %s '
                'WHERE id_products = %s'
            )
            cursor.execute(query, (product_name, um_id, price_per_unit, product_id))
            self.connection.commit()


if __name__ == '__main__':
    db = DatabaseConnection()
    cnx = db.connect()

    product_dao = ProductDAO(cnx)
    # Use product_dao for product operations

    db.disconnect()
