from werkzeug.security import generate_password_hash
from app.db import get_db
from flask import Blueprint, render_template
from dotenv import load_dotenv

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

@app.route('/register', methods=('GET', 'POST'))
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
            return f"User {username} created successfully"
        else:
            return error, 418

    ## TODO: Return an actual register page
    return "Register Page not yet implemented", 501
