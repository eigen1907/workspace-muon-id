# main.py
import glob
import random
import numpy as np
import pandas as pd
from data_loader import load_data_in_batches
from train_model import train_model
from model_utils import create_model_save_callback
from evaluate_model import evaluate_model
from logging_utils import get_logger

logger = get_logger(__name__, log_file='logs/main.log')

def main():
    random.seed(42)
    data_dir = "/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/TrackDetMatches/"
    track_files = sorted(glob.glob(data_dir + "output_*.csv"))
    random.shuffle(track_files)

    det_raw_ids_path = "/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/muon_system_det_raw_id.csv"
    det_raw_ids_df = pd.read_csv(det_raw_ids_path)
    det_raw_ids = np.sort(det_raw_ids_df['det_raw_id'].unique())

    num_files = len(track_files)
    train_ratio = 0.9
    train_count = int(num_files * train_ratio)
    train_files = track_files[:train_count]
    test_files = track_files[train_count:]

    batch_file_count = 10
    model_save_prefix = "incremental_model"
    logger.info("Starting training process")

    model_save_callback = create_model_save_callback(logger, model_save_prefix)

    # Train
    train_data_gen = load_data_in_batches(train_files, det_raw_ids, batch_file_count=batch_file_count, scaled=True, scaler=None)
    model, scaler = train_model(train_data_gen, callback=model_save_callback, model_path=None)

    # Test
    if test_files:
        test_data_gen = load_data_in_batches(test_files, det_raw_ids, batch_file_count=len(test_files), scaled=True, scaler=scaler)
        X_test_list = []
        Y_test_list = []
        for X_t, Y_t, _ in test_data_gen:
            X_test_list.append(X_t)
            Y_test_list.append(Y_t)

        X_test = np.vstack(X_test_list)
        Y_test = np.vstack(Y_test_list)

        evaluate_model(model, X_test, Y_test)
    else:
        logger.info("No test files available. Evaluation skipped.")

    logger.info("Training and evaluation completed.")

if __name__ == '__main__':
    main()


