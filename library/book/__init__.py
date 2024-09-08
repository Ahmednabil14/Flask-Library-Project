from flask import Blueprint

books_blueprint = Blueprint('books', __name__, url_prefix='/books')
from library.book import views