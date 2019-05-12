from app import db

class FeedModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(500), index=True, unique=True)
	body = db.Column(db.String(500), index=True)
	date = db.Column(db.DateTime)

class RegisterModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(500), index=True, unique=True)
	password = db.Column(db.String(500), index=True, unique=True)
