# /usr/bin/python3
# coding=utf-8

import time
from random import randint
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecretYonglong'

def add_gold(name, n0, n1):
    old = int(session['gold'])
    n0 = int(n0)
    n1 = int(n1)
    earn = randint(n0, n1)
    if old + earn < 0: earn = -old
    session['gold'] = str(old + earn)
    if (earn >= 0): addstr = 'Earns ' + str(earn) + ' gold from the ' + name
    else: addstr = 'Entered a casino and lost ' + str(-earn) + ' gold ... Ouch.'
    timestr =' (' + time.strftime("%Y/%m/%d %I:%M %p", time.localtime()) + ')'
    session['activities'] = addstr + timestr + '\r\n' + session['activities']

@app.route('/')
def gold():
    if 'gold' not in session:
        session['gold'] = '0'
        session['activities'] = ''
    return render_template("gold.html")

@app.route('/gold_post/<name>/<n0>/<n1>', methods=['post'])
def gold_post(name, n0, n1):
    add_gold(name, n0, n1)
    return redirect('/')

if __name__=="__main__":
    app.run()

