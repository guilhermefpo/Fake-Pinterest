# Criar as rotas do nosso site (os links).

from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET","POST"])
def homepage():
  formlogin = FormLogin()
  return render_template('index.html', form=formlogin)

@app.route("/criarconta", methods=["GET","POST"])
def criarconta():
   formcriarconta = FormCriarConta()
   return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil")
@login_required
def usuario():
   return render_template('perfil.html')