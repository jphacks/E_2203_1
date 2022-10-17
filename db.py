import mysql.connector as mydb
import json

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
    `name` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` int(11) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

def insert(id, name, price):
    cur = conn.cursor()
    records = [
    (id, name, price)
    ]
    cur.executemany("INSERT INTO test_table VALUES (%s, %s, %s)", records)

def SelectAll ():
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM test_table")
    rows = cur.fetchall()

    data_all = []
    for row in rows:
        json.dumps(row)
        data_all.append(row)

    return data_all


