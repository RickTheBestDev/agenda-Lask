from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

# Rotas (endpoints)

@app.route("/") # Rota quando for acessado "/"
def ola_mundo():
    return "<p>Olá, Mundo!</p>"

@app.route("/ola") # Rota quando for acessado "/ola"
def ola():
    nome = request.args.get("nome", "Flask")
    return f"<p>Olá, {escape(nome)}!</p>"

@app.route("/usuario/<nome>")
def mostrarUsuario(nome):
    return f"Usuário: {escape(nome)}"

@app.route("/produto/<id>")
def mostrarProduto(id):
    return f"Produto: {escape(id)}"

@app.route("/soma/<int:num1>/<int:num2>")
def somarDoisNumeros(num1, num2):
    return f"Soma: {escape(num1 + num2)}"

@app.route("/agenda")
def mostrarAgenda():
    return render_template("agenda.html", title="Agenda Python")

@app.route("/multiplos/<int:x>/<int:y>")
def multiplosAteY(x, y):
    z = 0
    i = 1
    listaMultiplos = []
    while z <= y:
        z = x * i
        i += 1
        if z > y:
            break
        listaMultiplos.append(z)
    return ", ".join(map(str, listaMultiplos))

@app.route("/pares/<int:inicio>/<int:fim>")
def pares(inicio, fim):
    par = 0 
    pares = []
    if inicio % 2 == 0:
        pares.append(inicio)
    while par <= fim:
        inicio += 1
        if inicio % 2 == 0:
            par = inicio
            if par >= fim:
                break
            else:
                pares.append(par)
    return ", ".join(map(str, pares))

@app.route("/fatorial/<int:n>")
def fatorial(n):
    if n < 0:
        return "O número inserido é negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return f"{n}! = {resultado}"
    
@app.route("/soma/<int:n>")
def soma(n):
    soma = 0
    resultado = 0
    while soma <= n:
        for i in range(1, n + 1):
            resultado += i
        return f"{resultado}"

'''  
@app.route("/primos/<int:limite>")
def primos(limite):
    n = 0
    primos = []
'''