from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.property import Property
from flask_app.models.user import User # might not need these
from flask_app.controllers import users # might not need these 

# <---- PROPERTIES PAGE ---->
@app.route('/properties')
def properties():
    if 'user_id' not in session: 
        return redirect('/')

    properties = Property.get_all()
    return render_template('properties.html', properties=properties)

#<---- SAVES NEW PROPERTY TO DB ---->
@app.route('/properties/create', methods=['POST'])
def create_property():
    data = {
        'address': request.form['address'],
        'address_2': request.form['address_2'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip_code': request.form['zip_code'],
        'tenant_occ': request.form['tenant_occ'],
        'property_img': request.form['property_img'], 
        'user_id': session['user_id']
    }
    # recipe_validation = Recipe.validate_recipe(data)
    # if not recipe_validation:
    #     return redirect('/recipes/new')

    Property.save(data)
    return redirect('/properties')

#<---- ROUTES TO THE EDIT PAGE ---->
@app.route('/properties/edit/<int:id>')
def edit_property(id):
    if 'user_id' not in session: 
        return redirect('/login')
    
    data = {
        'id': id
    }

    property_id = data['id']
    properties = Property.get_one(data)
    
    print('------- LOOK BELOW -------')
    print(property_id, properties)
    
    return render_template('properties.html', property_id=property_id, properties=properties)

#<---- UPDATED THE SHOW IN DB ---->
@app.route('/properties/update/<int:id>', methods=['POST'])
def property_update(id):
    data = {
        'id': id,
        'address': request.form['address'],
        'address_2': request.form['address_2'],
        'city': request.form['city'], 
        'state': request.form['state'], 
        'zip_code': request.form['zip_code'],
        'tenant_occ': request.form['tenant_occ'],
        'property_img': request.form['property_img'],
    }

    # show_validation = Show.validate_show(data)
    # if not show_validation:
    #     return redirect(f'/shows/edit/{id}')
    print('YOU ARE HERE')
    Property.update(data)
    return redirect('/properties')


#<---- DELETE PROPERTY FROM DB ---->
@app.route('/properties/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    Property.delete(data)
    return redirect('/properties')