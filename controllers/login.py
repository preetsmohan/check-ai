from flask import *
from config import app
login = Blueprint('login', __name__, template_folder = 'views')
from mysql import pref_sql

@app.route('/signup', methods=['GET'])
def signup_get():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
        #print(request.form['username'])
        #print(request.form['password'])
        #print(request.form['confirm-password'])
        pref_sql("INSERT INTO user (username, password) VALUES ('{0}', '{1}');", (request.form['username'], request.form['password']))
        #cur = app.mysql.connection.cursor()
        #cur.execute("INSERT INTO user (username, password) VALUES ('{0}', '{1}');".format(request.form['username'],request.form['password']))
        #app.mysql.connection.commit()
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

def login_check(username, password):
    res = pref_sql("SELECT uid, password FROM user WHERE username = '{0}'", (username,))
    if res:
        print(res[0][1])
        print(password)
        if(res[0][1] == password):
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



