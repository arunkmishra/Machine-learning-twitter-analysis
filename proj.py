from flask import Flask
from Tweet_Classification import predict
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
import sqlite3
 
app = Flask(__name__)
nda = "nd"

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return client() 
 
@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pas =  request.form['password']
    db = sqlite3.connect("test.db")
    c = db.cursor()
    c.execute("SELECT * from dost WHERE username = ? AND password = ?",(user,pas))
    if (len(list(c)) > 0):
        cs = db.execute("select name from dost where username = ?",(user))
        for row in cs:
            name = row[0]
            session['username']= name
            session['logged_in'] = True
            return render_template("home.html",usern = session['username'])
    else:
        msg = "Login failed"
        return render_template("re.html",msg = msg)
    db.close()
        

@app.route("/logout")
def logout():
    session.clear()
    session["__invalidate__"] = True
    return home()

@app.route("/entry")
def entry():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("entry.html")

@app.route("/")
def hom():
    return render_template("home.html")

@app.route("/ml")
def ml():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("ml.html")

@app.route('/analyse', methods=['POST','GET'])
def analyse():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        inp = request.form['texta']
        result = predict([inp])
        output = result[0]
        return render_template("analyse.html",result = output ,one = inp)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/reg",methods=['POST'])
def reg():
    if request.method == 'POST':
        try:
            username = request.form['username']
            name = request.form['name']
            password = request.form['password']
            age = request.form['age']
            dob = request.form['dob']

            with sqlite3.connect("test.db") as conn:
                cur = conn.cursor()
                conn.execute("insert into dost(username,name,age,password,dob) values (?,?,?,?,?)",(username,name,age,password,dob));
                conn.commit()
                msg = "record added successfuly"
        except:
            conn.rollback()
            msg = "error in insert operation "
        finally:
            return render_template("re.html",msg = msg)
            conn.close()

@app.route('/client')
def client():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('client.html')

@app.route('/first')
def first():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('first.html')

@app.route('/second')
def second():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('second.html')

@app.route('/third')
def third():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('third.html')

@app.route('/fourth')
def fourth():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('fourth.html')

@app.route('/about')
def about():
    return render_template('xyz.html')
                            
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
