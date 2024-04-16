from flask import Blueprint
from .services import (add_book_service , get_book_by_id_service, get_all_books_sercice,
                       update_book_by_id_service, delete_book_by_id_service,)
books = Blueprint("books",__name__)



@books.route("/book-management/book" ,methods = ['POST'])
def add_book():
    return add_book_service()

@books.route("/book-management/book/<int:id>",methods = ['GET'])
def get_book_by_id(id):
    return get_book_by_id_service(id)

@books.route("/book-management/books",methods = ['GET'])
def get_all_books():
    return get_all_books_sercice()

@books.route("/book-management/book/<int:id>",methods = ['PUT'])
def update_book_by_id(id):
    return update_book_by_id_service(id)

@books.route("/book-management/book/<int:id>",methods = ['DELETE'])
def delete_book_by_id(id):
    return delete_book_by_id_service(id)