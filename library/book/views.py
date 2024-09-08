from library.book import books_blueprint
from flask import render_template, redirect, url_for, request
from library.models import db, Book
from .form import BookForm
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

@books_blueprint.route("/", endpoint="home")
def home():
    books = Book.query.all()
    return render_template("book/home.html", books=books)

@books_blueprint.route("/Details/<int:id>", endpoint="book_details")
@login_required
def details(id):
    book = Book.query.get(id)
    return render_template("book/details.html", book=book)

@books_blueprint.route("/Delete/<int:id>", endpoint="delete")
@login_required
def delete(id):
    book = Book.query.get(id)
    if current_user == book.author:
        db.session.delete(book)
        db.session.commit()
    else:
        return "You don't have permission to delete this book"
    return redirect(url_for("books.home"))

@books_blueprint.route("/Create", endpoint="create", methods=["GET", "POST"])
@login_required
def create():
    form = BookForm()
    if form.validate_on_submit():
        cover_image = request.files["cover_image"]
        cover_image_name = secure_filename(cover_image.filename)
        cover_image.save(os.path.join("library/static/images/books", cover_image_name))     
        book = Book(title=request.form["title"], description=request.form["description"], 
                    cover_image=request.files["cover_image"].filename, author=current_user, pages=request.form["pages"])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("books.home"))
    return render_template("book/form.html", form=form)

@books_blueprint.route("/Edit/<int:id>", endpoint="update", methods=["GET", "POST"])
@login_required
def update(id):
    book = Book.query.get(id)
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit() and current_user == book.author:
            if request.form["title"]:
                book.title = request.form["title"]
            if request.form["description"]:
                book.description = request.form["description"]
            if request.form["pages"]:
                book.pages = request.form["pages"]
            if request.files["cover_image"]:
                cover_image = request.files["cover_image"]
                cover_image_name = secure_filename(cover_image.filename)
                cover_image.save(os.path.join("library/static/images/books", cover_image_name))
                book.cover_image = cover_image_name
        db.session.commit()
        return redirect(url_for("books.home"))
    if current_user == book.author:
        return render_template("book/form.html", form=form)
    else:
        return "You don't have permission to delete this book"
