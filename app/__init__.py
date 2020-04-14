from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

"""Any libraries that need to be globally accessible (database, auth, etc)"""
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def create_app():
    """Initialize the core Flask app"""
    app = Flask(__name__)
    load_dotenv()

    #Initialize global plugins
    """app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQL_ALCHEMY_DATABASE_URI")
    db = SQLAlchemy(app)
    db.Model.metadata.reflect(db.engine)
    """

    #Register blueprints    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    ### Handle logging when app is not in debug or testing modes ###
    if not app.debug and not app.testing:
        #todo: setup logging here
        pass

    return app