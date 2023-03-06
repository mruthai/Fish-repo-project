from . import bp as auth_bp
from app.forms import RegisterForm, LoginForm
from app.blueprints.social.models import User
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)
            u = User(username=username, email=email, password_hash=password)
            user_match = User.query.filter_by(username=username).first()
            email_match = User.query.filter_by(email=email).first()
            if user_match or email_match:
                flash (f'User {username} already exists!', 'try again')
                return redirect(url_for('auth.register'))
            elif email_match:
                flash (f'Request to register {username}!', 'successful')
                return redirect(url_for('main.index'))
            else:
                u.hash_password(password)
                u.commit()
        return redirect(url_for('main.index'))
    return render_template('register.jinja', register=form, title='Register')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or Password was incorrect, try again')
            return redirect(url_for('auth.login'))
        flash (f'{form.username}, successful login')
        login_user(user_match, remember=form.remember.data)
        return redirect(url_for('social.user', username=current_user.username))
    return render_template('login.jinja', login=form, title='Login')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect('/')