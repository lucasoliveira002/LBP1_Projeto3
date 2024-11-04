from flask import Flask, render_template
from controllers.questionarioController import questionariocontroller

app = Flask(__name__)
app.register_blueprint(questionarioController)