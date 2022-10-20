from datetime import timedelta
from flask import Flask, request, jsonify, session
import pickle
# import pandas as pd
# import mysql.connector as mydb
# from main.work.db import SelectOne, insert, dbinit

app = Flask(__name__)
app.secret_key = "secret"
app.permanent_session_lifetime = timedelta(days=5)

# app.config['JSON_AS_ASCII'] = False
# datas = [
#             {'id': 0, 'temp':30, 'month':7}
# ]
# i = 0
# rank = []


# @app.route('/datas/all', methods=['GET'])
# def model_a():
#     json = request.get_json()
    
#     id = json['id']
#     temp = json['temp']
#     month = json['month']

#     #id = -1がきたら新しいIDをつける
#     if id == -1:
#         id = i + 1

#     data = {"id": id, "temp": temp, 'month':month}
#     datas.append(data)

#     df_A = pd.json_normalize(datas)

#     rank.append(model_A(df))

#     #dfでdbからとってくる
#     df_B = SelectOne()

#     rank.append(model_B(df))

#     #重複ないか調べる
#     return rank


# @app.route('/datas', methods=['POST'])
# def post_json():
#     json = request.get_json()

#     #パースする
#     menu = json['menu']
#     id = json['id']
#     temp = json['temp']
#     month = json['month']



#     if id == -1:
#         id = i + 1

#     data = {"menu": menu, "id": id, "temp": temp, 'month':month}
#     #datas.append(data)

#     insert (menu, id, temp, month)

#     return jsonify(data)

@app.route('/model', methods=['POST'])
def post_pickle():
    model = pickle.loads(request.get_data())
    session["model"] = model
    return jsonify({'massage': 'OK'}), 200


if __name__ == '__main__':
    # dbinit()
    app.run(host="0.0.0.0", port=80, debug=True)
