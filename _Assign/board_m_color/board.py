# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    rows = 8
    cols = 8
    return render_template('index.html', myrows=rows, mycols=cols)

@app.route('/play/<rows>/<cols>')
def board(rows, cols):
    rows = int(rows)
    cols = int(cols)
    return render_template('index.html', myrows=rows, mycols=cols)

if __name__ == '__main__':
    app.run()