# /usr/bin/python3
# coding=utf-8

import re, time
from flask import Flask, render_template, request, redirect, session, flash
from openmysqldb import *

app = Flask(__name__)
app.secret_key = 'ThisIsSecretly'

def save_form(form):
    email = form['email']
    mysql = OpenMySqlDb("dojodb")
    qryres = mysql.query_db("Select email,create_at from dojo_users;")
    arr = arr_from_qry(qryres, 1)
    if email in arr:
        flash("This email has existed!", "email")
        mysql.close()
        return False
    timestr = time.strftime("%m/%d/%y %I:%M%p", time.localtime());
    str = form['first_name'] + "','" + form['last_name'] + "','" + form['email'] + "','" + form['pwd'] + "','" + timestr
    sql = "Insert into dojo_users (first_name,last_name,email,password,create_at) values ('" + str + "');"
    mysql.query_db(sql)
    mysql.query_db("commit")
    mysql.close()
    return True

def check_login(email, pwd):
    mysql = OpenMySqlDb("dojodb")
    sql = "Select email,password from dojo_users where email='" + email + "' and password='" + pwd + "';"
    qryres = mysql.query_db(sql)
    arr = arr_from_qry(qryres, 1)
    if arr == []: return False
    else:         return True

@app.route('/')
def login():
    session.clear()
    return render_template("login.html", mymode=0)

@app.route('/register_post', methods=['post'])
def register_post():
    session.clear()
    session["email"]        = request.form['email']
    session["first_name"]   = request.form['first_name']
    session["last_name"]    = request.form['last_name']
    session["pwd"]          = request.form['pwd']
    session["confirm"] = request.form['confirm']
    mode = 1
    if checkFirstName(request.form['first_name']) == True:
        mode = 2
        if checkLastName(request.form['last_name']) == True:
            mode = 3
            if checkEmail(request.form['email']) == True:
                mode = 4
                if checkPwd(request.form['pwd']) == True:
                    mode = 5
                    if checkConfirm(request.form['confirm'], request.form['pwd']) == True:
                        mode = 3
                        if save_form(request.form) == True :
                            mode = 7
    return render_template("login.html", mymode=mode)

@app.route('/login_post', methods=['post'])
def login_post():
    session.clear()
    session["log_email"] = request.form['log_email']
    session["log_pwd"] = request.form['log_pwd']
    if check_login(session["log_email"], session["log_pwd"]) == False:
        mode = 8
    else:
        mode = 9
        session.clear()
    return render_template("login.html", mymode=mode)

if __name__=="__main__":
    app.run()
