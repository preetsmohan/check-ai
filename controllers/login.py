from flask import *
from config import app
login = Blueprint('login', __name__, template_folder = 'views')

@app.route('/signup', methods=['GET'])
def signup_get():
	return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
        print request.form['full-name']
        print request.form['password']
        print request.form['confirm-password']
        cur = app.mysql.connection.cursor()
        cur.execute("INSERT INTO user (name, password) VALUES ('{0}', '{1}');".format(request.form['full-name'],request.form['password']))
	app.mysql.connection.commit()
        
        return render_template('signup.html')
