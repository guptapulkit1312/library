from app import app
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/login')
def index():
    return render_template("login.html", title='Login')

@app.route('/Register')
def register():
    return render_template("form.html", title='Register')

@app.route('/Sign-Up')
def signup():
    return render_template("signup.html", title='Sign-Up')
