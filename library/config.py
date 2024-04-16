import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")
SECRET_KEY = os.environ.get("KEY")
SQLALCHEMY_DATABASE = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")