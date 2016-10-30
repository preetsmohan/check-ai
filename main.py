from flask import Flask
from flask import render_template
import controllers
from config import app
from flask_mysqldb import MySQL
import os

app.secret_key = os.urandom(24)
app.register_blueprint(controllers.pref)
app.register_blueprint(controllers.login)

@app.route('/')
def hello_world():
    cur = app.mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    rv = cur.fetchall()
    cur.close()
    # return str(rv)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()


