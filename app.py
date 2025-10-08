from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

#Rotas (endpoints)

@app.route("/") # Rota quando for acessado "/"
def ola_mundo():
    return "<p>Olá, Mundo!</p>"

@app.route("/ola")
def ola():
    nome = request.args.get("nome", "Flask")
    return f"<p>Olá {escape(nome)}!</p>"

@app.route("/usuario/<nome>")
def mostrarUsuario(nome):
    return f"usuário: {escape(nome)}"

@app.route("/produto/<id>")
def mostrarProduto(id):
    return f"Produto: {escape(id)}"

@app.route("/soma/<int:num1>/<int:num2>")
def somarDoisNumeros(num1, num2):
    return f"Soma: {escape(num1 + num2)}"

app.route("/agenda")
def mostrarAgenda():
    return render_template("agenda.html")