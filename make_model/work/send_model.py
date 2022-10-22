import os
import pickle
import time

import pandas as pd
import requests
from sqlalchemy import create_engine

import modelA
import modelB


def get_train_data():
    user_name = "root"
    password = os.getenv("MYSQL_ROOT_PASSWORD")
    host = "jp-mysql"
    port = 3306
    db_name = "jp-db"

    engine = create_engine(f"mysql+mysqlconnector://{user_name}:{password}@{host}:{port}/{db_name}")

    query = "select month, steps, temperature, latitude, longitude, time_hour, dish_id from situations "
    df = pd.read_sql(query, con=engine)

    return df


def get_models(df: pd.DataFrame):
    model_a = modelA.ModelA()
    model_a.make_model(df)

    model_b = modelB.ModelB()
    model_b.make_sc(df)

    models_dict = {'model_a': model_a, 'model_b': model_b}
    return models_dict


def main():
    time.sleep(10)
    df = get_train_data()
    models_dict = get_models(df)

    url = "http://jp-main/model"

    res = requests.post(
        url=url,
        data=pickle.dumps(models_dict),
        headers={"Content-Type": "application/octet-stream"}
    )

    print(res)


if __name__ == "__main__":
    main()
