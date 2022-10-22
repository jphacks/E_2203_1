import pickle

import pandas as pd

from datetime import timedelta

from flask import Flask, request, jsonify, session

import db
import modelA
import modelB

app = Flask(__name__)
model_a = None
model_b = None
user = [1,2,3,4,5,6,7,8,9,10]


@app.route('/recommend', methods=['GET'])
def recommend():
    dish_list = db.select_dish()

    j_data = request.get_json()
    user_id: int = j_data['user_data']
    situation: pd.DataFrame = pd.DataFrame(j_data).drop('user_id')

    a_reco_list = model_a.pred(situation)

    user_df = db.make_df(user_id)
    b_reco_list = model_b.pred(user_df, situation)

    reco_list = list(set(a_reco_list + b_reco_list))

    return reco_list[:6]
    # for i in range(6):
    #     if len(reco_list) > 6:
    #         break
    #
    #     reco_list.append()


@app.route('/dish_list', methods=['GET'])
def dish_list():
    menu = db.select_dish()
    return jsonify(menu)


@app.route('/ate_dish', methods=['POST'])  # userがmenuを選んだあとにくるリクエスト
def post_json():
    j_data = request.get_json()

    user_id = j_data['user_id']
    month = j_data['month']
    temp = j_data['temperature']
    latitude = j_data['latitude']
    longitude = j_data['longitude']
    time = j_data['time_hour']
    dish_id = j_data['dish_id']

    db.insert(user_id, month, temp, latitude, longitude, time, dish_id)

    return jsonify({"massege": "ok"}), 200


@app.route('/create_user', methods=['GET'])
def create_user():
    j_data = request.get_json()

    user_id = j_data['user_id']
    if user_id == -1:
        user.append(user_id)
        user_id = len(user)

    return jsonify({"user_id": user_id})


@app.route('/model', methods=['POST'])
def post_pickle():
    global model_a
    global model_b

    models_dict = pickle.loads(request.get_data())

    model_a = models_dict['model_a']
    model_b = models_dict['model_b']
    return jsonify({'massage': 'OK'}), 200


if __name__ == '__main__':
    # dbinit()
    app.run(host="0.0.0.0", port=80, debug=True)
