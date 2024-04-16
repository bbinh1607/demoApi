from library.extension import db
from library.library_ma import BookSchema
from library.model import Books
from flask import request, jsonify
import json

book_schema = BookSchema()
books_schema = BookSchema(many=True)


def add_book_service():
    data =  request.json
    if (data and ('name' in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data)):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']
    
        try:
            new_book = Books(name=name, page_count=page_count, author_id=author_id, category_id=category_id)
            db.session.add(new_book)
            db.session.commit()
            return "Book added successfully!"
        except Exception as e:
            db.session.rollback()
            return "Can not add book"
    else:
        return "Request error"


def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return "Not Found book"
    

def get_all_books_sercice():
    books = Books.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return "Not Found book"
    
    
def update_book_by_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data and "page_count" in data:
            try:
                book.page_count = data["page_count"]
                db.session.commit()
                return "book updated"
            except Exception as e:
                db.session.rollback()
                return "Can not uptade book"
    else:
        return "Not Found book"
    
    
def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "book deleted successfully"
        except Exception as e:
            db.session.rollback()
            return "Can not delete book"
    else:
        return "Not Found book"