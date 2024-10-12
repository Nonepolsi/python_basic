from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from views.users import users_app
from views.posts import posts_app

import config
from models import db



app = Flask(__name__)

app.config.update(
    SECRET_KEY=config.SECRET_KEY,
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
csrf = CSRFProtect(app=app)



@app.get("/", endpoint="index")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(
        debug=False,
        host='0.0.0.0',
    )