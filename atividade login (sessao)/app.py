from flask import*
from controller import*

app = Flask(__name__)
app.register_blueprint(app_controller)
app.secret_key = '1234566789'

if __name__ == '__main__':
    app.run(debug = True)