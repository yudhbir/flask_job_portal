from flask import Flask
from mysql.connector import (connection)

app = Flask(__name__)

db = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='db_sandbox3')

import rxinfo.views

if __name__ == '__main__':
    app.run(debug=True)