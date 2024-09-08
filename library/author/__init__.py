from flask import Blueprint
import flask_login
from library.models import Author

login_manager = flask_login.LoginManager()
login_manager.login_view = "author.login"

@login_manager.user_loader
def load_user(author_id):
    """Load user by ID."""
    return Author.query.get(author_id)
    
authors_blueprint = Blueprint('author', __name__, url_prefix='/author')
from library.author import views