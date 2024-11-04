from flask import*      
from model import*

app_controller = Blueprint('controller', __name__)

@app_controller.route('/')
def index():
    if 'nome' in session:
        return render_template('home.html', resposta=f'Bem-vindo {session["nome"]}', id=0)
    return render_template('index.html', resposta='Você não está logado', id=1)

@app_controller.route('/login', methods=['GET', 'POST'])
def login():
    if 'nome' in session:
        return redirect(url_for('controller.index'))
    
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        if session['nome'] == '':
            return render_template('login.html')
        return redirect(url_for('controller.index'))
    return render_template('login.html')

@app_controller.route('/logout')
def logout():
    session.pop('nome', None)
    return redirect(url_for('controller.index'))