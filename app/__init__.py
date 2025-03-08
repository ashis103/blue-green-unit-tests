import os
from flask import Flask
from app.database import init_db

app = Flask(__name__)

if os.getenv('FLASK_ENV') != 'test':
    init_db()

# else:
#     app.config.from_object('app.config')

from app import routes


