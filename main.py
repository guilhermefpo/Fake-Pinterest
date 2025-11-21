from flask  import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template('index.html')

@app.route("/perfil")
def usuario():
   return render_template('perfil.html')


if __name__ == "__name__":
    app.run(debug=True)