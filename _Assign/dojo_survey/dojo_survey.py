# /usr/bin/python3
# coding=utf-8

import re
from flask import Flask, render_template, request, redirect, session, flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecretly'

@app.route('/')
def index():
    return render_template("log.html")

@app.route('/log_post', methods=['post'])
def log_post():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']

    Len = len(request.form['name'])
    if Len < 1: flash("Name can not be blank! ", 'name')
    elif Len <= 3: flash("Name must be 3+ characters! ", 'name')
    else:
        Len = len(request.form['comment'])
        if Len < 1:  flash("Comment can not be blank! ", 'comment')
        elif Len > 100: flash("Comment must be less than 100 characters! ", 'comment')
        else: return render_template("info.html")
    return redirect("/")

if __name__=="__main__":
    app.run()
