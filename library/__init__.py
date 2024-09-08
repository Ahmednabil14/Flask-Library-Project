from flask import Flask
from .config import config_options
from .models import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
import os
from flask_wtf import CSRFProtect
from library.author import login_manager
from flask_restful import Api
from flask_wtf.csrf import *


def create_app(conf_option='prd'):
    app = Flask(__name__)
    current_conf = config_options[conf_option]
    app.config.from_object(current_conf)
    db.init_app(app)

    login_manager.init_app(app)

    migrate = Migrate(app, db)
    bootstrap = Bootstrap5(app)
    app.secret_key = os.urandom(32)
    csrf = CSRFProtect(app)

    api = Api(app, decorators=[csrf.exempt])

    from library.book import books_blueprint
    app.register_blueprint(books_blueprint)

    from library.author import authors_blueprint
    app.register_blueprint(authors_blueprint)

    from library.book.api.views import  BookList, HandelBook
    api.add_resource(BookList, '/api/books')
    api.add_resource(HandelBook, '/api/books/<int:book_id>')

    return app