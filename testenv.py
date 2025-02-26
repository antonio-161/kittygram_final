import os

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(','))

print(os.getenv('SECRET_KEY', get_random_secret_key()))

print(os.getenv('DEBUG', 'False')) == 'True'
