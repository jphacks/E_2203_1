import mysql.connector as mydb
import json
import pandas as pd
from make_model.work.model_c import engine

# コネクションの作成
conn = mydb.connect(
    host='127.0.0.1',
    port='3306',
    user='user',
    password='pass',
    database='db'
)

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())

def dbinit():
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS `test_table`")
    cur.execute("""CREATE TABLE IF NOT EXISTS `test_table` (
    `id` int(11) NOT NULL,
    `state` int(11) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

def insert(menu, id, temp, month):
    cur = conn.cursor()
    records = [
    (menu, id, temp, month)
    ]
    cur.executemany("INSERT INTO test_table VALUES (%s, %s, %s, %s)", records)

#SelectAll多分使わない
def SelectAll ():
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM test_table")
    rows = cur.fetchall()

    data_all = []
    
    for row in rows:
        json.dumps(row)
        data_all.append(row)

    return data_all

def SelectOne (id):
    query = "select from test_table where id = {%s}", id  #変数いれたい
    df = pd.read_sql(query,con = engine)
    return df


