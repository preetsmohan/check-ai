def pref_sql(app, query, parameters):
    connection = app.mysql.connection
    cursor = connection.cursor()
    cursor.execute(query.format(*parameters))
    connection.commit()
    result = cursor.fetchall()
    return result
