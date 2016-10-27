from flask import Flask
import re
import os
import sys
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	
 	return 'Hello, World!'