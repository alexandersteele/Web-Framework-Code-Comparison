#imports
from flask import Flask, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.secret_key = '231DFSGA34AWD3sdfs'
app.config.from_object('config')
db = SQLAlchemy(app)

Bootstrap(app)

from app import views, models
