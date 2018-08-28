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
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['name']) <= 3:
        flash("Name must be 3+ characters", 'name')

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')

    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!", 'comment')
    elif len(request.form['comment']) > 100:
        flash("Comment must be less than 100 characters", 'comment')

    if '_flashes' not in session.keys():
        flash("Success !")

    return redirect("/")

if __name__=="__main__":
    app.run()
