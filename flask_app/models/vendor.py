from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re

class Vendor: 
    db ='beyond_re'

    def __init__(self, data):
        self.id = data['id'] 
        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.phone_num = data['phone_num'] 
        self.email = data['email'] 
        self.web_link = data['web_link'] 
        self.social_link = data['social_link'] 
        self.company_name = data['company_name'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# <----- GRABS ALL THE VENDORS-----> 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM vendors LEFT JOIN users on vendors.user_id = users.id;"
        #results returns a list of dictionarites with the data form the table in the db
        results = connectToMySQL(cls.db).query_db(query)
        vendors = []

        for vendor in results:
            vendors.append(cls(vendor))
        return vendors

# <----- GET ONE VENDOR BY ID-----> 
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM vendors LEFT JOIN users on users.id = vendors.user_id  WHERE vendors.id=%(id)s"

        # result is an array of dictionaries. 
        results = connectToMySQL(cls.db).query_db(query,data)
        vendors = []

        for vendor in results:
            vendors.append(cls(vendor))
        return vendors 

# <----- SAVES VENDOR INTO DB-----> 
    @classmethod 
    def save(cls,data):

        query = "INSERT INTO vendors (first_name, last_name, phone_num, email, web_link, social_link, company_name, created_at, updated_at, user_id) VALUES (%(first_name)s, %(last_name)s, %(phone_num)s, %(email)s, %(web_link)s, %(social_link)s, %(company_name)s, NOW(), NOW(), %(user_id)s);"

        return connectToMySQL(cls.db).query_db(query, data)

# <----- UPDATES VENDOR IN DB-----> 
    @classmethod
    def update(cls,data):
        query = "UPDATE vendors SET first_name=%(first_name)s, last_name=%(last_name)s, phone_num=%(phone_num)s, email=%(email)s, web_link=%(web_link)s, social_link=%(social_link)s, company_name=%(company_name)s, updated_at=NOW() WHERE id=%(id)s;"

        return connectToMySQL(cls.db).query_db(query,data)

# <----- DELETES VENDORS BY ID FROM DB -----> 
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM vendors WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)