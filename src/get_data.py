import os
import yaml
import pandas as pd
import argparse

def read_parmas(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def get_data(config_path):
    config = read_parmas(config_path)
    #print(config)
    data = config['data_source']['s3_source']
    df = pd.read_csv(data, sep=',', encoding='utf-8').iloc[:, 1:]
    print(df.head())
    return df

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parse_args = args.parse_args()
    get_data(config_path=parse_args.config)
