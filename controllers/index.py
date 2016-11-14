from flask import *
from config import app
index = Blueprint('index', __name__, template_folder = 'views')
#Exclusions, Skills, Position-type (PM, software dev), Field (AI, Medicine, sports), Experience Level
from utils import *

@app.route('/')
def hello_world():
    logged_in = session.get('uid')
    return render_template('index.html', signedIn=logged_in)
