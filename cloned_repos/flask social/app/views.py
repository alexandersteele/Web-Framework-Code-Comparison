from flask import render_template, flash, request, session, redirect, url_for
from app import app, db
from .forms import FeedForm, RegisterForm, NewPasswordForm
from app.models import FeedModel, RegisterModel
from time import gmtime, strftime
import datetime

@app.route('/', methods=['GET', 'POST'])
def feed():
	if 'user' in session:
		session_user = session['user']
	else:
		session['user'] = "Guest"
		session_user = session['user']
	form = FeedForm()
	if form.validate_on_submit(): # Check for validation
		p = FeedModel(body=form.text.data, date=datetime.datetime.utcnow(), username=session_user)
		log(session_user + " posted on feed", "low")
		db.session.add(p) # Add to db
		db.session.commit() # Commit to db
		flash('Success') # Print message

	list_item = FeedModel.query.order_by(FeedModel.id.desc()) #store all incomplete tasks
	return render_template('feed.html', title='Connektion Feed', form=form, list_item=list_item, session_user=session_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	session_user = session['user']
	if form.validate_on_submit(): # Check for validation
		p = RegisterModel(username=form.username.data, password=form.password.data)

		checkUser = RegisterModel.query.filter_by(username = form.username.data).first() #Check user against users in db
		if checkUser is not None: #validate username entry
			flash('Username taken')
		else:
			log(form.username.data + " registered", "high")
			db.session.add(p) # Add to db
			db.session.commit() # Commit to db
			flash('Success') # Print message


	list_item = RegisterModel.query.all() #store all incomplete tasks
	return render_template('register.html', title='Connektion Registration', form=form, list_item=list_item, username=session_user, session_user=session['user'])

@app.route('/login', methods=['GET', 'POST'])
def userLogin():
	form = RegisterForm()
	if form.validate_on_submit(): # Check for validation
		p = RegisterModel(username=form.username.data, password=form.password.data)
		checkUser = RegisterModel.query.filter_by(username = form.username.data).first() #Check user against users in db
		if checkUser is not None: #validate username entry
			if checkUser.password == form.password.data:
				log(form.username.data + " logged in", "medium")
				session['user'] = form.username.data
				return redirect(url_for('feed'))
		flash('Incorrect username or password') # Print message

	return render_template('login.html', title='Connektion Log-In', form=form, session_user=session['user'])

@app.route('/logout')
def logout():
	session['user'] = "Guest"
	return redirect(url_for('feed'))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
	form = NewPasswordForm()
	if form.validate_on_submit(): # Check for validation
		RegisterModel.query.filter_by(username = session['user']).first().password = form.newPassword.data
		db.session.commit()
		flash('Password Changed')
		log(session['user'] + " changed their password", "medium")
	return render_template('settings.html', title='Settings', form=form, session_user=session['user'])

def log(data, severity):
	with open("log.txt", "ab") as fo:
		datelog = strftime("%d-%m-%Y   %H:%M:%S   ", gmtime())
		stringlog = datelog + data + " Severity: " + severity + "\n"
		fo.write(stringlog.encode('utf-8'))
