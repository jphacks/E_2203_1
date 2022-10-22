import mysql.connector as mydb
import json
#import pandas as pd
#from make_model.work.send_model import engine

# コネクションの作成
conn = mydb.connect(
    host='jp-mysql',
    port='3306',
    user='root',
    password='pass',
    database='jp-db')

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

print(conn.is_connected())

def Insert(id, month, steps, temp, latitude, longitude, time, dish_id):
    cur = conn.cursor()
    # (id, month, steps, temp, latitude, longitude, time, dish_id)
    sql = ("INSERT INTO state (id, month, steps, temprature, latitude, longitude, time_hour, dish_id)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    cur.execute(sql, (id, month, steps, temp, latitude, longitude, time, dish_id))

    conn.commit()

# def Dish_Insert(id, month):
#     cur = conn.cursor()
#     # (id, month, steps, temp, latitude, longitude, time, dish_id)
#     sql = ("INSERT INTO dish (id, dish)VALUES (%s, %s)")

#     cur.execute(sql, (id, month))

#     conn.commit()

def Select_user(userid):
    data_history= []
    cur = conn.cursor()
    cur.executemany("select from state where userid = (%s)", (userid))
    rows = cur.fetchall()

    for row in rows:
        json.dumps(row)
        data_history.append(row)
    return data_history


def Select_dish(dish_id):
    menu = []
    cur = conn.cursor()
    cur.executemany("select from dish where id = (%s)", (dish_id))
    rows = cur.fetchall()

    for row in rows:
        menu = json.dumps(row)
    return menu


