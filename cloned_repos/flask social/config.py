import os

#CSRF Vulnerability protection
WTF_CSRF_ENABLED = True
SECRET_KEY = 'DFGdss12fgsxcv97'

basedir = os.path.abspath(os.path.dirname(__file__))

#sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
