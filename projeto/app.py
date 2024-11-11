from flask import Flask, render_template, request, session, redirect, url_for
from controllers.auth_controller import login, register, adicionar  # Importa as funções de login e registro

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

# rota de adicionar
@app.route("/adicionar", methods=["GET", "POST"])
def adicionar_route():
    if request.method == "POST":
        adicionar();
    return render_template("adicionar.html")

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

@app.route("/lista", methods=['POST', 'GET'])
def lista():
    #{session["animal"]}
    animal = session.get('animal')
    data = session.get('data')
    tipo = session.get('tipo')
    return render_template("lista.html", animal=animal, data=data, tipo=tipo)
    #if request.method == 'POST':
        #session['animal'] = request.form['animal']
        #session['tipo'] = request.form['tipo']
        #session['data'] = request.form['data']

if __name__ == "__main__":
    app.run(debug=True)
