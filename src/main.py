import joblib
import pandas as pd
import numpy as np
import glob
import pandas as pd



def run_model():
    df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))

    model = joblib.load('model_dump')

    x=df.drop(['price','mainroad',
          'guestroom',
          'basement',
          'hotwaterheating',
          'airconditioning',
          'prefarea',
          'furnishingstatus'], axis=1)

    y = model.predict(x)

    df['predict_value'] = y

    df.to_csv('data/result.csv')


    print("predicts are written to result.csv")

if __name__ == "__main__":
    run_model()
