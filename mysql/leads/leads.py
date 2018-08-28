
from flask import Flask, render_template, request, redirect, session, flash
from openmysqldb import *

app = Flask(__name__)
app.secret_key = 'ThisIsSecretly'

@app.route('/')
def leads():
    mysql = OpenMySqlDb("friendsdb")
    qryres = mysql.query_db("Select name,lead_number from leads;")
    mysql.close()
    arr = arr_from_qry(qryres, 1)
    dict0 = dict_from_arr(arr)
    dict1 = dict_from_arr(arr_with_percetage(arr))
    return render_template("leads.html", mydict0=dict0, mydict1=dict1)

@app.route('/leads_post', methods=['post'])
def leads_post():
    return redirect('/')

if __name__=="__main__":
    app.run()


