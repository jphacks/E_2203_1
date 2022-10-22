#from datetime import timedelta
from flask import Flask, request, jsonify#, session
# import pickle
# import pandas as pd
import json
#from pandas import json_normalize
import db

app = Flask(__name__)
user = [] 

@app.route('/dish_list', methods=['GET'])
def dish_list():
    j_data= json.loads(request.data)
    
    dish_id    =  j_data['id']

    menu = db.Select_dish(dish_id)

    return menu

@app.route('/ate_dish', methods=['POST']) #userがmenuを選んだあとにくるリクエスト
def post_json():

    j_data= json.loads(request.data)
    
    id          =  j_data['id']
    month       =  j_data['month']
    steps       =  j_data['steps']
    temp        =  j_data['temperature']
    latitude         =  j_data['latitude']
    longitude   =  j_data['longitude']
    time        =  j_data['time_hour']
    dish_id     =  j_data['dish_id']

    db.Insert(id, month, steps, temp, latitude, longitude, time, dish_id)

    return jsonify({"massege": "ok"}),200

# @app.route('/dish_insert', methods=['POST']) 
# def post_menu():

#     j_data= json.loads(request.data)
 
#     id       =  j_data['id']
#     menu     =  j_data['menu']
 
#     db.Dish_Insert(id, menu)
#     return jsonify({"massege": "ok"}),200

@app.route('/create_user',methods=['GET'])
def create_user():
    
    j_data = json.loads(request.data)

    user_id   =  j_data['user_id']

    if user_id == -1:
        user_id = len(user)
    

    data = {"user_id": user_id}

    user.append(data)
    
    json.dumps(data)

    return (data)

# @app.route('/model', methods=['POST']) 
# def post_pickle():
#     model = pickle.loads(request.get_data())
#     session["model"] = model
#     return jsonify({'massage': 'OK'}), 200


if __name__ == '__main__':
    # dbinit()
    app.run(host="0.0.0.0", port=80, debug=True)
