from whitenoise import WhiteNoise
from flask import Flask, request, render_template
from app.portfolio import portfolio
import os
from . import db

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.register_blueprint(portfolio)

@app.errorhandler(404)
def not_found(error_message):
    return render_template("404.html"), 404
