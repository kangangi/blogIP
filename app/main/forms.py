from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import Required

class addPost(FlaskForm):
    title = StringField("Post Title", validators = [Required()])
    content = TextAreaField("Your Post",validators=[Required()])
    submit = SubmitField("Add Post")

    