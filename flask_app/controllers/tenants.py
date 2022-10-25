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

#<---- ROUTES TO THE EDIT PAGE ---->
@app.route('/tenants/edit/<int:tenant_id>/<int:property_id>')
def edit_tenant(tenant_id, property_id):
    if 'user_id' not in session: 
        return redirect('/login')
    
    data ={
        'tenant_id': tenant_id,
        'property_id': property_id
    }

    property_id = data['property_id']
    properties = Tenant.get_one(data)
    
    return render_template('properties.html', property_id=property_id, properties=properties)

#<---- UPDATED THE TENANT IN DB ---->
@app.route('/tenants/update/<int:tenant_id>', methods=['POST'])
def tenant_update(tenant_id):

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
        'tenant_id': tenant_id 
    }

    # show_validation = Show.validate_show(data)
    # if not show_validation:
    #     return redirect(f'/shows/edit/{id}')
    Tenant.update(data)
    return redirect('/tenants')


#<---- DELETE TENANT FROM DB ---->
@app.route('/tenants/delete/<int:tenant_id>/<int:property_id>')

def delete_tenant(tenant_id, property_id):
    data ={
        'tenant_id': tenant_id,
        'property_id': property_id
    }
    Tenant.delete(data)
    return redirect('/tenants')