from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model.property import Property
from flask_app.model.tenant import Tenant
from flask import flash
from flask_app import app
import re

class Prop_has_tenant:
    db ='beyond_re'

    def __init__(self, data):
        self.property_id = data['property_id']  
        self.tenant_id = data['tenant_id']  
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']