# /usr/bin/python3
# coding=utf-8

import re
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ThisIsSecretly'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def exist_space(str):
    if ' ' in str:
        return True;
    return False;

def exist_num(str):
    return bool(re.search(r'\d',str))

def checkEmail(email):
    Len = len(email)
    if Len <= 0: flash("Email can not be blank! ", "email"); return False
    if Len <= 3: flash("Email must be 3+ characters! ", "email"); return False
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if re.match(EMAIL_REGEX, email): return True
    flash("Invalid email address! ", "email"); return False

def checkFirstName(name):
    Len = len(name)
    if Len <= 0: flash("First_name can not be blank! ", "first_name"); return False
    if Len <= 3: flash("First_name must be 3+ characters! ", "first_name"); return False
    if exist_space(name): flash("First_name included a invalid space! ", "first_name"); return False
    if exist_num(name): flash("First_name included number(s)! ", "first_name"); return False
    return True

def checkLastName(name):
    Len = len(name)
    if Len <= 0: flash("Last_name can not be blank! ", "last_name"); return False
    if Len <= 3: flash("Last_name must be 3+ characters! ", "last_name"); return False
    if exist_space(name): flash("Last_name included a invalid space! ", "last_name"); return False
    if exist_num(name): flash("Last_name included number(s)! ", "last_name"); return False
    return True

def checkPwd(pwd):
    Len = len(pwd)
    if Len <= 0: flash("Password can not be blank! ", "pwd"); return False
    if Len <  8: flash("Password must be 8+ characters! ", "pwd"); return False
    if exist_space(pwd): flash("Password included a invalid space! ", "pwd"); return False
    return True

def checkConfirm(confirm, pwd):
    if confirm != pwd: flash("Password not be confirmed! ", "confirm"); return False
    return True

@app.route('/')
def index():
    return render_template("log.html")

@app.route('/log_post', methods=['post'])
def log_post():
    session["email"]        = request.form['email']
    session["first_name"]   = request.form['first_name']
    session["last_name"]    = request.form['last_name']
    session["pwd"]          = request.form['pwd']
    if checkEmail(request.form['email']) == True:
        if checkFirstName(request.form['first_name']) == True:
            if checkLastName(request.form['last_name']) == True:
                if checkPwd(request.form['pwd']) == True:
                    if checkConfirm(request.form['confirm'], request.form['pwd']) == True:
                        session.clear();
                        flash("Submitted successfully! ", 'ok')
    return redirect("/")

if __name__=="__main__":
    app.run()
