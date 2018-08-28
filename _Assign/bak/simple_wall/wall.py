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
    timestr = time.strftime("%m/%d/%y %I:%M%p", time.localtime())
    str = form['first_name'] + "','" + form['last_name'] + "','" + form['email'] + "','" + form['pwd'] + "','" + timestr
    sql = "Insert into dojo_users (first_name,last_name,email,password,create_at) values ('" + str + "');"
    mysql.query_db(sql)
    mysql.query_db("commit")
    mysql.close()
    return True

def save_message(form):
    for dict in form:
        id = dict
        info=form[id]
        if info=='': return
    vid = str(id)
    sid = session['me_id']
    mysql = OpenMySqlDb("dojodb")
    timestr = time.strftime("%m/%d/%y %I:%M%p", time.localtime())
    sql = "Insert into dojo_message (message, sender_id, viewer_id, create_at)  values ('" +info+ "','" +sid+ "','" + vid +"','" +timestr+ "');"
    mysql.query_db(sql)
    mysql.query_db("commit")
    mysql.close()

def check_login(email, pwd):
    mysql = OpenMySqlDb("dojodb")
    sql = "Select email,password from dojo_users where email='" + email + "' and password='" + pwd + "';"
    qryres = mysql.query_db(sql)
    arr = arr_from_qry(qryres, 1)
    mysql.close()
    if arr == []: return False
    else:         return True

def qry_me():
    email = session['log_email']
    mysql = OpenMySqlDb("dojodb")
    sql = "Select id,first_name from dojo_users where email='" + email + "';"
    qryres = mysql.query_db(sql)
    arr = arr_from_qry(qryres, 1)
    session['me_id'] = str(arr[0])
    sql = "Select message from dojo_message where sender_id='" +session['me_id']+ "';"
    qryres = mysql.query_db(sql)
    session['me_email'] = email
    session['me_total'] = len(arr_from_qry(qryres, 1))
    session['me_name'] = arr[1]
    mysql.close()

def qry_peers():
    arr = []
    email = session['log_email']
    mysql = OpenMySqlDb("dojodb")
    sql = "Select id, first_name from dojo_users where email !='" + email + "';"
    qryres = mysql.query_db(sql)
    arr = arr_from_qry(qryres, 1)
    return dict_from_arr(arr)

def qry_info():
    arr = []
    mysql = OpenMySqlDb("dojodb")
    me_id = session['me_id']
    sql = "select first_name, dojo_message.create_at, message from dojo_message join dojo_users where sender_id = dojo_users.id and  viewer_id ='" +me_id+ "';"
    qryres = mysql.query_db(sql)
    arr = arr_from_qry(qryres, 1)
    session['info_total'] = round(len(arr)/3)
    mysql.close()
    return arr

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
        return render_template("login.html", mymode=mode)
    else:
        mode = 9
        qry_me()
        peers = qry_peers()
        info = qry_info()
        return render_template("wall.html", mypeers=peers, myinfo=info)


@app.route('/wall_post', methods=['post'])
def wall_post():
    return render_template("login.html", mymode=0)

@app.route('/message_post', methods=['post'])
def message_post():
    save_message(request.form)
    qry_me()
    peers = qry_peers()
    info = qry_info()
    return render_template("wall.html", mypeers=peers, myinfo=info)

if __name__=="__main__":
    app.run()
