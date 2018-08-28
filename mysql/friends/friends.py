
from flask import Flask, render_template, request, redirect, session, flash
from openmysqldb import OpenMySqlDb

app = Flask(__name__)
app.secret_key = 'ThisIsSecretly'

def add_db():
    mysql = OpenMySqlDb("friendsdb")
    mysql.query_db( "insert into friends (first_name, last_name, occupation, created_at, updated_at) "
                 +  "value ('" + session['first_name'] + "','" + session['last_name'] + "','" + session['occupation'] + "','2018-01-01','2018-02-02');" )
    mysql.close()

@app.route('/')
def friends():
    mysql = OpenMySqlDb("friendsdb")
    all_friends = mysql.query_db("Select first_name, last_name, occupation from friends;")
    mysql.close()
    return render_template("friends.html", friends=all_friends)

@app.route('/friends_post', methods=['post'])
def friends_post():
    print(request.form)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['occupation'] = request.form['occupation']

    i=0;
    if len(session['first_name'])==0: i=1;
    elif len(session['last_name'])==0: i=1;
    elif len(session['occupation'])==0: i=1;
    if i==1: flash("Required no empty!")
    else:
        add_db()
        session.clear()

    return redirect('/')

if __name__=="__main__":
    app.run()
