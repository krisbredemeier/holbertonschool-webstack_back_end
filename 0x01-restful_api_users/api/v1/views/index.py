#!/usr/bin/python3
from flask import Flask
from api.v1.views import app_views

app_views.strict_slashes = False

@app_views.route('/api/v1/status', methods='GET')
def test():
    return '{"status" : "OK"}'
