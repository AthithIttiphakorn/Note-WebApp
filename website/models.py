#store database models
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin): #define column and row of db
    #define column named id (access as user.id ) that will store int that are unique (primary_key=True)
    id = db.Column(db.Integer, primary_key = True)
    #define column named email that will contain str with max 150 char. all str will be unique.
    email = db.Column(db.String(150), unique=True)