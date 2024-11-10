# controllers/auth_controller.py
from flask import request, session, redirect, url_for, render_template

# Banco de dados simples para armazenar usuários
users_db = {}

def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Verificação para login
        if username in users_db and users_db[username] == password:
            session['user'] = username
            return redirect(url_for("boas_vindas"))
        
        elif username == "admin" and password == "1234":
            # Caso seja o usuário admin
            session['user'] = username
            return redirect(url_for("boas_vindas"))
        
        else:
            return "<p>Usuário ou senha incorretos!</p>"
    
    return render_template("login.html")  # Carrega a tela de login

def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Verificação se o nome de usuário já existe
        if username in users_db:
            return "<p>Usuário já existe!</p>"
        
        # Salva o novo usuário
        users_db[username] = password
        return redirect(url_for("login_route"))  # Redireciona para a página de login após o registro
    
    return render_template("register.html")  # Carrega o formulário de registro
