from .db import db

class User(db.Model):
    __table__name = 'User_Details'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Integer,unique = True ,nullable = False)
    email = db.Column(db.String(50),unique=True,nullable = False)
