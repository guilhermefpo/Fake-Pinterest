# Criar as rotas do nosso site (os links).

from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from flask_login import login_required, login_user
from fakepinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET","POST"])
def homepage():
  formlogin = FormLogin()
  return render_template('index.html', form=formlogin)

@app.route("/criarconta", methods=["GET","POST"])
def criarconta():
   formcriarconta = FormCriarConta()
   if formcriarconta.validate_on_submit():
      senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
      usuario = Usuario(username=formcriarconta.username.data, email=formcriarconta.email.data, senha=senha)

      database.session.add(usuario)
      database.session.commit()
      login_user(usuario, remember=True)
      return redirect("perfil", usuario=usuario.username)
   return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil")
@login_required
def usuario():
   return render_template('perfil.html')