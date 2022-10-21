from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.vendor import Vendor

#<---- VENDORS PAGE ----> 
@app.route('/vendors')
def vendors():
    if 'user_id' not in session: 
        return redirect('/login')

    vendors = Vendor.get_all()
    return render_template('vendors.html', vendors=vendors)

#<---- SAVES NEW PROPERTY TO DB ---->
@app.route('/vendors/create', methods=['POST'])
def create_vendor():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'phone_num': request.form['phone_num'],
        'email': request.form['email'],
        'web_link': request.form['web_link'],
        'social_link': request.form['social_link'],
        'company_name': request.form['company_name'], 
        'user_id': session['user_id']
    }
    # recipe_validation = Recipe.validate_recipe(data)
    # if not recipe_validation:
    #     return redirect('/recipes/new')

    Vendor.save(data)
    return redirect('/vendors')

#<---- ROUTES TO THE EDIT PAGE ---->
@app.route('/vendors/edit/<int:id>')
def edit_vendor(id):
    if 'user_id' not in session: 
        return redirect('/login')
    
    data = {
        'id': id
    }

    vendor_id = data['id']
    vendors = Vendor.get_one(data)
    
    return render_template('vendors.html', vendor_id=vendor_id, vendors=vendors)

#<---- UPDATED THE SHOW IN DB ---->
@app.route('/vendors/update/<int:id>', methods=['POST'])
def vendor_update(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'phone_num': request.form['phone_num'],
        'email': request.form['email'],
        'web_link': request.form['web_link'],
        'social_link': request.form['social_link'],
        'company_name': request.form['company_name'], 
    }

    # show_validation = Show.validate_show(data)
    # if not show_validation:
    #     return redirect(f'/shows/edit/{id}')
    Vendor.update(data)
    return redirect('/vendors')


#<---- DELETE PROPERTY FROM DB ---->
@app.route('/vendors/delete/<int:id>')
def delete_vendor(id):
    data ={
        'id': id
    }
    Vendor.delete(data)
    return redirect('/vendors')