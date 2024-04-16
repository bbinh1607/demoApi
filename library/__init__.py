import os
from flask import Flask
from .books.controller import books
from .extension import db, ma
from .model import Books, Students, Author, Category, Borrow

def create_db(app):
    with app.app_context():
        db.create_all()
        print("Đã tạo cơ sở dữ liệu!")

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    
    # Lấy đường dẫn của thư mục cha
    current_dir = os.path.dirname(__file__)
    
    # Thiết lập đường dẫn tương đối cho cơ sở dữ liệu
    database_path = os.path.join(current_dir, 'library.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{database_path}"
    
    db.init_app(app)
    
    ma.init_app(app)
    # Kiểm tra và tạo cơ sở dữ liệu nếu chưa tồn tại
    if not os.path.exists(database_path):
        create_db(app)
    else:
        print("Cơ sở dữ liệu đã tồn tại!")

    app.register_blueprint(books)
    return app
