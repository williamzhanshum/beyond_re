from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re
 
# Not sure why it worked after commenting this out. 
# from flask_bcrypt import Bcyrpt 
# bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db ='beyond_re'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name'] 
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# <----- VALIDATING REGISTRATION INPUT -----> 
    @staticmethod
    def validate_user(user):
        data = {
            'email': user['email']
        }
        is_valid = True
        #checking to see if the user is already in the db
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.", 'input-error')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email! ", 'input-error')
            is_valid=False
        if len(user['first_name']) < 2: 
            flash("First name must be at least 2 characters.", 'input-error')
            is_valid=False
        if len(user['last_name']) < 2: 
            flash("Last name must be at least 2 characters.", 'input-error')
            is_valid=False
        if len(user['password']) < 8:
            flash("Password must be at least 8 charachters long.", 'input-error')
            is_valid=False
        if (user['password'] != user['confirm_password']):
            flash("Psssword must match!", 'input-error')
            is_valid=False
        return is_valid

# <----- Validate Login Inputs -----> 
    @classmethod
    def validate_login(cls,data):
        # is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(User.db).query_db(query,data)
        print(f"Results: {results}")
        
        if len(results) < 1:
            return None
        return cls(results[0])