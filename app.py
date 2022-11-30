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

@app.route("/feed", methods=["GET", "POST"])
@login_required
def feed():
    #Call username using id to render on feed
    username = db.execute("SELECT * FROM accounts WHERE id = ?", session["user_id"])[0]["username"]
    """Show landing page"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("message"):
            flash("Please input in a message.")
            return render_template("feed.html", username=username)
        message = request.form.get("message")
        username = db.execute("SELECT * FROM accounts WHERE id = ?", session["user_id"])[0]["username"]
        try:
            # Add to the database
            db.execute("INSERT INTO posts (user_id, username, message, date) VALUES(?, ?, ?, datetime('now', 'localtime'))",
                        session["user_id"], username, message)
            return redirect("/feed")
        except:
            flash("Fatal Error")
            postFeed = db.execute("SELECT username, message, date FROM posts ORDER BY id DESC")
            return render_template("feed.html", username=username)
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        postFeed = db.execute("SELECT * FROM posts ORDER BY id DESC")
        return render_template("feed.html", username=username, postFeed=postFeed)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Please insert username.")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Please insert password.")
            return render_template("login.html")

        # Query database for username
        currentUser = db.execute("SELECT * FROM accounts WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(currentUser) != 1 or not check_password_hash(currentUser[0]["hash"], request.form.get("password")):
            flash("invalid username and/or password")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = currentUser[0]["id"]

        # Redirect user to home page
        return redirect("/feed")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# The delete route purpose is to allow users to delete their post.
@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    """Delete posts"""
    if request.method == "POST":
        postId = request.form.get("postId")
        # Verify user has the credentials to delete post
        if session["user_id"] == 2:
            flash("You are Anonymous. You have no delete post privileges ☹️. Please refresh page.")
            return(redirect("/feed"))
        ownership = db.execute("SELECT * FROM posts WHERE user_id = ? AND id = ?", session["user_id"], postId)
        if ownership == 0:
            try:
                #db.execute("SELECT * FROM posts WHERE user_id = ? AND id = ?", session["user_id"], postId)[0]["id"]
                db.execute("DELETE FROM posts WHERE user_id = ? AND id = ?", session["user_id"], postId)
                #db.execute #to delete the post corresponding to the postID
                return redirect("/feed")
            except:
                flash("Something went wrong, please try again.")
                return(redirect("/feed"))
        else:
            flash("Sorry, can't delete. You do NOT own this post ☹️. Moderators will look into it 🧐.")
            return(redirect("/feed"))
    else:
        return ("/feed")