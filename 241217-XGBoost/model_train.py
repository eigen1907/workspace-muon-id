import sys
import glob
import random
import numpy as np
import pandas as pd
import argparse

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

from data_loader import load_data_in_batches
from model_utils import save_model
from logging_utils import get_logger, StreamToLogger


logger = get_logger(__name__, log_file='logs/training.log')
sys.stdout = StreamToLogger(logger, level=20)

def model_train(
    X_batch,
    Y_batch,
    model_path=None
):
    X_train, X_val, Y_train, Y_val = train_test_split(X_batch, Y_batch, test_size=0.2, random_state=42)

    model = XGBRegressor(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)
    if model_path is not None:
        model.fit(X_train, Y_train, eval_set=[(X_val, Y_val)], verbose=True, xgb_model=model_path)
    else:
        model.fit(X_train, Y_train, eval_set=[(X_val, Y_val)], verbose=True)

    return model

def run_training(
    data_dir,
    detid_table_path,
    n_file=50,
    n_batch=10,
    model_prefix='XGBoost'
):
    random.seed(42)
    track_files = sorted(glob.glob(data_dir + '*'))
    random.shuffle(track_files)

    if n_file > len(track_files):
        raise ValueError('n_file cannot be larger than the total number of files.')

    detid_table_df = pd.read_csv(detid_table_path)
    detid_table = np.sort(detid_table_df['det_raw_id'].unique())

    train_files = track_files[:n_file]
    model_path = None
    scaler = None

    logger.info(f'Using {n_file} files for training.')

    train_data_gen = load_data_in_batches(train_files, detid_table, n_batch=n_batch, scaled=True, scaler=scaler)

    batch_index = 0
    final_model_path = None
    for X_batch, Y_batch, scaler in train_data_gen:
        batch_index += 1
        model = model_train(X_batch, Y_batch, model_path=model_path)
        model_path = f'{model_prefix}_{batch_index}.json'
        save_model(model, model_path)
        logger.info(f'Model saved after batch {batch_index}: {model_path}')
        final_model_path = model_path

    logger.info('Training completed.')
    if final_model_path:
        logger.info(f'Final model saved at: {final_model_path}')

def main():
    parser = argparse.ArgumentParser(description='Train XGBoost model incrementally.')
    parser.add_argument('--data_dir', type=str, required=True, help='track detector match data dir path')
    parser.add_argument('--detid_table_path', type=str, required=True, help='detector raw id table csv file path')
    parser.add_argument('--n_file', type=int, default=50, help='Number of files to use for training')
    parser.add_argument('--n_batch', type=int, default=10, help='Number of files per batch')
    parser.add_argument('--model_prefix', type=str, default='XGBoost', help='Prefix for saved models')
    args = parser.parse_args()

    run_training(
        data_dir=args.data_dir,
        detid_table_path=args.detid_table_path,
        n_file=args.n_file,
        n_batch=args.n_batch,
        model_prefix=args.model_prefix
    )

if __name__ == '__main__':
    main()
