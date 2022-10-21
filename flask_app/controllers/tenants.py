from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.tenant import Tenant
from flask_app.models.property import Property

# <---- TENANTS PAGE ---->
@app.route('/tenants')
def tenants():
    if 'user_id' not in session: 
        return redirect('/login')
    
    tenants = Tenant.get_all()
    properties = Property.get_all()
    return render_template('tenants.html', tenants=tenants, properties=properties)

#<---- SAVES NEW TENANTS TO DB ---->
@app.route('/tenants/create', methods=['POST'])
def create_tenant():

    # print("HERE IS PROPERTY ID")
    # print(request.form['property'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'primary_phone': request.form['primary_phone'],
        'secondary_phone': request.form['secondary_phone'],
        'email': request.form['email'],
        'dob': request.form['dob'],
        'gender': request.form['gender'], 
        'tenant_img': request.form['tenant_img'],
        'property_id': request.form['property_id'],
    }

    # recipe_validation = Recipe.validate_recipe(data)
    # if not recipe_validation:
    #     return redirect('/recipes/new')

    Tenant.save(data)
    return redirect('/tenants')