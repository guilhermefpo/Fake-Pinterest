# Criar as rotas do nosso site (os links).

from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET","POST"])
def homepage():
  formlogin = FormLogin()
  if form_login.validate_on_submit():
     usuario = Usuario.query.filter_by(email=form_login.email.data).first()
     if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
        login_user(usuario)
        return redirect("perfil", usuario=usuario.username)
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
      return redirect("perfil", id_usuario=usuario.id)
   return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario):
    if int(id_usuario) ==  int(current_user.id):
         # O usuário ta vendo o perfil dele.
         return render_template("perfil.html", usuario=current_user)
    else:
      usuario = Usuario.query.get(int(id_usuario))
      return render_template('perfil.html', usuario=usuario)


@app.route("/logout")
@login_required
def logout():
   logout_user()
   return redirect(url_for("homepage"))