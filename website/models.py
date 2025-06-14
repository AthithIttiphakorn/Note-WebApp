#store database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #Foreign Key: Column in database that links to other column in another database to establish a relationship between them. eg. users and their notes
            #reference id column from user class
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #.id is the unique identifier for a specific record in the database. (DB ONLY!)

class User(db.Model, UserMixin): #define column and row of db
    #define column named id (access as user.id ) that will store int that are unique (primary_key=True)
    id = db.Column(db.Integer, primary_key = True)
    #define column named email that will contain str with max 150 char. all str will be unique.
    email = db.Column(db.String(150), unique=True)
    #define 1-many relationship with the other class (db model)
    notes = db.relationship('Note')

    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))