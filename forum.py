# Inicializar o Flask
from flask import Flask, render_template

app = Flask(__name__)

# home
@app.route("/")
def homepage():
    return render_template("home.html")

# outra rota
@app.route("/outrarota")
def outrarota():
    return ""

# run
if __name__ == "__main__":
    app.run(debug=True)