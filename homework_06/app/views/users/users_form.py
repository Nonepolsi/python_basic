from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    ValidationError,
)

from views.users.crud import users_storage


def validate_username(form, field):
    username = field.data
    if request.method == "POST" and users_storage.username_exists(username):
        raise ValidationError(
            f"Username {username!r} was already taken!",
        )
    

def validate_email(form, field):
    email = field.data
    if request.method == "POST" and users_storage.email_exists(email):
        raise ValidationError(
            f"User with the email {email!r} already exists!",
        )



class UserForm(FlaskForm):

    name = StringField(
        label="Real name",
        validators=[
            DataRequired()
        ],
    )

    username = StringField(
        label="Username",
        validators=[
            DataRequired(),
            validate_username,
        ],
    )
    
    email = StringField(
        label="E-mail",
        validators=[
            DataRequired(),
            Email(),
            validate_email
        ],
    )

    add = SubmitField(
        label="Create",
    )
