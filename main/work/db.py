import mysql.connector as mydb
import sqlalchemy as sa
import pandas as pd

# コネクションの作成
conn = mydb.connect(
    host='jp-mysql',
    port='3306',
    user='root',
    password='pass',
    database='jp-db')

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

url = 'mysql+pymysql://user:pass@localhost:3306/db?charset=utf8'
engine = sa.create_engine(url, echo=False)


def make_df(user_id):
    query = f"select * from situations where user_id = {user_id}"
    df = pd.read_sql(query, con=engine)

    return df


def insert(user_id, month, temp, latitude, longitude, time, dish_id):
    cur = conn.cursor()
    # (id, month, steps, temp, latitude, longitude, time, dish_id)
    sql = ("INSERT INTO situations (user_id, month, temperature, latitude, longitude, time_hour, dish_id)VALUES (%s, %s, %s, %s, %s, %s, %s)")

    cur.execute(sql, (user_id, month, temp, latitude, longitude, time, dish_id))

    conn.commit()

def select_dish() -> dict:
    menu = {}
    cur = conn.cursor()
    cur.execute("select * from dish")
    rows = cur.fetchall()

    for row in rows:
        menu[row[0]] = row[1]

    return menu
