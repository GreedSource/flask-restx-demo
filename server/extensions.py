from flask import Flask

from server.resources import register_routes


def routes_setup(app: Flask):
    register_routes(app)
