# Criar site.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    os.getenv("DATABASE_URL") or "sqlite:///comunidade.db"
)
app.config["SECRET_KEY"] = "3ed06923cf5209673645"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Configuração correta do LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "homepage"  # ou a rota de login que você quiser

from fakepinterest import views
