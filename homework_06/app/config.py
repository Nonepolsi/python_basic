import os



SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg://user:example@localhost:5432/blog"
)
SQLALCHEMY_ECHO = False
SECRET_KEY = "38199ec4c6db988ae0c26e759737d70adf79332f27b1ecaae361df8b40842fbe"