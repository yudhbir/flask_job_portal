from rxinfo import app
from rxinfo import db
from flask import jsonify
from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
# from werkzeug.exceptions import abort
# from rxinfo.auth import login_required


@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute(''' select * FROM users order by id desc limit 10 ''')
    records = cursor.fetchall()
    return render_template('users/index.html', users=records)
    # return jsonify(records)