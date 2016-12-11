from flask import *
from config import app
about = Blueprint('about', __name__, template_folder = 'views')
from utils import *

@about.route('/about')
def about_show():
    return render_template('about.html')
