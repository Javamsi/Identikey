from identikey_website import app
from flask import render_template, redirect, url_for, request
from user.form import SignUpForm
import os

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
	os.system('python server.py &')
	os.system('python client.py &')
	return render_template('index.html')
    