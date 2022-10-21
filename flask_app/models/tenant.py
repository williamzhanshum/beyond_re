from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re

class Tenant: 
    db ='beyond_re'

    def __init__(self, data):
        self.id = data['id'] 
        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.primary_phone = data['primary_phone'] 
        self.secondary_phone = data['secondary_phone'] 
        self.email = data['email'] 
        self.dob = data['dob'] 
        self.gender = data['gender'] 
        self.tenant_img = data['tenant_img'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.property_id = data['property_id']
        self.tenant_id = data['tenant_id']
        self.address = data['address']
        self.user_id = int(data['user_id'])


# <----- GRABS ALL THE TENANTS-----> 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM property_has_tenant LEFT JOIN properties on properties.id = property_has_tenant.property_id LEFT JOIN tenants ON property_has_tenant.tenant_id = tenants.id WHERE user_id = user_id"
        #results returns a list of dictionarites with the data form the table in the db
        results = connectToMySQL(cls.db).query_db(query)
        tenants = []
        
        for tenant in results:
            tenants.append(cls(tenant))
        return tenants

# <----- GET ONE TENANT BY ID-----> 
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM tenants LEFT JOIN users on users.id = tenants.user_id  WHERE tenants.id=%(id)s"

        # result is an array of dictionaries. 
        results = connectToMySQL(cls.db).query_db(query,data)
        tenants = []

        for tenant in results:
            tenants.append(cls(tenant))
        return tenants 

# <----- UPDATES TENANT IN DB-----> 
    @classmethod
    def update(cls,data):

        query = "UPDATE tenants SET (first_name, last_name, primary_phone, secondary_phone, email, dob, gender, tenant_img) VALUES (%(first_name)s, %(last_name)s, %(primary_phone)s, %(secondary_phone)s, %(email)s, %(dob)s, %(gender)s, %(tenant_img)s);"
        tenant_id = connectToMySQL(cls.db).query_db(query, data)

        data['tenant_id'] = tenant_id

        query2 = 'UPDATE property_has_tenant (property_id, tenant_id) VALUES (%(property_id)s, %(tenant_id)s);'
        
        return connectToMySQL(cls.db).query_db(query2,data)

# <----- SAVES TENANT INTO DB-----> 
    @classmethod 
    def save(cls,data):

        query = "INSERT INTO tenants (first_name, last_name, primary_phone, secondary_phone, email, dob, gender, tenant_img) VALUES (%(first_name)s, %(last_name)s, %(primary_phone)s, %(secondary_phone)s, %(email)s, %(dob)s, %(gender)s, %(tenant_img)s);"
        tenant_id = connectToMySQL(cls.db).query_db(query, data)

        data['tenant_id'] = tenant_id
        # query2= "INSERT INTO property_has_tenant (property_id, tenant_id) VALUES(%(property_id)s,%(tenant_id)s)"
        # connectToMySQL(cls.db).query_db(query2, data)

        query3 = 'INSERT INTO property_has_tenant (property_id, tenant_id) VALUES (%(property_id)s, %(tenant_id)s);'

        return connectToMySQL(cls.db).query_db(query3, data)

# <----- DELETES TENANT BY ID FROM DB -----> 
    @classmethod
    def delete(cls, data):
        # query = "DELETE FROM tenants WHERE id=%(id)s;"
        query = 'DELETE FROM property_has_tenant WHERE property_id = %(property_id)s and tenant_id= %(tenant_id)s;'
        return connectToMySQL(cls.db).query_db(query,data)