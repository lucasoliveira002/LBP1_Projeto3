from flask import Flask
from controllers import playlist_controller

app = Flask(__name__)
app.register_blueprint(playlist_controller)

if __name__ ==  '__main__':
    app.run(debug=True)