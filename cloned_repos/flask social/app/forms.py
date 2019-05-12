from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

#Fields for forms
class FeedForm(Form):
	text = TextAreaField('text', validators=[DataRequired()])

class RegisterForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])

class NewPasswordForm(Form):
	newPassword = StringField('password', validators=[DataRequired()])
