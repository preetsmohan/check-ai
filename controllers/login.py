from flask import *
from config import app
login = Blueprint('login', __name__, template_folder = 'views')
from mysql import ins_usr

@app.route('/signup', methods=['GET'])
def signup_get():
	return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
        print(request.form['full-name'])
        print(request.form['password'])
        print(request.form['confirm-password'])
        
        ins_usr(app, "INSERT INTO user (name, password) VALUES ('{0}', '{1}');", (request.form['full-name'],request.form['password']))
        
        return render_template('signup.html')
