# Inicializar o Flask
from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

# Login
# modifiquei user_id=user_id. deixar assim até poder vincular ao banco de dados
@app.route("/forum/<user_id>", methods=["GET", "POST"])
def forum(user_id):
    return render_template("forum.html", user_id=user_id)

# Run
if __name__ == "__main__":
    app.run(debug=True)