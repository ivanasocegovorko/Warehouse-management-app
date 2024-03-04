import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp

from helpers import apology, login_required

import datetime

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'super secret key'
#Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///warehouse.db")

def get_db_connection():
    conn = sqlite3.connect('warehouse.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show warehouse inventory"""
    # get_db_connection() function used to open a database connection
    conn = get_db_connection()
    warehousedb = conn.execute("SELECT * FROM status ORDER BY datetime DESC, name ASC").fetchall()
    conn.close()

    return render_template("index.html", warehousedb = warehousedb)

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    """Updating warehouse inventory"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        name = request.form.get("name")
        quantity = request.form.get("quantity")

        # Updating database

        conn = sqlite3.connect('warehouse.db')
        cur = conn.cursor()
        date = datetime.datetime.now().replace(
            microsecond=0,
            second=0
        )
        query = "INSERT INTO status (name, quantity, datetime) VALUES (?, ?, ?)"
        val = (name, quantity, date)

        cur.execute(query,val)
        conn.commit()
        conn.close()

        return render_template("admin.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("admin.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():

    button_id = request.form.get("delete")

    # Updating database

    conn = sqlite3.connect('warehouse.db')
    cur = conn.cursor()

    query = "DELETE FROM status where id = ?"
    val = button_id

    cur.execute(query, (val,))
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/loginadmin", methods=["GET", "POST"])
def loginadmin():
    """Log admin in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("admin_username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("admin_password"):
            return apology("must provide password", 403)

        # Ensure username exists and password is correct
        if request.form.get("admin_username") != 'zoran': 
            return apology("invalid username and/or password", 403)

        # Ensure username exists and password is correct
        if request.form.get("admin_password") != 'jasenska': 
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = 'zoran'

        # Redirect user to home page
        return redirect("/admin")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("loginadmin.html")

@app.route("/loginuser", methods=["GET", "POST"])
def loginuser():
    """Log admin in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure username exists and password is correct
        if request.form.get("username") != 'ivana': 
            return apology("invalid username and/or password", 403)

        # Ensure username exists and password is correct
        if request.form.get("password") != 'zagreb': 
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = 'ivana'

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("loginuser.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/loginuser")



   