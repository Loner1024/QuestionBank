from app import app, login
from flask import render_template, redirect
from flask_login import login_required

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
