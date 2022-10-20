from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re

class Property: 
    db ='beyond_re'

    def __init__(self, data):
        self.id = data['id'] 
        self.address = data['address'] 
        self.address_2 = data['address_2'] 
        self.city = data['city'] 
        self.state = data['state'] 
        self.zip_code = data['zip_code'] 
        self.tenant_occ = data['tenant_occ'] 
        self.property_img = data['property_img'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# <----- GRABS ALL THE PROPERTIES-----> 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM properties LEFT JOIN users on properties.user_id = users.id;"
        #results returns a list of dictionarites with the data form the table in the db
        results = connectToMySQL(cls.db).query_db(query)
        properties = []

        for one_property in results:
            properties.append(cls(one_property))
        return properties

# <----- GET ONE PROPERTY BY ID-----> 
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM properties LEFT JOIN users on users.id = properties.user_id  WHERE properties.id=%(id)s"

        # result is an array of dictionaries. 
        results = connectToMySQL(cls.db).query_db(query,data)
        properties = []

        for one_property in results:
            properties.append(cls(one_property))
        return properties 

# <----- UPDATES SHOW IN DB-----> 
    @classmethod
    def update(cls,data):
        query = "UPDATE properties SET address=%(address)s, address_2=%(address_2)s, city=%(city)s, state=%(state)s, zip_code=%(zip_code)s, tenant_occ=%(tenant_occ)s, property_img=%(property_img)s, updated_at=NOW() WHERE id=%(id)s;"

        return connectToMySQL(cls.db).query_db(query,data)

# <----- SAVES RECIPE INTO DB-----> 
    @classmethod 
    def save(cls,data):

        query = "INSERT INTO properties (address, address_2, city, state, zip_code, tenant_occ, property_img, created_at, updated_at, user_id) VALUES (%(address)s, %(address_2)s, %(city)s, %(state)s, %(zip_code)s, %(tenant_occ)s, %(property_img)s, NOW(), NOW(), %(user_id)s);"

        return connectToMySQL(cls.db).query_db(query, data)

# <----- DELETES RECIPE BY ID FROM DB -----> 
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM properties WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)