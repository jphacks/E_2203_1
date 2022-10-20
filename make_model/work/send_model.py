#モデルコンテナのコード
import pandas as pd
import os
import requests
import pickle
from sqlalchemy import create_engine


def get_df():
    user_name = "root"
    password = os.getenv("MYSQL_ROOT_PASSWORD")
    host = "jp-mysql"
    port = 3306
    db_name = "db"

    engine = create_engine(f"mysql+mysqlconnector://{user_name}:{password}@{host}:{port}/{db_name}")

    query = "select month, steps, temperature, latitude, longitude, time_hour, dish_id from test_table where "
    df = pd.read_sql(query, con=engine)
    
    return df

def main():
    # df = get_df()
    # model = make_model_A(df)
    model = ["1", "2", "3"]

    url = "http://jp-main/model"

    res = requests.post(
        url=url,
        data=pickle.dumps(model),
        headers={"Content-Type": "application/octet-stream"}
    )

    print(res)

if __name__ == "__main__":
    main()