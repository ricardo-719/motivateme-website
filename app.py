import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Show landing page"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Redirect user to home page
        return redirect("/feed")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()
    if request.method == "POST":
        # Validate submission: No empty fields, password and confirmation match
        if not request.form.get("username"):
            flash("Invalid username. Please try again")
            return render_template("register.html")
        if not request.form.get("password") or request.form.get("password") != request.form.get("confirmation"):
            flash("Invalid password. Please try again.")
            return render_template("register.html")
        else:
            # Password requirements verification following regular expressions defined
            reg = "(?=.*[A-Z])(?=.*[0-9])(?=.{8,}$)"
            match_re = re.compile(reg)
            res = re.search(match_re, request.form.get("password"))
            if res:
                username = request.form.get("username")
                password = request.form.get("password")
                hash = generate_password_hash(password)
                try:
                    # Add user to the database
                    db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
                except:
                    flash("Something went wrong. Please try again.")
                    return render_template("register.html")
                return redirect("/feed")
            else:
                flash("Password must contain (1) uppercase and (1) digit. At least (8) chars long.")
                return render_template("register.html")
    else:
        return render_template("register.html")