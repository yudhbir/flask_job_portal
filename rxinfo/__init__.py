from flask import Flask
from mysql.connector import (connection)
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = "dEsGtRsXOUxhsIfW$98468b08f2485b191db523219282ce75eca4a063ee68"
app.config['TESTING'] = True
app.config['DEBUG'] = True


db = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='db_stay_healthy')

csrf = CSRFProtect(app)

import rxinfo.views
from rxinfo.controllers.users import user
app.register_blueprint(user)

if __name__ == '__main__':
    app.run()