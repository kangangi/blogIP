from flask import render_template, request,redirect, url_for,abort
from . import main
from flask_login import login_required,current_user
from app.models import User, Post, Comment
from .. import db

@main.route('/')
def index():
    '''
    View root page function that returns index page
    '''
    title = "my blog"
    return render_template('index.html', title = title)
