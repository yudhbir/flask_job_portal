from rxinfo import app
from rxinfo import db
from flask import (Blueprint, flash, g, redirect, render_template, request, url_for,jsonify,session)
from werkzeug.security import generate_password_hash, check_password_hash
# from rxinfo.auth import login_required
from rxinfo.decorator import login_required,authorize
from rxinfo.forms import LoginForm
user = Blueprint('users', __name__, url_prefix='/user')

@user.route('/edit', methods=['GET'])
def add_user():
  return render_template('user_management/add.html')