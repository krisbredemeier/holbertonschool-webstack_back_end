#!/usr/bin/python3
from flask import Flask
from flask import Blueprint
from flask import jsonify
from api.v1.views import app_views
import os
app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')
app.register_blueprint(app_views)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not found"), 404

def get_db():
    '''
    Opens a new database connection if there is none yet for the
    current application context.
    '''
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    '''
    Closes the database again at the end of the request.
    '''
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
