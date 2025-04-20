#This is a package associated with the folder website. 
#  Stuff inside this file will run automatically 
# once the website folder has been imported.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #__name__ is name of file - Flask app will have same name
    app.config['SECRET_KEY'] = 'cheesetacotickler123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #register blueprints in initialzation
    from .views import views
    from .auth import auth
    #url_prefix - prefix that gets added in front of the route name thing
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app


