from config import app

def pref_sql(query, parameters):
    connection = app.mysql.connection
    cursor = connection.cursor()
    cursor.execute(query.format(*parameters))
    print(query.format(*parameters))
    connection.commit()
    result = cursor.fetchall()
    return result
