"""
The flask application package.
"""

from flask import Flask


app = Flask(__name__)

import mcel.views
from peewee import Database
from mcel.models import db

db = Database(app)







