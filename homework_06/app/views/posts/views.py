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

from .posts_form import PostForm
from .crud import posts_storage as storage
from views.users.crud import users_storage



posts_app = Blueprint("posts_app", __name__, url_prefix="/posts")


@posts_app.get("/", endpoint="list")
def get_posts():
    return render_template(
        "posts/list.html",
        posts=storage.get()
    )


@posts_app.route("/add/", endpoint="add", methods=["GET", "POST"])
def add_post():
    form = PostForm()
    if request.method == "GET":
        return render_template(
            "posts/add.html",
            form=form
        )

    if not form.validate_on_submit():
        return (
            render_template(
                "posts/add.html",
                form=form
            ),
            HTTPStatus.UNPROCESSABLE_ENTITY
        )

    post_title = form.title.data
    post_body = form.body.data
    post_user_id = form.user_id.data
    post = storage.create(
        title=post_title,
        body=post_body,
        user_id=post_user_id
    )
    url = url_for("posts_app.details", post_id=post.id)
    return redirect(url)


@posts_app.get("/<int:post_id>/", endpoint="details")
def get_post(post_id: int):
    post = storage.get_by_id(post_id)
    if post is None:
        raise NotFound(f"Post with id #{post_id} not found!")
    
    user = users_storage.get_by_id(post.user_id)

    return render_template(
        "posts/details.html",
        post=post,
        user=user
    )