from dotenv import load_dotenv
from flask import Flask
import os

"""Any libraries that need to be globally accessible (database, auth, etc)"""
#db = SQLAlchemy()
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def create_app():
    """Initialize the core Flask app"""
    app = Flask(__name__)
    load_dotenv()

    #Initialize global plugins
    """db.init_app(app)"""

    #Register blueprints
    #app.register_blueprint(errors.bp)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    ### Handle logging when  ###
    if not app.debug and not app.testing:
        #todo: setup logging here
        pass

    return app