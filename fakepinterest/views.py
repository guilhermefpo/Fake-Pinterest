# Criar as rotas do nosso site (os links).

from flask import render_template, url_for
from fakepinterest import app

@app.route("/")
def homepage():
  return render_template('index.html')

@app.route("/perfil")
def usuario():
   return render_template('perfil.html')