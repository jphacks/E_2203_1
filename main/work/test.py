from unittest import main
from flask import Flask
from sqlalchemy import create_engine

import os

app = Flask(__name__)

user_name = "root"
password = os.getenv("MYSQL_ROOT_PASSWORD")
host = "http://jp-mysql:3306"
db_name = "db"

engin = create_engine(f"mysql://{user_name}:{password}@{host}/{db_name}")

@app.route("/test")
def test():
    print("test")


if __name__ == "__main__":
    app.run(debug=True)