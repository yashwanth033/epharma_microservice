# services/users/project/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# instantiate the extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config for the app
    # App settings and FLASK_ENV can be seen in docker-compose files 
    # respective to the type of testing (dev or prod)  
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)


    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    
    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # shell context for flask cli
    # This is used to register the app and db to the shell. 
    # Now we can work with the application context and the database without 
    # having to import them directly into the shell, which you’ll see shortly.
    
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
