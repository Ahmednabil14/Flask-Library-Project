from flask_restful import Resource, marshal_with
from library.models import Book
from library.book.api.serializers import *
from library.book.api.parsers import *
from library.models import db

class BookList(Resource):
    @marshal_with(book_serializers)
    def get(self):
        books = Book.query.all()
        return books

    @marshal_with(book_serializers)
    def post(self):
        book_args = book_parser.parse_args()
        book = Book(**book_args)
        db.session.add(book)
        db.session.commit()
        return book, 201
    

class HandelBook(Resource):
    @marshal_with(book_serializers)
    def get(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return {'message': 'Book not found'}, 404
        return book
    
    @marshal_with(book_serializers)
    def put(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return {'message': 'Book not found'}, 404
        book_args = book_parser.parse_args()
        for key, value in book_args.items():
            if value:
                setattr(book, key, value)
        db.session.commit()
        return book
        
    @marshal_with(book_serializers)
    def delete(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return {'message': 'Book not found'}, 404
        db.session.delete(book)
        db.session.commit()
        return Book.query.all()
