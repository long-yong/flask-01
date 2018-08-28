# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pg1')
def pg_1():
    return render_template('pg_1.html')

@app.route('/<par>')
def pg_par(par):
    return render_template('pg_par.html', mypar=par)

if __name__ == '__main__':
    app.run()