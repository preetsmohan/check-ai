from flask import *
from config import app
login = Blueprint('login', __name__, template_folder = 'views')
from mysql import pref_sql

@app.route('/signup', methods=['GET'])
def signup_get():
	return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
        print(request.form['full-name'])
        print(request.form['password'])
        print(request.form['confirm-password'])
        cur = app.mysql.connection.cursor()
        cur.execute("INSERT INTO user (name, password) VALUES ('{0}', '{1}');".format(request.form['full-name'],request.form['password']))
        app.mysql.connection.commit()
        
        return render_template('signup.html')

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    res = pref_sql("SELECT uid, password FROM user WHERE name = '{0}'", (request.form['username'],))
    print(res[0][1])
    if res:
        if(res[0][1] == request.form['password']):
            session['username'] = request.form['username']
            session['uid'] = res[0][0]
        else:
            return "error - wrong password"
    else:
        return "error - username not found"

    return render_template('login.html')
