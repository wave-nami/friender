from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sl

app = Flask(__name__)
# name of .db file
db = '.db'

@app.route("/")
def home():
    """ home page """
    # might need to pass more components
    return render_template("index.html")

@app.route("/client")
def client():
    # admin: sent to admin.html
    if session['admin'] == True:
        return render_template('admin.html')
    # user: sent to user.html
    else:
        return render_template('user.html')

@app.route("/action/createuser", methods=["POST", "GET"])
def create_user():
    db_create_user("username", "password")



def db_create_user(un, pw):
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un, pw)
    stmt = "INSERT OR IGNORE INTO credentials (username, password) VALUES " + str(v)
    curs.execute(stmt)
    conn.commit()
    conn.close()