from whitenoise import WhiteNoise

from flask import Flask
from flask import render_template

from app.portfolio import portfolio

app = Flask(__name__)

app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")

app.register_blueprint(portfolio)


@app.errorhandler(404)
def not_found(error_message):
    return render_template("404.html"), 404
