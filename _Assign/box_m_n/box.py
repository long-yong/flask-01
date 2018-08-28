# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<num>')
def play_num(num):
    return render_template('play_num.html', mynum=int(num))

@app.route('/play/<num>/<color>')
def play_num_color(num, color):
    return render_template('play_num_color.html', mynum=int(num), mycolor=color)

if __name__ == '__main__':
    app.run()