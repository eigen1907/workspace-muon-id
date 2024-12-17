# data_loader.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler

def load_data_in_batches(track_files, det_raw_ids, batch_file_count=10, scaled=True, scaler=None):
    total_files = len(track_files)
    fitted_scaler = scaler
    for start_idx in range(0, total_files, batch_file_count):
        end_idx = start_idx + batch_file_count
        batch_files = track_files[start_idx:end_idx]
        df_list = []
        for f in batch_files:
            df_temp = pd.read_csv(f)
            df_list.append(df_temp)
        tracks_df = pd.concat(df_list, ignore_index=True)

        tracks_df['det_raw_id'] = tracks_df['det_raw_id'].apply(lambda x: list(map(int, x.split(' ')[:-1])))

        mlb = MultiLabelBinarizer(classes=det_raw_ids)
        Y = mlb.fit_transform(tracks_df['det_raw_id'])

        X = tracks_df[['track_pt', 'track_eta', 'track_phi']].values

        if scaled:
            if fitted_scaler is None:
                fitted_scaler = StandardScaler()
                X = fitted_scaler.fit_transform(X)
            else:
                X = fitted_scaler.transform(X)

        yield X, Y, fitted_scaler
