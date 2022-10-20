#モデルコンテナのコード
from flask import Flask
import pandas as pd
import pickle
import sqlalchemy as sa

app = Flask(__name__)

url = 'mysql+pymysql://user:pass@localhost:3306/db?charset=utf8'
engine = sa.create_engine(url, echo=False)

def Get_df_state():
    query = "select * from db"
    df = pd.read_sql(query,con = engine)
    return df

model_A = make_model_A(Get_df_state())  

with open('model_A.pickle', 'wb') as f:
    pickle.dump(model_A, f) #model_Aをmodel_A.pickleとして保存

def Get_df_user():
    query = "select from db where u_id = {}"
    df = pd.read_sql(query,con = engine)
    return df

with open('model_B.pickle', 'wb') as d:
    pickle.dump(model_B, d)