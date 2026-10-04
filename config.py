import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-change-me')
    DATABASE_URL = os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR / "careerhub.db"}')
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_TIME_LIMIT = None
    DEV_SHOW_RESET_LINK = os.getenv('DEV_SHOW_RESET_LINK', '1') == '1'
    JOBS_PER_PAGE = 20
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    UPLOAD_EXTENSIONS = {'pdf','doc','docx','jpg','jpeg','png','webp'}
