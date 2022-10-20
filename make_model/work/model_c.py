#モデルコンテナのコード
from flask import Flask
import pandas as pd
import pickle
import sqlalchemy as sa


def Get_df_state():
    url = 'mysql+pymysql://user:pass@localhost:3306/db?charset=utf8'
    engine = sa.create_engine(url, echo=False)
    query = "select from test_table where "
    df = pd.read_sql(query,con = engine)
    return df

def main():
    df_state = Get_df_state()
    model = make_model_A(df_state)

    with open('model.pickle', 'wb') as f:
        pickle.dump(model, f) #model_Aをmodel_A.pickleとして保存

if __name__ == "__main__":
    main()