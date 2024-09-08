from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Book(db.Model):
    """post model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    cover_image = db.Column(db.String, nullable=True)
    pages = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)


class Author(db.Model, UserMixin):
    """user model"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

