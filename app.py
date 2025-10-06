import json
from flask import Flask, render_template, request, redirect, session
from db import Database
import api

app = Flask(__name__)
app.secret_key = "my_secret_key"

dbo = Database()

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('username')
    email = request.form.get('useremail')
    password = request.form.get('userpassword')

    if not all([name, email, password]):
        return "Please fill all fields!"

    response = dbo.insert(name, email, password)
    if response:
        return render_template("login.html", message="Registration Successful. Kindly login to proceed.")
    else:
        return render_template("register.html", message="Email already exists.")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('useremail')
    password = request.form.get('userpassword')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile')
def profile():
    if 'logged_in' in session:
        return render_template('profile.html', user=session.get('user'))
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if 'logged_in' in session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    if 'logged_in' in session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)
        return render_template("ner.html", response=response)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5003)
