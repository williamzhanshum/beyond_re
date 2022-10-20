from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.property import Property
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/dashboard')

# <---- LOGIN/REG PAGE ----> 
@app.route('/login')
def login_registration():
    return render_template('login_reg.html')

# <----- Route will do REGISTRATION INPUT VALIDATION-----> 
@app.route('/register', methods=['POST'])
def register():
    # Will check the the registration inputs are correct format 
    if not User.validate_user(request.form):
        return redirect('/login')

    #This will hash the password after it gets validated. 
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }

    user_id = User.save(data)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']

    return redirect('/dashboard')

# <----- Route to LOGIN VALIDATION ----->
@app.route('/login', methods=['POST'])
def login():
    data = { "email": request.form['email']}
    
    user_in_db = User.validate_login(data)

    if not user_in_db:
        flash("Invalid Email or Password", 'login-error')
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email or Password', 'login-error')
        return redirect('/login')
    
    #if the passwords match, set the user_id into session 
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect('/dashboard')

#<---- DASHBOARD ---->
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# <---- TENANTS PAGE ---->
@app.route('/tenants')
def tenants():
    return render_template('tenants.html')

#<---- VENDORS PAGE ----> 
@app.route('/vendors')
def vendors():
    return render_template('vendors.html')