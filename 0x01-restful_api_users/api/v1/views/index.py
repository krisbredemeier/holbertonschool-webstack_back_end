#!/usr/bin/python3
from flask import Flask
from app.v1.views import app_views

app_views.url_map.strict_slashes = False

@app_views.route('/api/v1/status', methods='GET')
def test():
    return '{"status" : "OK"}'
