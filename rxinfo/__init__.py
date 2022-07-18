from flask import Flask
from mysql.connector import (connection)
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "dEsGtRsXOUxhsIfW$98468b08f2485b191db523219282ce75eca4a063ee68"
app.config['TESTING'] = True
app.config['DEBUG'] = True


db = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='db_stay_healthy')

# intergation of the SqlAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/db_stay_healthy'

DB2 = SQLAlchemy(app)

csrf = CSRFProtect(app)

import rxinfo.views
from rxinfo.controllers.users import user
app.register_blueprint(user)

if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0", port=8080)