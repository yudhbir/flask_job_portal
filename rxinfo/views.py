from rxinfo import app
from rxinfo import db
from flask import (Blueprint, flash, g, redirect, render_template, request, url_for,jsonify,session)
from werkzeug.security import generate_password_hash, check_password_hash
# from rxinfo.auth import login_required
from rxinfo.decorator import login_required,authorize
from rxinfo.forms import LoginForm

@app.route('/', methods=['GET'])
def index_page():
  return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
@authorize
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form['email']
            password = request.form['password']
            cursor = db.cursor(dictionary=True)    
            cursor.execute("SELECT * FROM tbl_users WHERE email=%s", (email,))
            user = cursor.fetchone() 
            print(user)   
            if user and check_password_hash(user['password'], password):
                user['isloggedin']='true'
                session['AuthUser'] = user
                return redirect(url_for('dashboard'))
            else:
                flash('You are valid user. Please check.','error')
                return redirect(url_for('login'))
        else:
            return render_template('users/login.html', form=form)          
    else:
        return render_template('users/login.html',form=form)

@app.route('/register', methods=['GET', 'POST'])
@authorize
def register():
    if request.method == 'POST':        
        # print(request.form)
        fullname = request.form['full_name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        # print(password)
        cursor = db.cursor()
        cursor.execute("INSERT INTO tbl_users (full_name,email,password) VALUES (%s,%s,%s)",(fullname,email,password))
        db.commit()
        flash('You are successfully registered. Please login.','success')
        return redirect(url_for('login'))
    else:
        return render_template('users/register.html')

@app.route('/forgot/password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':        
        print(request.args)
    else:
        return render_template('users/forgot_password.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session['AuthUser']=None
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    cursor = db.cursor(dictionary=True)
    cursor.execute(''' select * FROM tbl_users order by id desc limit 10 ''')
    records =cursor.fetchall()    
    return render_template('user_management/index.html', users=records)
    # return jsonify(records)