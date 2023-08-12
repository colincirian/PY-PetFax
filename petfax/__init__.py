from flask import Flask
from . import pet
from . import facts

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "This is our index!"
    
    app.register_blueprint(facts.bp_facts)
    app.register_blueprint(pet.bp)
    
    return app