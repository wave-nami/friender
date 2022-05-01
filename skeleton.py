from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sl
from datetime import datetime, date

app = Flask(__name__)
# TODO : database file name
db = '.db'


@app.route("/")
def home():
    """ home page """
    # might need to pass more components
    return render_template("index.html")


@app.route("/client")
def client():
    """ send user to their user page """
    # admin: sent to admin.html
    if session['admin']:
        return render_template('admin.html')
    # user: sent to user.html
    else:
        return render_template('user.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    # check credentials with db
    # if credential is correct, send to client()
    # start session
    # else send them back to log in page
    if request.method == "POST" and db_check_creds(request.form["username"], request.form["password"]):
        session["username"] = request.form["username"]
        session["logged_in"] = True
        return redirect(url_for('client'))
    else:
        return redirect(url_for('home'))


@app.route("/registration", methods=["POST", "GET"])
def registration():
    """ send user to registration form """
    # format the birthday
    formatted = datetime.today().strftime('%Y-%m-%d')
    year = int(formatted[:4]) - 18
    birthday = str(year) + formatted[4:]

    # check if there is an error message
    em = session.pop('errorMessage', None)
    if em is None:
        em = ''
    return render_template('registration.html', date=birthday, errorMessage=em)


@app.route("/registration/numberVerification", methods=["POST", "GET"])
def numberVerification():
    """ verify new account with SMS code verification """
    # TODO : implement twilio API
    if request.method == "POST":
        code = request.form["code"]
        number = session.pop('number', None)
        # verify if the code works
        verified = code

        if verified == True:
            # add a user to the database
            # the inputs need to come from register() as session variables
            fname = session.pop('firstname', None)
            db_create_user(fname, ...)
            # redirect user to their user page
            return redirect(url_for("client"))
        else:
            # try verifying again or redirect them to registration
            return redirect(url_for("numberVerification"))


@app.route("/action/register", methods=["POST", "GET"])
def register():
    """ submitted registration form, add new user to the database """
    if request.method == "POST":
        # TODO : how to input interests
        # TODO : check the name attributes of the form
        # TODO : check how to block empty entries
        # sessions and variable names for checking the credentials are right
        # firstname, lastname, username, number, password, confirm, interests, sexual orientation
        #   profile picture, social media, culture/race/ethnicity

        # examples
        session['firstname'] = request.form["fname"]
        session['lastname'] = request.form["lname"]

        # other form responses
        username = request.form["username"]
        number = request.form["number"]
        password = request.form["password"]
        confirm = request.form["password"]
        age = calc_age(request.form["birthday"])

        # and other parts of the profile
        em = verify_registration(username, password, confirm)
        if em != '':
            session['errorMessage'] = em
            return redirect(url_for("registration"))

    # send to number verification
    session['number'] = number
    return redirect(url_for("numberVerification"))


@app.route("/userinfo")
def userinfo():
    # TODO : user profile page
    return render_template('userinfo.html')


@app.route("/action/edit", methods=["POST", "GET"])
def edit_userinfo():
    # TODO : edit user information
    pass


@app.route("/action/interest", methods=["POST", "GET"])
def interest():
    # TODO : show users that clicked on the same interest
    users = db_get_interest_list()
    return redirect(url_for("client"))


@app.route("/chat")
def chat():
    # TODO : show chat between 2 users
    pass


@app.route("/action/friendrequest", methods=["POST", "GET"])
def friendrequest():
    # TODO : send someone a friend request
    pass


@app.route("/action/friendrequest", methods=["POST", "GET"])
def friendrequest():
    # TODO : accept a friend request
    pass


@app.route("/logout", methods=["POST", "GET"])
def logout():
    # destroy session
    # send them back to home page
    if request.method == "POST":
        session["logged_in"] = False
        session.pop('username', None)
        return redirect(url_for('home'))


def verify_registration(un, pw, c):
    """ verify user registration """
    # TODO : implement verification methods
    # any of the entries are empty
    users = db_get_user_list()
    if not face_verification():
        return 'Face verification failed. Possible reasons can include bad lighting, angles, etc.'
    # if user already exists
    elif un in users:
        return 'Username already exists.'
    # password is too short
    elif len(pw) < 8:
        return 'Password is too short.'
    # password and confirm password are different


def calc_age(b):
    """ calculate users age from their birthday in YYYY-MM-DD format """
    year, month, date = b.split('-')
    birthdate = date(int(year), int(month), int(date))
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def face_verification():
    # TODO : face verification (later)
    pass


def db_create_user(un, pw):
    # TODO : implement create user functionality
    pass


def db_get_user_list():
    # TODO : implement get user list functionality
    brutish = []
    return brutish


def db_check_creds(un, pw):
    # TODO : check creds
    return True


def db_get_userinfo():
    # TODO : get user's info
    pass


def db_set_userinfo(inp):
    # TODO : set user's info
    pass


def db_remove_user(un):
    # TODO : remove user info
    pass


def db_get_interest_list(int):
    # TODO : get users that have the same interest
    l = []
    return l