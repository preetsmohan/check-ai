from flask import Flask
from flask import render_template
import controllers
from config import app
from flask_mysqldb import MySQL
import os

app.secret_key = os.urandom(24)
app.register_blueprint(controllers.pref)
app.register_blueprint(controllers.login)
app.register_blueprint(controllers.jobs)
app.register_blueprint(controllers.index)


if __name__ == "__main__":
    app.run()

