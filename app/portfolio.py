from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request
from dotenv import load_dotenv
from app.db import get_db

load_dotenv()

portfolio = Blueprint("portfolio", __name__, template_folder="templates")

@portfolio.route("/")
def index():
    title = "Miyabi"
    description = "About Me"
    return render_template(
        "index.html",
        title=title,
        description=description,
    )

@portfolio.route("/health")
def health():
    return render_template("404.html"), 200

@portfolio.route("/projects/")
def projects():
    title = "Projects"
    description = "Project"
    return render_template(
        "projects.html",
        title=title,
        description=description,
    )


@portfolio.route("/contact/")
def contact():
    title = "Contact"
    description = "contact"
    return render_template(
        "contact.html",
        title=title,
        description=description,
    )


@portfolio.route("/resume/")
def resume():
    title = "Resume"
    description = "Resume"
    return render_template(
        "resume.html",
        title=title,
        description=description,
    )

@portfolio.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return render_template("login.html")
        else:
            return error, 418

    ## TODO: Return an actual register page
    return render_template("register.html")

@portfolio.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return render_template("index.html")
        else:
            return error, 418
    return render_template("login.html")
