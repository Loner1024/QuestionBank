from app import app
from app.forms import LoginForm, AnswerForm
from app.model import User
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user


@app.route('/')
@app.route('/index', methods=['GET', "POST"])
@login_required
def index():
    # form = AnswerForm()
    #if form.validate_on_submit():

    return render_template('index.html')
    #return render_template('index.html', form=form)


@app.route('/login', methods=['GET', "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user == None:
            flash('User does not exist')
        elif not user.check_password(password=form.password.data):
            flash('Wrong password')
        elif user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    # return render_template('login.html', title='Sign In', form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
