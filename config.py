from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder = 'views')
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lightning'
app.config['MYSQL_DB'] = 'checkai'
app.mysql = MySQL(app)
app.config['DEBUG'] = True

