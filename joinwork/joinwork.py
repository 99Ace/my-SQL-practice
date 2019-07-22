from flask import Flask, render_template, request, redirect
import os
import pymysql

connection = pymysql.connect(
    host='localhost', # IP address of the database; localhost means "the local machine"
    user="admin@localhost",  #the mysql user
    password="password", #the password for the user
    database="northwind" #the name of database we want to use
)

app = Flask(__name__)

@app.route('/')
def index():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM Suppliers"
    cursor.execute(sql)
    results = []
    for r in cursor:
        results.append(r)
    return render_template("northwind.html", data = results)
    
@app.route('/create/supplier')
def goto_enter_supplier():
    return render_template("newsupplier.html")
    
@app.route('/create/supplier', methods=['POST'])
def create_supplier():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    companyName = request.form.get('companyName')
    contactName =request.form.get('contactName')
    contactTitle=request.form.get('contactTitle')
    
    print(companyName + contactName + contactTitle)
    
    sql = "INSERT INTO Suppliers (CompanyName, ContactName, ContactTitle) VALUES (%s, %s, %s)"
    
    cursor.execute(sql, [companyName, contactName, contactTitle])
    connection.commit()
    return redirect("northwind.html")
    
@app.route('/edit/supplier')
def goto_edit_supplier():
    return ('linked')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)