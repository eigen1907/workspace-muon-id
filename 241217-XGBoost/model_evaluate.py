import sys
import glob
import random
import numpy as np
import pandas as pd
import argparse

from data_loader import load_data_in_batches
from model_utils import load_model
from sklearn.metrics import hamming_loss, f1_score
from logging_utils import get_logger

logger = get_logger(__name__, log_file='logs/evaluation.log')

def model_evaluate(model, X_test, Y_test):
    Y_pred_reg = model.predict(X_test)
    Y_prob = 1 / (1 + np.exp(-Y_pred_reg))
    Y_pred_bin = (Y_prob > 0.5).astype(int)

    hl = hamming_loss(Y_test, Y_pred_bin)
    f1_micro = f1_score(Y_test, Y_pred_bin, average='micro')
    f1_macro = f1_score(Y_test, Y_pred_bin, average='macro')

    logger.info(f"Hamming Loss: {hl:.4f}")
    logger.info(f"Micro-F1: {f1_micro:.4f}")
    logger.info(f"Macro-F1: {f1_macro:.4f}")

def run_evaluation(
    data_dir,
    detid_table_path,
    model_path,
    n_test=10,
):
    random.seed(42)
    track_files = sorted(glob.glob(data_dir + '*'))
    random.shuffle(track_files)

    detid_table_df = pd.read_csv(detid_table_path)
    detid_table = np.sort(detid_table_df['det_raw_id'].unique())

    if n_test > len(track_files):
        raise ValueError("n_test cannot be larger than the total number of files.")

    test_files = track_files[:n_test]

    model = load_model(model_path)
    logger.info(f"Loaded model from {model_path}")

    test_data_gen = load_data_in_batches(test_files, detid_table, n_batch=n_test, scaled=True, scaler=None)
    X_test_list = []
    Y_test_list = []
    for X_t, Y_t, _ in test_data_gen:
        X_test_list.append(X_t)
        Y_test_list.append(Y_t)

    X_test = np.vstack(X_test_list)
    Y_test = np.vstack(Y_test_list)

    model_evaluate(model, X_test, Y_test)
    logger.info("Evaluation completed.")

def main():
    parser = argparse.ArgumentParser(description='Evaluate XGBoost model.')
    parser.add_argument('--data_dir', type=str, required=True, help='track detector match data dir path')
    parser.add_argument('--detid_table_path', type=str, required=True, help='detector raw id table csv file path')    
    parser.add_argument('--model_path', type=str, required=True, help='Path to the saved model file')
    parser.add_argument('--n_test', type=int, default=10, help='Number of files to use for testing')
    args = parser.parse_args()

    run_evaluation(
        data_dir=args.data_dir,
        detid_table_path=args.detid_table_path,
        n_test=args.n_test,
        model_path=args.model_path
    )

if __name__ == '__main__':
    main()
    