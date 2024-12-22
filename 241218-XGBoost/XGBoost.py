import os
import glob
import numpy as np
import pandas as pd
import joblib
import argparse

from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

def load_data(file_paths, track_scaler, detid_encoder):
    df_list = [pd.read_csv(file_path) for file_path in file_paths]
    df = pd.concat(df_list, ignore_index=True)
    df['det_raw_id'] = df['det_raw_id'].apply(lambda x: list(map(int, x.split(' ')[:-1])))

    X = track_scaler.transform(df[['track_pt', 'track_eta', 'track_phi']].values)
    Y = detid_encoder.transform(df['det_raw_id'])
    return X, Y

def data_generator(file_paths, batch_size, track_scaler, detid_encoder):
    for i in range(0, len(file_paths), batch_size):
        batch_files = file_paths[i:i+batch_size]
        X_batch, Y_batch = load_data(batch_files, track_scaler, detid_encoder)
        yield X_batch, Y_batch

def init_model_and_scaler(data_dir, detid_table_path, output_model_dir, n_files=10):
    track_paths = sorted(glob.glob(os.path.join(data_dir, '*.csv')))
    sample_paths = track_paths[:n_files]

    df_list = [pd.read_csv(p) for p in sample_paths]
    df_sample = pd.concat(df_list, ignore_index=True)
    df_sample['det_raw_id'] = df_sample['det_raw_id'].apply(lambda x: list(map(int, x.split(' ')[:-1])))

    detid_table_df = pd.read_csv(detid_table_path)
    detid_table = np.sort(detid_table_df['det_raw_id'].unique())

    detid_encoder = MultiLabelBinarizer(classes=detid_table)
    detid_encoder.fit(df_sample['det_raw_id'])

    track_scaler = StandardScaler()
    track_scaler.fit(df_sample[['track_pt', 'track_eta', 'track_phi']].values)

    X_sample = track_scaler.transform(df_sample[['track_pt', 'track_eta', 'track_phi']].values)
    Y_sample = detid_encoder.transform(df_sample['det_raw_id'])
    X_train, X_val, Y_train, Y_val = train_test_split(X_sample, Y_sample, test_size=0.1, random_state=42)

    model = XGBClassifier(n_estimators=100, max_depth=10, learning_rate=0.1, random_state=42)
    model.fit(X_train, Y_train, eval_set=[(X_val, Y_val)], verbose=True)
    
    if not os.path.exists(output_model_dir):
        os.makedirs(output_model_dir)
    model.save_model(os.path.join(output_model_dir, 'model.json'))
    joblib.dump(track_scaler, os.path.join(output_model_dir, 'scaler.pkl'))
    joblib.dump(detid_encoder, os.path.join(output_model_dir, 'encoder.pkl'))

def train_model(data_dir, input_model_dir, output_model_dir, n_files=100, batch_size=10):
    model = XGBClassifier()
    model.load_model(os.path.join(input_model_dir, 'model.json'))

    track_scaler = joblib.load(os.path.join(input_model_dir, 'scaler.pkl'))
    detid_encoder = joblib.load(os.path.join(input_model_dir, 'encoder.pkl'))

    track_paths = sorted(glob.glob(os.path.join(data_dir, '*.csv')))
    train_track_paths = track_paths[:n_files]

    for X_batch, Y_batch in data_generator(train_track_paths, batch_size, track_scaler, detid_encoder):
        X_train, X_val, Y_train, Y_val = train_test_split(X_batch, Y_batch, test_size=0.1, random_state=42)
        model.fit(X_train, Y_train, xgb_model=model.get_booster(), eval_set=[(X_val, Y_val)], verbose=True)
    
    if not os.path.exists(output_model_dir):
        os.makedirs(output_model_dir)
    model.save_model(os.path.join(output_model_dir, 'model.json'))
    joblib.dump(track_scaler, os.path.join(output_model_dir, 'scaler.pkl'))
    joblib.dump(detid_encoder, os.path.join(output_model_dir, 'encoder.pkl'))

def evaluate_model(data_dir, input_model_dir, n_files=10):
    model = XGBClassifier()
    model.load_model(os.path.join(input_model_dir, 'model.json'))

    track_scaler = joblib.load(os.path.join(input_model_dir, 'scaler.pkl'))
    detid_encoder = joblib.load(os.path.join(input_model_dir, 'encoder.pkl'))

    track_paths = sorted(glob.glob(os.path.join(data_dir, '*.csv')))
    eval_paths = track_paths[-n_files:]
    
    X_eval, Y_eval = load_data(eval_paths, track_scaler, detid_encoder)
    preds = model.predict(X_eval)
    accuracy = (preds == Y_eval).mean()
    return accuracy

def main():
    parser = argparse.ArgumentParser(description='Workflow for XGBoost.')
    parser.add_argument('--workflow', type=str, required=True, help='select workflow: "init", "train", "eval"')
    parser.add_argument('--data_dir', type=str, required=True, help='track detector match data dir path')
    parser.add_argument('--detid_table_path', type=str, help='detector raw id table csv file path')
    parser.add_argument('--input_model_dir', type=str, help='model&scaler input dir path')
    parser.add_argument('--output_model_dir', type=str, default='model/xgboost', help='model&scaler output dir path')
    parser.add_argument('--n_files', type=int, default=10, help='Number of files to use for workflow')
    parser.add_argument('--batch_size', type=int, default=10, help='Number of files per batch')
    args = parser.parse_args()

    if args.workflow == 'init':
        init_model_and_scaler(args.data_dir, args.detid_table_path, args.output_model_dir, args.n_files)
    elif args.workflow == 'train':
        train_model(args.data_dir, args.input_model_dir, args.output_model_dir, args.n_files, args.batch_size)
    elif args.workflow == 'eval':
        evaluate_model(args.data_dir, args.input_model_dir, args.n_files)


if __name__ == '__main__':
    main()
