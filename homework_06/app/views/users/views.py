from http import HTTPStatus

from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect
)
from werkzeug.exceptions import (
    NotFound
)

from .users_form import UserForm
from .crud import users_storage as storage



users_app = Blueprint("users_app", __name__, url_prefix="/users")


@users_app.get("/", endpoint="list")
def get_users():
    return render_template(
        "users/list.html",
        users=storage.get()
    )


@users_app.route("/add/", endpoint="add", methods=["GET", "POST"])
def add_user():
    form = UserForm()
    if request.method == "GET":
        return render_template(
            "users/add.html",
            form=form
        )

    if not form.validate_on_submit():
        return (
            render_template(
                "users/add.html",
                form=form
            ),
            HTTPStatus.UNPROCESSABLE_ENTITY
        )

    user_name = form.name.data
    user_username = form.username.data
    user_email = form.email.data
    user = storage.create(
        name=user_name,
        username=user_username,
        email=user_email
    )
    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)


@users_app.get("/<int:user_id>/", endpoint="details")
def get_user(user_id: int):
    user = storage.get_by_id(user_id)
    if user is None:
        raise NotFound(f"User with id #{user_id} not found!")

    return render_template(
        "users/details.html",
        user=user
    )