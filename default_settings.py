import os

from dotenv import load_dotenv

load_dotenv('.env')
SECRET_KEY = os.environ.get('SECRET_KEY')
