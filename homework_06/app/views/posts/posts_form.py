from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import (
    DataRequired,
    NumberRange,
    ValidationError
)

from views.posts.crud import posts_storage
from views.users.crud import users_storage


def validate_title(form, field):
    title = field.data
    if request.method == "POST" and posts_storage.title_exists(title):
        raise ValidationError(
            f"Post with the title {title!r} already exists!"
        )
    

def validate_user_id(form, field):
    user_id = field.data
    if request.method == "POST" and not users_storage.get_by_id(user_id):
        raise ValidationError(
            f"User with the id {user_id} doesn't exist!"
        )



class PostForm(FlaskForm):

    title = StringField(
        label="Title",
        validators=[
            DataRequired(),
            validate_title
        ]
    )

    body = StringField(
        label="Body",
        validators=[
            DataRequired()
        ]
    )

    user_id = IntegerField(
        label="Author ID",
        validators=[
            DataRequired(),
            NumberRange(min=1),
            validate_user_id
        ]
    )

    add = SubmitField(
        label="Create"
    )
