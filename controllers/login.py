from flask import *
from config import app
login = Blueprint('login', __name__, template_folder = 'views')

@app.route('/signup')
def signup():
	return render_template('signup.html')
