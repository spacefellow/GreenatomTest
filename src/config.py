import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.dbenv'))
DB_DRIVER = os.environ.get('POSTGRES_DRIVER')
DB_CONNECTOR = os.environ.get('POSTGRES_CONNECTOR')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')
DB_NAME = os.environ.get('POSTGRES_NAME')

load_dotenv(find_dotenv('.dev_env'))
SECRET_KEY = os.environ.get('SECRET_KEY')