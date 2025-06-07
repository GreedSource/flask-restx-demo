from flask import Flask

# Assuming you have an 'api' instance here (e.g., Flask-RESTX Api)
from .extensions import routes_setup

# from .scheduler import init_scheduler


def create_app():
    app = Flask(__name__)

    # Initialize Flask-RESTX API
    routes_setup(app)

    # Initialize and start the scheduler, only if not already initialized
    # if not hasattr(app, "scheduler_initialized"):
    #     init_scheduler()  # Initialize scheduler
    #     app.scheduler_initialized = True

    return app
