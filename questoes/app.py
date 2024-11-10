from flask import Flask, render_template, session, redirect, url_for, request
from controllers.questoesController import questoesController

app = Flask(__name__)
app.secret_key = "oidahfoknas"

rotas_publicas = ["questoes.index", "questoes.verifica"]

@app.before_request
def verificaSessao():
    if request.endpoint in rotas_publicas:
        return
    
    # if "email" not in session:
    #     return redirect(url_for("questoes.index"))
    return

app.register_blueprint(questoesController)

if __name__ == "__main__":
    app.run(debug = True)