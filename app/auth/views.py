from flask import render_template,redirect,url_for,flash,request
from app.models import User
from .forms import LoginForm
from .. import db
from flask_login import login_user, login_required, logout_user
from .. import auth

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    title = "Owner Login"
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data

        user = User.query.by(email = user.email).first
        if user is not None and user.verify_password(user_password):
            flash("You have successfully logged in... write your posts")
            return url_for('main.index')
        flash("Invalid username or password")
        

    return render_template("auth/login.html", form = form , title = title)

