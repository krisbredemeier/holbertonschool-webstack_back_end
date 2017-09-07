#!/usr/bin/python3
from flask import Flask
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def test():
    return '{"status" : "OK"}'
