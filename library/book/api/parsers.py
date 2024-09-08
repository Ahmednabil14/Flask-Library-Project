from flask_restful import reqparse


book_parser = reqparse.RequestParser()

book_parser.add_argument("title", required=False, type=str, help="Name is required")
book_parser.add_argument("description", required=False, type=str, help="description is required")
book_parser.add_argument("cover_image", required=False, type=str, help="image is required")
book_parser.add_argument("pages", required=False, type=int, help="number of is required")
book_parser.add_argument("author_id", required=False, type=int, help="Author ID is required")