import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from application import create_app
app = create_app()
manager = Manager(app) #Manager controls the instance of the application with factory

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    
    #Cloud9 settings
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 80))
    
    #Local settings
    # host = '0,0,0,0',
    # port = 80
    )
)

if __name__ == "__main__":
    manager.run()