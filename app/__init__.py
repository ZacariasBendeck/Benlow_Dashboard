from flask import Flask
import json




app = Flask(__name__)

from app import views
from app import login_views