from flask import *
from config import app
pref = Blueprint('pref', __name__, template_folder = 'views')
#Exclusions, Skills, Position-type (PM, software dev), Field (AI, Medicine, sports), Experience Level
from mysql import *

@pref.route('/preferences', methods = ['GET'])
def pref_route_get():
    session['username'] = '1'
    get_pref(app, "SELECT skills, exclusions, postype, field, explevel FROM user WHERE uid = '{0}'", (session['username']))
    return render_template("preferences.html")

@pref.route('/preferences', methods = ['POST'])
def pref_route_post():
    if request.method == 'POST':
        #print request.form
        skills = request.form.getlist('skillz')
        exclusions = request.form.getlist('exclusions')
        postype = request.form.getlist('postype')
        fields = request.form.getlist('fields') 
    
    return render_template("preferences.html")
