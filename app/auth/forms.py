from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email
from app.models import User

class LoginForm(FlaskForm):
    email = StringField("Your Email Address", validators = [Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Sign In')

