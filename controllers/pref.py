from flask import *
from config import app
pref = Blueprint('pref', __name__, template_folder = 'views')
#Exclusions, Skills, Position-type (PM, software dev), Field (AI, Medicine, sports), Experience Level


@pref.route('/preferences', methods = ['GET'])
def pref_route_get():
    cur = app.mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    rv = cur.fetchall()
    print(str(rv))
    return render_template("preferences.html")

@pref.route('/preferences', methods = ['POST'])
def pref_route_post():
    if request.method == 'POST':
        #print request.form
        skills = request.form.getlist('skillz')
    
    
    return render_template("preferences.html")
