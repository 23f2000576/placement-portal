from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from app.extensions import db, jwt, mail

# Load environment variables
load_dotenv()


def create_app():

    app = Flask(__name__)

    # ------------------------
    # DATABASE CONFIG
    # ------------------------
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placement.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ------------------------
    # JWT CONFIG
    # ------------------------
    app.config["JWT_SECRET_KEY"] = "placement-secret"

    # ------------------------
    # MAIL CONFIG
    # ------------------------
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

    # ------------------------
    # ENABLE CORS
    # ------------------------
    CORS(app)

    # ------------------------
    # INIT EXTENSIONS
    # ------------------------
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    # ------------------------
    # REGISTER ROUTES
    # ------------------------
    from app.routes import register_routes
    register_routes(app)

    return app