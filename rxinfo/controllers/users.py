from rxinfo import DB
from flask import (Blueprint, flash, g, redirect, render_template, request, url_for,jsonify,session)
from rxinfo.decorator import login_required,authorize
from rxinfo.forms import PatientForm
from rxinfo.models.model import Patient
user = Blueprint('users', __name__, url_prefix='/user')

@user.route('/add', methods=['GET','POST'])
@login_required
def add_user():
  form = PatientForm()
  if request.method == 'POST':
    if form.validate_on_submit():  
      patient = Patient(
                first_name = request.form['first_name'],
                last_name = request.form['last_name'],
                email = request.form['email'],
                date_of_birth = request.form['date_of_birth'],
                gender = request.form['gender'],
                age = request.form['age'],
              ) 
      DB.session.add(patient)
      DB.session.commit()        
      flash('Patient has been added successfully.','success')
      return redirect(url_for('users.add_user'))      
    else:
        return render_template('user_management/add.html', form=form)          
  else:
    return render_template('user_management/add.html',form=form)