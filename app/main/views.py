from flask import render_template, request,redirect, url_for,abort
from . import main
from flask_login import login_required,current_user
from app.models import User, Post, Comment
from .forms import addPost, addComment
from .. import db,photos

@main.route('/')
def index():
    '''
    View root page function that returns index page
    '''
    title = "my blog"

    posts = Post.query.all()
    return render_template('index.html', title = title, posts = posts)


@main.route('/posts/<post_id>' ,methods = ['GET', 'POST'])
def post(post_id):
    '''
    View post page function that displays the posts in detail
    '''
    post = Post.query.filter_by(id = post_id).first()

    form = addComment()
    if form.validate_on_submit():
        content = form.content.data
        new_comment= Comment(content=content, post_id = post.id)
        new_comment.save_comment()
        return redirect(url_for('main.post', post_id = post.id))

    comments = Comment.get_comments(post.id)    


    return render_template('post.html', post = post, form =form ,comments = comments)


@main.route('/user/<uname>/addpost', methods = ['GET', 'POST'])
@login_required
def add_post(uname):
    title = "add post"
    form = addPost()
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        if "post_photo" in request.files:
            pic = photos.save(request.files["post_photo"])
            path =f"photos/{pic}"
            image_url = path

        new_post = Post(title = title, content = content, user = user, image_url = image_url)
        new_post.save_post()

        return redirect(url_for('main.index'))

    return render_template('addpost.html', form = form, title = title )

