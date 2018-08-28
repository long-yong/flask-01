# /usr/bin/python3
# coding=utf-8

from random import randint
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def check_session():
    if 'guess' not in session:
        session['guess'] = str(randint(1, 100))

@app.route('/')
def great_number():
    check_session()
    return render_template("great_number.html")

@app.route('/great_number_post', methods=['post'])
def great_number_post():
    session.pop('guess', None)
    return redirect("/")

if __name__=="__main__":
    app.run()

