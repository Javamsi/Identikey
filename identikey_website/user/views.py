from identikey_website import app
from flask import render_template, flash, redirect, url_for, request, session
from user.form import SignUpForm, LoginForm
from user.models import User
from identikey_website import db
from user.decorators import login_required
import bcrypt 
import os, sys
import socket

@app.route('/', methods=('GET', 'POST'))
def home():
	return render_template('index.html')

""""  
@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None
    
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)
        
    if form.validate_on_submit():
        users = User.query.filter_by(
            username=form.username.data,
            ).limit(1)
        if users.count():
            user = users[0] 
            if bcrypt.hashpw(form.password.data, user.password) == user.password:
                session['username'] = form.username.data
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('login_success'))
            else:
                error = "Incorrect username and password"
        else:
            error = "Incorrect username and password"
    return render_template('login.html', form=form, error=error)
  """
  
@app.route('/login', methods=('GET', 'POST'))
def login():
	form = LoginForm()
	error = None
	os.chdir('..')
	os.chdir('..')
	os.chdir('./identikey')
	os.chdir('./user')
        
	if request.method == 'GET' and request.args.get('next'):
		session['next'] = request.args.get('next', None)
		
	if form.validate_on_submit():
		for line in open(os.getcwd() + '/user.txt'):
			if 'Username: ' in line:
				if not (form.username.data == (line.split('Username: ', 1)[1]).strip()):
					return "Invalid Username"
			if 'Password: ' in line:
				if not (form.password.data == (line.split('Password: ', 1)[1]).strip()):
					return "Invalid Password"
		return "Congrats you are in"		
	return render_template('login.html', form=form, error=error)

    
@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        #hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            form.fullname.data,
            form.email.data,
            form.username.data,
            form.password.data
            )
        #db.session.add(user)
        #db.session.commit()
        
        # Create the necessary Identikey files on the system
        os.chdir('..')
        os.chdir('..')
        if not os.path.exists('./identikey'):
        	os.mkdir('identikey')
        else:
        	return "User has already been created for this machine"
        	
        os.chdir('./identikey')
        if not os.path.isfile('./user'):
        	os.mkdir('user')
        if not os.path.isfile('./friends'):
        	os.mkdir('friends')
        if not os.path.isfile('./posts'):
        	os.mkdir('posts')
        if not os.path.isfile('./photos'):
        	os.mkdir('photos')
        if not os.path.isfile('./videos'):
        	os.mkdir('videos')
        if not os.path.isfile('./notifications'):
        	os.mkdir('notifications')
        
		if  os.path.isfile("./user/user.txt"):
			return "User has already been created for this machine"
		else:
			file = open("./user/user.txt", 'w')
			file.write("Username: ")
			file.write(form.username.data)
			file.write("\n")
			file.write("Full Name: ")
			file.write(form.fullname.data)
			file.write("\n")
			file.write("Email: ")
			file.write(form.email.data)
			file.write("\n")
			file.write("Password: ")
			file.write(form.password.data)
			file.write("\n")
			file.close()
        
        return render_template('index.html')
    return render_template('signup.html', form=form)
    
@app.route('/success', methods=('GET', 'POST'))
def success():
    form = SignUpForm()
    user = User(
        form.fullname.data,
        form.email.data,
        form.username.data,
        form.password.data
        )
    db.session.add(user)
    db.session.commit()
    
    return render_template('index.html', form=form)
    
@app.route('/login_success')
@login_required
def login_success():
    return "Author logged in!"
    
	