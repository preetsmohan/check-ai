from config import app

def pref_sql(query, parameters):
    connection = app.mysql.connection
    cursor = connection.cursor()
    cursor.execute(query.format(*parameters))
    print(query.format(*parameters))
    connection.commit()
    result = cursor.fetchall()
    return result

def get_skills():
    results = pref_sql("SELECT skills FROM user WHERE uid = '{0}'", (session['uid'],))
    skills = results[0][0].split(";")
    return skills;
