def ins_usr(app, query, parameters):
    connection = app.mysql.connection
    cursor = connection.cursor()
    cursor.execute(query.format(parameters[0], parameters[1]))
    connection.commit()
