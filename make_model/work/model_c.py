#モデルコンテナのコード
from flask import Flask
import pandas as pd
import pickle
import sqlalchemy as sa

app = Flask(__name__)

#DBにコネクト
url = 'mysql+pymysql://user:pass@localhost:3306/db?charset=utf8'
engine = sa.create_engine(url, echo=False)

#1日に一回DBからdfでもってきて機械学習のやつに突っ込む

def Get_df_state():
    query = "select from test_table where "
    df = pd.read_sql(query,con = engine)
    return df

model_A = make_model_A(Get_df_state())  #dfの引数渡せばモデル作れる...？

with open('model_A.pickle', 'wb') as f:
    pickle.dump(model_A, f) #model_Aをmodel_A.pickleとして保存

def Get_df_user():#引数もたせたい
    query = "select from db where id = {}" #変数入れたい
    df = pd.read_sql(query,con = engine)
    return df
model_B = make_model_B(Get_df_user())

with open('model_B.pickle', 'wb') as d:
    pickle.dump(model_B, d)