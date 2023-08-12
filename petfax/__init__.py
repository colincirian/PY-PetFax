from flask import Flask
from . import pet
from . import facts
from . import models


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "This is our index!"
    
    app.register_blueprint(facts.bp_facts)
    app.register_blueprint(pet.bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql: //username:password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    return app