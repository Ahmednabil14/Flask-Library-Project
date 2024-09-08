from wtforms import StringField, FileField, SubmitField, IntegerField
from flask_wtf import FlaskForm

class BookForm(FlaskForm):
    title = StringField('Title')
    description = StringField('Content')
    cover_image = FileField('Image')
    pages = IntegerField("Number Of Pages")
    submit = SubmitField("Add Book")