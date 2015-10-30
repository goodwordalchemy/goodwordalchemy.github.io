from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from config import config

pages = FlatPages()
freezer = Freezer()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    freezer.init_app(app)
    pages.init_app(app)

    #register blueprints:
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app