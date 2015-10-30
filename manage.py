import os
from app import create_app, freezer
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def freeze():
    freezer.run(debug=True)
    freezer.freeze()

if __name__ == '__main__':
    manager.run()
