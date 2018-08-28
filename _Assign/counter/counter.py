# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


def counter_add(n):
    if 'counter' in session:
        n += int(session['counter'])
    session['counter'] = str(n)


@app.route('/')
def counter():
    counter_add(1)
    return render_template("counter.html")

@app.route('/counter_post/<num>', methods=['post'])
def counter_post(num):
    if num == '0': session.pop('counter', None)
    else: counter_add(1)
    return redirect("/")

if __name__=="__main__":
    app.run()

