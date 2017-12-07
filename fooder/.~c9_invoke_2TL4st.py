from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import random
import time

from helpers import apology, login_required, lookup, usd

from flask_mail import Mail
from flask_mail import Message

# Configure application
app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='mail.smtp2go.com',
	MAIL_PORT=2525,
	MAIL_USE_SSL=False,
	MAIL_USERNAME = 'abdub1@hotmail.com',
	MAIL_PASSWORD = 'iloverahal'
	)
mail = Mail(app)

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
db = SQL("sqlite:///fooder.db")

# INDEX

@app.route("/confirm", methods=["GET", "POST"])
@login_required
def confirm():

    if request.method == "POST":

        rows = db.execute("SELECT * FROM users WHERE userid=:userid", userid=session["user_id"])

        confirmation_code = request.form.get("code")
        confcode = rows[0]["confcode"]

        if confcode == confirmation_code:
            db.execute("UPDATE users SET confirmed=:confirmed WHERE userid=:userid",
                       confirmed=1, userid=session["user_id"])

            return redirect("/")

        else:
            return apology("incorrect confirmation code", 400)

    else:
        return render_template("confirm.html")


@app.route("/email")
@login_required
def email():

    rows = db.execute("SELECT * FROM users WHERE userid=:userid", userid=session["user_id"])
    email = rows[0]["email"]


    msg = Message("Confirmation Code",
                  sender="abdub1@hotmail.com",
                  recipients=['%(email)s' % {'email': email}])

    confcode = rows[0]["confcode"]


    msg.body = ('Your confirmation code is %(confcode)s' %
                {'confcode': confcode})

    mail.send(msg)

    return redirect("/confirm")



@app.route("/")
@login_required
def index():

    #cash = db.execute("SELECT cash FROM users WHERE id=:userid",
     #                 userid=session["user_id"])[0]["cash"]
# this code needs to be evaluated
    
    orders = db.execute("Select orderid from orders Where unixtime > :unixtimenowdatetime('now','-4 hours')")

    unixtimenow=int(time.time())


    #datetime(datetime, '-200 hours') <= datetime('now')")
    #Select orderid from orders Where date(datetime, "+2 hour") >= date('now')")
    #select orderid from orders DATE_ADD(datetime, INTERVAL 10 MINUTE) >= NOW()")
    #where datetime > datetime('now','-2 hours')")

    #total = cash

    #rows = db.execute("SELECT * FROM orders WHERE id=:userid", userid=session["user_id"])

    for order in orders:

        # filling index with data from the portfolio
        #data = lookup(order["symbol"])

        order["username"] = db.execute("Select username From info Where orderid=:orderid", orderid=order["orderid"])[0]["username"]

        order["foodtype"] = db.execute("Select foodtype From info Where orderid=:orderid", orderid=order["orderid"])[0]["foodtype"]

        order["description"] = db.execute("Select description From info Where orderid=:orderid", orderid=order["orderid"])[0]["description"]#orders.description

        order["location"] = db.execute("Select geolocation From info Where orderid=:orderid", orderid=order["orderid"])[0]["geolocation"]
        #orders.geolocation

        order["commits"] = db.execute("Select commits From info Where orderid=:orderid", orderid=order["orderid"])[0]["commits"]

        order["time"] = db.execute("Select datetime From info Where orderid=:orderid", orderid=order["orderid"])[0]["datetime"]#orders.datetime

        order["email"] = db.execute("SELECT users.email FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["email"]

        order["venmo"] = db.execute("SELECT users.venmo FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["venmo"]

        order["phone"] = db.execute("SELECT users.phone FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["phone"]

        order["commits"] = db.execute("SELECT commits FROM info WHERE orderid=:orderid", orderid=order["orderid"])[0]["commits"]

    return render_template("index.html", orders=orders)

@app.route("/commitments")
@login_required
def committments():

    #cash = db.execute("SELECT cash FROM users WHERE id=:userid",
     #                 userid=session["user_id"])[0]["cash"]
# this code needs to be evaluated
    orders = db.execute("Select orderid from commits Where userid=:userid",userid = session["user_id"] )
    #Select orderid from orders Where date(datetime, "+2 hour") >= date('now')")
    #select orderid from orders DATE_ADD(datetime, INTERVAL 10 MINUTE) >= NOW()")
    #where datetime > datetime('now','-2 hours')")

    #total = cash

    #rows = db.execute("SELECT * FROM orders WHERE id=:userid", userid=session["user_id"])

    for order in orders:

        # filling index with data from the portfolio
        #data = lookup(order["symbol"])

        order["username"] = db.execute("Select username From info Where orderid=:orderid", orderid=order["orderid"])[0]["username"]

        order["foodtype"] = db.execute("Select foodtype From info Where orderid=:orderid", orderid=order["orderid"])[0]["foodtype"]

        order["description"] = db.execute("Select description From info Where orderid=:orderid", orderid=order["orderid"])[0]["description"]#orders.description

        order["location"] = db.execute("Select geolocation From info Where orderid=:orderid", orderid=order["orderid"])[0]["geolocation"]
        #orders.geolocation

        order["time"] = db.execute("Select datetime From info Where orderid=:orderid", orderid=order["orderid"])[0]["datetime"]#orders.datetime

        order["email"] = db.execute("SELECT users.email FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["email"]

        order["venmo"] = db.execute("SELECT users.venmo FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["venmo"]

        order["phone"] = db.execute("SELECT users.phone FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["phone"]

        order["commits"] = db.execute("SELECT commits FROM info WHERE orderid=:orderid", orderid=order["orderid"])[0]["commits"]

    return render_template("commitments.html", orders=orders)

@app.route("/myorders")
@login_required
def myorders():

    #cash = db.execute("SELECT cash FROM users WHERE id=:userid",
     #                 userid=session["user_id"])[0]["cash"]
# this code needs to be evaluated
    orders = db.execute("Select orderid from orders Where userid=:userid", userid = session["user_id"])
    #Select orderid from orders Where date(datetime, "+2 hour") >= date('now')")
    #select orderid from orders DATE_ADD(datetime, INTERVAL 10 MINUTE) >= NOW()")
    #where datetime > datetime('now','-2 hours')")

    #total = cash

    #rows = db.execute("SELECT * FROM orders WHERE id=:userid", userid=session["user_id"])

    for order in orders:

        # filling index with data from the portfolio
        #data = lookup(order["symbol"])

        order["username"] = db.execute("Select username From info Where orderid=:orderid", orderid=order["orderid"])[0]["username"]

        order["foodtype"] = db.execute("Select foodtype From info Where orderid=:orderid", orderid=order["orderid"])[0]["foodtype"]

        order["description"] = db.execute("Select description From info Where orderid=:orderid", orderid=order["orderid"])[0]["description"]#orders.description

        order["location"] = db.execute("Select geolocation From info Where orderid=:orderid", orderid=order["orderid"])[0]["geolocation"]
        #orders.geolocation

        order["commits"] = db.execute("Select commits From info Where orderid=:orderid", orderid=order["orderid"])[0]["commits"]

        order["time"] = db.execute("Select datetime From info Where orderid=:orderid", orderid=order["orderid"])[0]["datetime"]#orders.datetime

        order["email"] = db.execute("SELECT users.email FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["email"]

        order["venmo"] = db.execute("SELECT users.venmo FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["venmo"]

        order["phone"] = db.execute("SELECT users.phone FROM users INNER JOIN info ON users.username = info.username WHERE info.orderid=:orderid", orderid=order["orderid"])[0]["phone"]

        order["commits"] = db.execute("SELECT commits FROM info WHERE orderid=:orderid", orderid=order["orderid"])[0]["commits"]

    return render_template("myorders.html", orders=orders)

# BUY
@app.route("/search")
@login_required
def search():
    """Search for places that match query"""
    # Request is a get request, we have all the data in our system
    if request.method == "GET":
        q = request.args.get("q") + "%"

    # Execute the SQL command looking for the given substring
    location = db.execute(
        "SELECT * FROM places WHERE postal_code LIKE :q OR place_name LIKE :q OR admin_name1 LIKE :q", q=q)

    return jsonify(location)


@app.route("/addentry", methods=["GET", "POST"])
@login_required
def addentry():
    """Add an entry to the db"""
    if request.method == "POST":
        if not (request.form.get("dorms")):
            return apology("must provide dorm", 403)

        if not (request.form.get("description")):
            return apology("must provide description", 403)

        if not (request.form.get("foodtype")):
            return apology("must provide food type", 403)

        if not (request.form.get("room number")):
            return apology("must provide room number", 403)

        if not (request.form.get("number of commits")):
            return apology("must provide commits", 403)

        bob = db.execute("INSERT INTO orders (userid, geolocation, description, piclocation, datetime, commits, foodtype, unixtime) \
                          VALUES(:userid, :geolocation, :description, :piclocation, :datetime, :commits, :foodtype, :unixtime)",
                         userid=session["user_id"], geolocation=request.form.get("dorms"),
                         description=request.form.get("description"),
                         piclocation=request.form.get("room number"), datetime="{:%Y/%m/%d %H:%M:%S}".format(datetime.now()),
                         commits=request.form.get("number of commits"), foodtype=request.form.get("foodtype"), unixtime=int(time.time()))



        if not bob:
            return apology("order taken", 400)

        # store their id in session
        session["user_orderid"] = bob

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("addentry.html")



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
        session["user_id"] = rows[0]["userid"]

        confirmation = rows[0]["confirmed"]

        if confirmation == 1:

        # Redirect user to home page
            return redirect("/")

        else:
            return redirect("/email")

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




@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        email = request.form.get("email")
        venmo = request.form.get("venmo")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        phone = request.form.get("phone")

        if not "@college.harvard.edu" in email:
            return apology("only available for Harvard Students", 400)

        if not username:
            return apology("no username input", 400)

        if not password:
            return apology("no password input", 400)

        if not email:
            return apology("no email input", 400)

        if not firstname:
            return apology("name not valid", 400)

        if not lastname:
            return apology("name not valid", 400)

        if not phone:
            return apology("insert a valid phone number", 400)

        if not confirmation:
            return apology("password does not match confirmation", 400)

        if password != confirmation:
            return apology("password does not match confirmation", 400)

        num_count = 0
        let_count = 0
        sym_count = 0
        for c in password:

            if c.isdigit():
                num_count += 1
            elif c.isalpha():
                let_count += 1
            else:
                sym_count += 1

        if not num_count and not let_count and not sym_count:
            return apology("your password needs at least one letter, number, and symbol!")

        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # makes sure that a username is not being used
        if len(rows) != 0:
            return apology("username already taken", 400)

        hashpass = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # creating the user profile in users
        db.execute("INSERT INTO users (username, hash, email, venmo, firstname, lastname, phone, confcode) VALUES (:username, :password, :email, :venmo, :firstname, :lastname, :phone, :confcode)",
                   username=username, password=hashpass, email=email, venmo=venmo, firstname=firstname, lastname=lastname, phone=phone, confcode=(random.randrange(1000, 9999)))

        userid = db.execute("SELECT userid FROM users WHERE username=:username",
                            username=username)[0]["userid"]
        session["user_id"] = userid

        return redirect("/email")

    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)







