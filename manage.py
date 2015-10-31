import os
from datetime import datetime
from app import create_app, freezer
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def freeze(debug=False):
    if debug:
        freezer.run(debug=True)
    freezer.freeze()

@manager.command
def new_post(title):
    """
    creates a new file in 'pages' directory with 
    indicated title, formatted yaml header, and opens
    new file in sublime text editor
    """
    from config import basedir
    
    yaml_header = 'title: %s' % title + '\n' +\
                  'date: %s' % datetime.now() + '\n\n'
    
    dirname = title.replace(' ','_')
    dirpath = os.path.join(basedir, dirname)
    os.mkdir(dirpath)

    filename = dirname + '.md'
    filepath = os.path.join(dirpath, filename)
    with open(filepath, 'w') as thefile:
        thefile.write(yaml_header)

    os.system("subl %s" % filepath)



if __name__ == '__main__':
    manager.run()
