from library.author import authors_blueprint
from flask import render_template, request, redirect, url_for, flash
from .register_form import RegisterForm
from library.author.login_form import LoginForm
from library.models import Author, db
from flask_login import login_user, logout_user, current_user, login_required
import os
from werkzeug.utils import secure_filename


@authors_blueprint.route("/<int:id>", endpoint="books")
@login_required
def books(id):
    author_books = current_user.books
    return render_template("author/author_books.html", author_books=author_books)

@authors_blueprint.route("/register",endpoint="register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = dict(request.form)
        del data['csrf_token']
        del data['submit']
        author = Author(**data)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for("author.login"))        
    return render_template("author/register.html", form=form)

@authors_blueprint.route("/login", endpoint="login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        author = Author.query.filter_by(email=request.form["email"]).first()
        if author and author.password == request.form["password"]:
            login_user(author)
            return redirect(url_for("books.home"))
        else:
            flash("Invalid email or password")  
    return render_template("author/login.html", form=form)

@authors_blueprint.route("/logout", endpoint="logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("books.home"))
