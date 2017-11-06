from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# INDEX
@app.route("/")
@login_required
def index():

    cash = db.execute("SELECT cash FROM users WHERE id=:userid", userid=session["user_id"])[0]["cash"]
    total = cash

    rows = db.execute("SELECT * FROM portfolio WHERE id=:userid", userid=session["user_id"])

    for row in rows:

        data = lookup(row["symbol"])
        row["name"] = data["name"]
        row["price"] = usd(data["price"])
        row["total"] = float(data["price"])*row["shares"]
        row["total2"] = usd(row["total"])
        total += row["total"]

    return render_template("index.html", total=usd(total), rows=rows, cash=usd(cash))

# BUY
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")

    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        data = lookup(request.form.get("symbol"))

        if not shares.isdigit():
            return apology("hello", 400)

        if not symbol:
            return apology("not a valid stock symbol", 400)

        if not shares:
            return apology("not a valid number of shares", 400)

        if not data:
            return apology ("not a valid stock symbol", 400)

        cost = data["price"]*float(shares)
        cash = db.execute("SELECT cash FROM users WHERE id =:userid", userid = session["user_id"])[0]["cash"]

        if cost > cash:
            return apology("Get your money up", 400)

        shareRows = db.execute("SELECT shares FROM portfolio WHERE id=:userid AND symbol=:symbol", userid = session["user_id"], symbol = data["symbol"])

        if len(shareRows) == 0:
            db.execute("INSERT INTO portfolio (id, symbol, shares) VALUES (:userid, :symbol, :shares)", userid = session["user_id"], symbol = data["symbol"], shares = shares)

        else:
            NumSharesOwn = shareRows[0]["shares"]
            db.execute("UPDATE portfolio SET shares=:shares WHERE id=:userid AND symbol=:symbol", shares = NumSharesOwn + int(shares), userid = session["user_id"], symbol = data["symbol"])

        db.execute("UPDATE users SET cash=:cash WHERE id=:userid", cash = cash - cost, userid = session["user_id"])

        time = "{:%Y/%m/%d %H:%M:%S}".format(datetime.now())
        db.execute("INSERT INTO transactions (id, symbol, shares, price, type, time) VALUES (:userid, :symbol, :shares, :price, :ttype, :time)", userid = session["user_id"], symbol = data["symbol"], shares = shares, price = data["price"], ttype = "purchase", time = time)

        return redirect("/")

# HISTORY
@app.route("/history")
@login_required
def history():

    rows = db.execute("SELECT * FROM transactions WHERE id=:userid", userid=session["user_id"])

    for row in rows:

        data = lookup(row["symbol"])
        row["symbol"] = data["symbol"]
        row["price"] = usd(data["price"])
        #row["shares"] = data["shares"]
        #row["time"] = data["time"]

    return render_template("history.html", rows=rows)

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

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

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    #gives the user the form to request a stock quote
    if request.method == "GET":
        return render_template("quote.html")

    else:
        data = lookup(request.form.get("symbol"))

        if data is None:
            return apology("invalid symbol")

        #tells user how much the stock is worth
        message = "One {} share ({}) is worth {}".format(data["name"], data["symbol"], usd(data["price"]))
        return render_template("quoted.html", message=message)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ensures that password must have at least one digit!
        digit = False
        length = len(password)
        for i in range(length):
            character = password[i]

            if character.isdigit():
                digit = True

        if digit == False:
            return apology("password must have at least one digit", 400)

        if not username:
            return apology("no username input", 400)

        if not password:
            return apology("no password input", 400)

        if not confirmation:
            return apology("password does not match confirmation", 400)

        if password != confirmation:
            return apology("password does not match confirmation", 400)

        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        if len(rows) != 0:
            return apology("username already taken", 400)

        hashpass = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        db.execute("INSERT INTO users (username, hash) VALUES (:username, :password)", username = username, password = hashpass)

        userid = db.execute("SELECT id FROM users WHERE username=:username", username=username)[0]["id"]
        session["userid"] = userid

        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    if request.method == "GET":
        rows = db.execute("SELECT symbol FROM portfolio WHERE id=:userid", userid=session["user_id"])
        return render_template("sell.html", rows=rows)

    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        data = lookup(request.form.get("symbol"))

        if not symbol:
            return apology("not a valid stock symbol", 400)

        if not shares:
            return apology("not a valid number of shares", 400)

        if not data:
            return apology ("not a valid stock symbol", 400)

        cost = data["price"]*float(shares)
        cash = db.execute("SELECT cash FROM users WHERE id =:userid", userid = session["user_id"])[0]["cash"]

        shareRows = db.execute("SELECT shares FROM portfolio WHERE id=:userid AND symbol=:symbol", userid = session["user_id"], symbol = data["symbol"])
        NumSharesOwn = shareRows[0]["shares"]


        if int(shares) > NumSharesOwn:
            return apology ("not enough shares owned", 400)

        else:
            db.execute("UPDATE portfolio SET shares=:shares WHERE id=:userid AND symbol=:symbol", shares = NumSharesOwn - int(shares), userid = session["user_id"], symbol = data["symbol"])

        newshares = NumSharesOwn - int(shares)
        shareRows = db.execute("SELECT shares FROM portfolio WHERE id=:userid AND symbol=:symbol", userid = session["user_id"], symbol = data["symbol"])

        if newshares == 0:
            #db.execute("DELETE FROM portfolio (id, symbol, shares) VALUES (:userid, :symbol, :shares)", userid = session["user_id"], symbol = data["symbol"], shares = shares)
            db.execute("DELETE FROM portfolio WHERE id=:userid AND symbol=:symbol", userid=session["user_id"], symbol=data["symbol"])

        db.execute("UPDATE users SET cash=:cash WHERE id=:userid", cash = cash + cost, userid = session["user_id"])

        time = "{:%Y/%m/%d %H:%M:%S}".format(datetime.now())
        db.execute("INSERT INTO transactions (id, symbol, shares, price, type, time) VALUES (:userid, :symbol, :shares, :price, :ttype, :time)", userid = session["user_id"], symbol = data["symbol"], shares = shares, price = data["price"], ttype = "sale", time = time)

        return redirect("/")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
