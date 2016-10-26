from flask import *

pref = Blueprint('pref', __name__, template_folder = 'views')

@pref.route('/preferences')
def pref_route():
    return render_template("preferences.html")
