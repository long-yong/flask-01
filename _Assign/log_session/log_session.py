# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecretly'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/log_post', methods=['post'])
def log_post():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/log')

if __name__=="__main__":
    app.run()
