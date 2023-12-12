# Inicializar o Flask
from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

# Login
@app.route("/forum")
def forum():
    return render_template("forum.html")

# Sintaxe para infos dinâmicas
# @app.route('/reporter/<int:reporter_id>')
# def reporter(reporter_id):
#     return f'''
#     <h2>Reporter {reporter_id} Bio</h2>
#     <a href="/">Return to home page</a>
#     '''

# @app.route('/article/<article_name>')
# def article(article_name):
#   return f'''
#   <h2>{article_name.replace('-', ' ').title()}</h2>
#   <a href="/">Return back to home page</a>
#   '''

# Usuários
# @app.route("/usuarios/<nome_usuario>")
# def usuarios(nome_usuario):
#     return render_template("usuarios.html", nome_usuario=nome_usuario)

# Run
if __name__ == "__main__":
    app.run(debug=True)