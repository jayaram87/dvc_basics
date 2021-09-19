import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save(config_path):
    config = read_params(config_path)
    train_path = config['split_data']['train_path']
    test_path = config['split_data']['test_path']
    split_ratio = config['split_data']['test_size']
    raw_data_path = config['load_data']['raw_dataset_csv']
    random_state = config['base']['random_state']
    
    df = pd.read_csv(raw_data_path, sep=',')
    train, test = train_test_split(df, random_state=random_state, test_size=split_ratio)
    train.to_csv(train_path, index=False, sep=',', encoding='utf-8')
    test.to_csv(test_path, index=False, sep=',', encoding='utf-8')

    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    split_and_save(parsed_args.config)

    
