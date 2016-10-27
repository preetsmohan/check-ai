from flask import *
from config import app
pref = Blueprint('pref', __name__, template_folder = 'views')

@pref.route('/preferences')
def pref_route():
    cur = app.mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    rv = cur.fetchall()
    print(str(rv))
    return render_template("preferences.html")
