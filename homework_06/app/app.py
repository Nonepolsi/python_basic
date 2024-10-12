from flask import (
    Flask,
    render_template,
)
from flask_migrate import Migrate

import config

from models import db
from views.users import users_app
from views.posts import posts_app


app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)

app.register_blueprint(
    users_app
)

app.register_blueprint(
    posts_app
)

db.init_app(app)
migrate = Migrate(app, db)



@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
