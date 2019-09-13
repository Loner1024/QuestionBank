from app import app, db
from app.forms import LoginForm, AnswerForm, RegisterForm
from app.model import User
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = AnswerForm()
    form.generate_form()
    if form.validate_on_submit():
        ans = str(dict(request.form))
        print(ans)
        print(type(ans))
        print('啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊')
        current_user.ans = str(dict(request.form))
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', title='Answer', form=form)


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
    return render_template('login.html', form=form, title='Login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        if form.username.data == '':
            flash('Username can not be empty')
        elif User.query.filter_by(username=form.username.data).first() != None:
            flash('Duplicate username')
        elif form.password.data == '':
            flash('Password can not be empty')
        elif form.repassword.data == '':
            flash('Enter your password again')
        elif form.password.data != form.repassword.data:
            flash('The password entered twice is different')
        elif form.qq.data == '':
            flash('Enter your qq number')
        else:
            user = User(username=form.username.data, password_hash=generate_password_hash(form.password.data), student_id=form.student_id.data, nation=form.nation.data, qq=form.qq.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/success')
@login_required
def success():
    return render_template('success.html', title='Success!')
