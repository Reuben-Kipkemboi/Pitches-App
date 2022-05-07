from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server) # launc the server to run application
if __name__ == '__main__':
    manager.run()
