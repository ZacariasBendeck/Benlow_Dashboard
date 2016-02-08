from flask import Flask
from .template_filters import get_image_filter
from werkzeug import secure_filename
import json


UPLOAD_FOLDER = '/home/USERNAME/Dropbox/FOLDER_NAME'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.jinja_env.filters['get_image'] = get_image_filter
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views
from app import login_views
