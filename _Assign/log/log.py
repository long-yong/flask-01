# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    # return redirect('/log')
    return render_template("index.html")

@app.route('/log')
def log():
    return render_template("log.html")

@app.route('/log/<par>')
def log_par(par):
    return render_template("log.html", mypar=par)

@app.route('/log_post', methods=['post'])
def log_post():
    print(request.form)
    return render_template('/log_post.html', post=request.form)

if __name__=="__main__":
    app.run()
