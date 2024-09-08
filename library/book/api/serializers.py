from flask_restful import fields

author_serilizer ={
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
}


book_serializers = {
    "id": fields.Integer,
    "title":fields.String,
    "description":fields.String,
    "cover_image":fields.String,
    "pages":fields.Integer,
    "author_id":fields.Integer,
    "author" :fields.Nested(author_serilizer)
}