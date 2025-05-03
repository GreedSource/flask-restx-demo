from flask import Flask

# Assuming you have an 'api' instance here (e.g., Flask-RESTX Api)
from .extensions import api
from .resources import register_routes  # Assuming this sets up your API routes
from .scheduler import init_scheduler


def create_app():
    app = Flask(__name__)

    # Initialize Flask-RESTX API
    api.init_app(app)  # Initialize API with Flask app

    # Register routes for the API
    register_routes(api)

    # Initialize and start the scheduler
    init_scheduler()  # Initialize scheduler

    return app
