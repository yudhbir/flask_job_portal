from flask import (Blueprint, flash, g, redirect, render_template, request, url_for,jsonify,session)
from rxinfo.decorator import login_required,authorize
# from rxinfo.forms import LoginForm
user = Blueprint('users', __name__, url_prefix='/user')

@user.route('/add', methods=['GET','POST'])
def add_user():
  return render_template('user_management/add.html')