# Criar as rotas do nosso site (os links).

from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required

@app.route("/")
def homepage():
  return render_template('index.html')

@app.route("/perfil")
@login_required
def usuario():
   return render_template('perfil.html')