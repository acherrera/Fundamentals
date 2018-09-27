"""
I don't know, just trying it out.
This is the framework for the SQL that will be used later
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique = True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# How to add data use this: 
"""
>>> from yourapplication import db
>>> db.create_all()
Boom, and there is your database. Now to create some users:

>>> from yourapplication import User
>>> admin = User(username='admin', email='admin@example.com')
>>> guest = User(username='guest', email='guest@example.com')
But they are not yet in the database, so let’s make sure they are:

>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.commit()
"""
