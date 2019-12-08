from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignInForm(FlaskForm):
    """Login form."""

    username_or_email = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])