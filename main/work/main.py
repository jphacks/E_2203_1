from flask import Flask, request, jsonify
import pandas as pd
import mysql.connector as mydb
from main.work.db import SelectOne, insert, dbinit
import pickle

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
datas = [
            {'id': 0, 'temp':30, 'month':7}
]
i = 0
rank = []

dbinit()

@app.route('/datas/all', methods=['GET'])
def model_a():
    json = request.get_json()
    
    id = json['id']
    temp = json['temp']
    month = json['month']

    #id = -1がきたら新しいIDをつける
    if id == -1:
        id = i + 1

    data = {"id": id, "temp": temp, 'month':month}
    datas.append(data)

    df_A = pd.json_normalize(datas)

    rank.append(model_A(df))

    #dfでdbからとってくる
    df_B = SelectOne()

    rank.append(model_B(df))

    #重複ないか調べる
    return rank


@app.route('/datas', methods=['POST'])
def post_json():
    json = request.get_json()

    #パースする
    menu = json['menu']
    id = json['id']
    temp = json['temp']
    month = json['month']



    if id == -1:
        id = i + 1

    data = {"menu": menu, "id": id, "temp": temp, 'month':month}
    #datas.append(data)

    insert (menu, id, temp, month)

    return jsonify(data)

@app.route('/pickle', methods=['POST'])
def post_pickle():
    
    return 


if __name__ == '__main__':
    app.run()

