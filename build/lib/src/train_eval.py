import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import pickle
import json

def train_eval(config_path):
    config = read_params(config_path)
    train_path = config['split_data']['train_path']
    test_path = config['split_data']['test_path']
    random_state = config['base']['random_state']
    model_dir = config['model_dir']
    alpha = config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio = config['estimators']['ElasticNet']['params']['l1_ratio']
    target = config['base']['target_col']

    train = pd.read_csv(train_path, sep=',')
    test = pd.read_csv(test_path, sep=',')

    train_x, train_y = train.iloc[:, 0:3], train.loc[:, target:]
    test_x, test_y = test.iloc[:, 0:3], test.loc[:, target:]

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)

    preds = lr.predict(test_x)

    rmse, mse, r2 = np.sqrt(mean_squared_error(test_y, preds)), mean_absolute_error(test_y, preds), r2_score(test_y, preds)

    with open(config['reports']['scores'], 'w') as f:
        scores = {
            "rsme": rmse,
            "mae": mse,
            "r2": r2
        }
        json.dump(scores, f, indent=4)

    with open(config['reports']['params'], 'w') as f:
        params = {
            "alpha": alpha,
            "l1_ratio": l1_ratio,
        }
        json.dump(params, f, indent=4)

    with open(os.path.join(model_dir, 'lr.sav'), 'wb+') as f:
        pickle.dump(lr, f)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    train_eval(parsed_args.config)

