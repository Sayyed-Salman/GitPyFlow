from flask import Flask
import requests


def create_app(config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello Flask!'

    @app.route('/add/<int:num1>/<int:num2>')
    def add(num1, num2):
        return f"{num1} + {num2} = {num1 + num2 + 1}"

    return app
