#Application Factory Method
from flask import Flask

def create_app(**config_overrides): #** allows unit tester to override
    app = Flask(__name__)
    
    app.config.from_pyfile('settings.py') #get application settings from file settings.py
    #Need to override this for unit testing
    app.config.update(config_overrides)
    
    #import views
    from home.views import home_app
    
    #import blueprints
    app.register_blueprint(home_app)
    
    
    return app