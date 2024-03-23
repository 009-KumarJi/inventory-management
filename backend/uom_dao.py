
def get_uoms(connection):
    with connection.cursor() as cursor:
        query = (
            "SELECT * FROM uom;"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        response = []
        for (uom_id, uom_name) in result:
            response.append({
                "uom_id": uom_id,
                "uom_name": uom_name,
            })
    return response