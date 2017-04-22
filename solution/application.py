#Application Factory Method
from flask import Flask

def create_app(**config_overrides): #** allows unit tester to override
    app = Flask(__name__)
    
    
    #Need to override this for unit testing
    app.config.update(config_overrides)
    
    #import views
    from home.views import home_app
    from rba.views import rba_app
    
    #import blueprints
    app.register_blueprint(home_app)
    app.register_blueprint(rba_app)
    
    return app