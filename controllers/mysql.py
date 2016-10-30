def ins_usr(app, query, parameters):
    connection = app.mysql.connection
    cursor = connection.cursor()
    cursor.execute(query.format(parameters[0], parameters[1]))
    connection.commit()

def get_pref(app, query, parameters):
    connection = app.mysql.connection
    cursor = connection.cursor()
    cursor.execute(query.format(parameters[0]))
    return cursor.fetchall()

def update_pref(app, query, parameters):
    connection = app.mysql.connection
    cursor = connection.cursor()
    cursor.execute(query.format(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4]))
    return cursor.fetchall()
