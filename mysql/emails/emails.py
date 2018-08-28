
import time
from flask import Flask, render_template, request, redirect, session, flash
from openmysqldb import *

app = Flask(__name__)
app.secret_key = 'ThisIsSecretly'

def save_email(email):
    mysql = OpenMySqlDb("friendsdb")
    qryres = mysql.query_db("Select email,create_at from emails;")
    arr = arr_from_qry(qryres,1)
    if email in arr:
        flash("This email has existed!", "email")
        mysql.close()
        return None
    timestr = time.strftime("%m/%d/%y %I:%M%p", time.localtime());
    sql = "Insert into emails (email,create_at) values ('" +email+ "','" +timestr+ "');";
    
    mysql.query_db(sql)

    mysql.query_db("commit")

    qryres = mysql.query_db("Select email,create_at from emails;")
    arr = arr_from_qry(qryres, 1)
    dict = dict_from_arr(arr)
    mysql.close()
    return dict

@app.route('/')
def emails():
    return render_template("emails.html")

@app.route('/emails_post', methods=['post'])
def emails_post():
    email = request.form['email']
    session['email'] = email
    if checkEmail(email) != True: return redirect('/')
    else:
        dict = save_email(request.form['email'])
        if(dict == None): return redirect('/')
        else: return render_template("email_list.html", mydict=dict, myemail=email)

if __name__=="__main__":
    app.run()


