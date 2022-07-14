from functools import wraps
from flask import g, request, redirect, url_for,session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['AuthUser'] is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['AuthUser']:
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function