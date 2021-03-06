from flask import *
from config import app
login = Blueprint('login', __name__, template_folder = 'views')
from utils import *
import hashlib

@app.route('/signup', methods=['GET'])
def signup_get():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
        salt = 'dabbingsux'
        hashed_pwd = hashlib.md5((request.form['password'] + salt).encode())
        pref_sql("INSERT INTO user (username, password, email) VALUES ('{0}', '{1}', '{2}');", (request.form['username'], hashed_pwd.hexdigest(), request.form['email']))
        success = login_check(request.form['username'], request.form['password'])
        if success:
            return redirect('/preferences')
        else:
            return render_template('signup.html')

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    success = login_check(request.form['username'], request.form['password'])
    if success:
        return redirect('/preferences')
    else:
        return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout_post():
    session.clear()
    return redirect('/')

def login_check(username, password):
    res = pref_sql("SELECT uid, password FROM user WHERE username = '{0}'", (username,))
    if res:
        hashed_pwd = hashlib.md5((password + 'dabbingsux').encode())
        if(res[0][1] == hashed_pwd.hexdigest()):
            session['username'] = request.form['username']
            session['uid'] = res[0][0]
            session['signedIn'] = True
        else:
            #bad password
            print("Bad password")
            return False
    else:
        #bad username
        print("Bad username")
        return False

    return True



