from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/dashboard')

#<---- DASHBOARD ---->
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login_registration():
    return render_template('login_reg.html')


# <---- PROPERTIES PAGE ---->
@app.route('/properties')
def properties():
    return render_template('properties.html')


# <---- PROPERTIES PAGE ---->
@app.route('/tenants')
def tenants():
    return render_template('tenants.html')