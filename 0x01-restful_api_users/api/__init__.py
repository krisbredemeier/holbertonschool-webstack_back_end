#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint(__name__)

from api.v1.views.index import *

app_views.register_blueprint(url_prefix='/api/v1')
