import mysql.connector as mydb

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
    cur.execute("INSERT INTO test_table(id, name, price) VALUES (%d, %s, %d);")
    seqs = [
        (id, name, price)
    ]

def SelectAll ():
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_table ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)



