from flask import Flask
from mysql.connector import (connection)

app = Flask(__name__)
app.secret_key = "dEsGtRsXOUxhsIfW$98468b08f2485b191db523219282ce75eca4a063ee68"

db = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='db_stay_healthy')

import rxinfo.views

if __name__ == '__main__':
    app.run(debug=True)