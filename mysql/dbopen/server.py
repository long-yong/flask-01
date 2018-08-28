
from flask import Flask, render_template, request, redirect
from openmysqldb import OpenMySqlDb

mysql = OpenMySqlDb("friendsdb")
print(mysql.query_db("Select * from friends;"))
mysql.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("log.html")

@app.route('/log_post', methods=['post'])
def log_post():
    print(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run()
