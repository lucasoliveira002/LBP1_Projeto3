from flask import Blueprint, render_template, request, redirect, url_for, session, make_response

questoesController = Blueprint("questoes", __name__)

a = 10
b = 15

@questoesController.route("/")
def index():
    return render_template("index.html", a = a, b = b)

@questoesController.route("/verifica", methods = ["POST"])
def verifica():
    nome = request.form.get("nome")
    email = request.form.get("email")
    resposta = request.form.get("resposta")
    if email.split("@")[1] == "aluno.ifsp.edu.br":
        if resposta == "25":
            session["email"] = email
            session["nome"] = nome
            return redirect(url_for("questoes.questionario"))
        return "email certo, mas resposta errada"
    return "email errado"

@questoesController.route("/questionario", methods = ["GET", "POST"])
def questionario():
    if request.method == "POST":
        resposta1 = request.form["pergunta1"]
        resposta2 = request.form["pergunta2"]
        response = make_response(render_template("fim.html"))
        
        if resposta1 == "Deodoro da Fonseca":
            response.set_cookie("resposta1", "Correto", max_age = 60 * 60 * 24)
        else:
            response.set_cookie("resposta1", "Incorreto", max_age = 60 * 60 * 24)
        
        if resposta2 == "1822":
            response.set_cookie("resposta2", "Correto", max_age = 60 * 60 * 24)
        else:
            response.set_cookie("resposta2", "Incorreto", max_age = 60 * 60 * 24)
        
        return response
    return render_template("questionario.html")

@questoesController.route("/logout")
def logout():
    resp = make_response(redirect(url_for("questoes.index")))
    session.pop("email", None)
    session.pop("nome", None)
    resp.set_cookie("resposta1", "", expires = 0)
    resp.set_cookie("resposta2", "", expires = 0)
    return resp