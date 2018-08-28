# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<par>')
def pg_par(par):
    users = (
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    )
    return render_template('pg_par.html', myusers=users)

if __name__ == '__main__':
    app.run()