from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

"""Any libraries that need to be globally accessible (database, auth, etc)"""
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
db = SQLAlchemy()

def create_app():
    """Initialize the core Flask app"""
    app = Flask(__name__)
    load_dotenv()

    #Initialize global plugins
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQL_ALCHEMY_DATABASE_URI")
    db.init_app(app)


    #with app.app_context():
        #db.Model.metadata.reflect(db.engine)
        #db.create_all()

        #Register blueprints 
    register_blueprints(app)  
    register_plugins(app)
        #from app.main import bp as main_bp
        #app.register_blueprint(main_bp)

#        from app.errors import bp as errors_bp
#        app.register_blueprint(errors_bp)

        ### Handle logging when app is not in debug or testing modes ###
    if not app.debug and not app.testing:
        #todo: setup logging here
        pass

    return app

def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

def register_plugins(app):
    with app.app_context():
        db.Model.metadata.reflect(db.engine)
        db.create_all()