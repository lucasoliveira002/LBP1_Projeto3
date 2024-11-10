from flask import Flask, render_template, request, session, redirect, url_for
from controllers.auth_controller import login, register  # Importa as funções de login e registro

app = Flask(__name__)
app.secret_key = '12'

# Middleware - Verificar se o usuário está autenticado
@app.before_request
def check_user_logged_in():
    # Se o usuário não estiver logado e a rota não for login, home ou registro, redireciona para o login
    if 'user' not in session and request.endpoint not in ['login_route', 'register_route', 'home']:
        return redirect(url_for('login_route'))

# Rota para a página inicial
@app.route("/")
def hello_world():
    return redirect(url_for("home"))

# Rota para renderizar o arquivo home.html
@app.route("/home")
def home():
    return render_template("home.html")

# Rota de login
@app.route("/login", methods=["GET", "POST"])
def login_route():
    return login()  # Chama a função de login

# Rota de cadastro
@app.route("/register", methods=["GET", "POST"])
def register_route():
    return register()  # Chama a função de registro

# Rota para a página de boas-vindas
@app.route("/boas_vindas")
def boas_vindas():
    username = session.get('user')
    if not username:
        return redirect(url_for("login_route"))
    
    return render_template("boas_vindas.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
