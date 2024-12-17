import pandas as pd
import numpy as np
import glob
import logging
import os
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# 로깅 설정
logging.basicConfig(
    filename='training.log',      # 로깅을 저장할 파일 이름
    level=logging.INFO,           # 로깅 레벨, DEBUG, INFO, WARNING, ERROR 중 선택
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Starting the incremental training process")

# 파일 리스트 가져오기
data_dir = "/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/TrackDetMatches/"
file_pattern = os.path.join(data_dir, "output_*.csv")
track_files = sorted(glob.glob(file_pattern))

# 전체 파일 개수와 배치 크기 설정
total_files = len(track_files)
batch_size = 10

logging.info(f"Total files: {total_files}, Batch size: {batch_size}")

# det_raw_ids 로드
det_raw_ids_df = pd.read_csv("/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/muon_system_det_raw_id.csv")
det_raw_ids = np.sort(det_raw_ids_df['det_raw_id'].unique())

mlb = MultiLabelBinarizer(classes=det_raw_ids)
scaler = StandardScaler()

model = None  # 첫 배치 전까지 모델은 None

for start_idx in range(0, total_files, batch_size):
    batch_files = track_files[start_idx:start_idx+batch_size]
    logging.info(f"Processing files {batch_files}")

    # 배치 데이터 로드
    tracks_df_list = []
    for f in batch_files:
        df_temp = pd.read_csv(f)
        tracks_df_list.append(df_temp)
    tracks_df = pd.concat(tracks_df_list, ignore_index=True)

    # det_raw_id를 리스트 형태로 변환
    tracks_df['det_raw_id'] = tracks_df['det_raw_id'].apply(lambda x: list(map(int, x.split(' ')[:-1])))

    # MultiLabel 인코딩
    track_det_matches = mlb.fit_transform(tracks_df['det_raw_id'])

    X = tracks_df[['track_pt', 'track_eta', 'track_phi']].values
    X_scaled = scaler.fit_transform(X)  # 스케일링

    Y = track_det_matches

    # Train/Test split
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    # 첫번째 배치일 경우 모델 초기화
    if model is None:
        model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
        logging.info("Initialized new XGBRegressor model")

        # 첫 배치 학습
        model.fit(X_train, Y_train, eval_set=[(X_test, Y_test)], verbose=True)
    else:
        # 추가 배치의 경우 이전 모델로부터 이어서 학습
        model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
        logging.info("Continuing training from previous model")
        
        # 이전 모델 파라미터를 이용해 추가 학습
        # 여기서 xgb_model에는 직전 batch 학습 완료 후 모델을 저장한 파일 혹은 model 객체를 사용할 수 있음
        # 이전 모델 객체(model)을 직접 넣을 수 있으나, 안정적으로 하려면 model을 파일로 저장 후 로드하는 방식을 권장
        model.fit(X_train, Y_train, eval_set=[(X_test, Y_test)], verbose=True, xgb_model=model.get_booster())

    # 평가
    Y_pred_reg = model.predict(X_test)
    # 시그모이드 변환
    Y_prob = 1 / (1 + np.exp(-Y_pred_reg))
    Y_pred_bin = (Y_prob > 0.5).astype(int)

    from sklearn.metrics import hamming_loss, f1_score
    hl = hamming_loss(Y_test, Y_pred_bin)
    f1_micro = f1_score(Y_test, Y_pred_bin, average='micro')
    f1_macro = f1_score(Y_test, Y_pred_bin, average='macro')

    logging.info(f"Batch {start_idx//batch_size + 1} evaluation:")
    logging.info(f"Hamming Loss: {hl:.4f}, Micro-F1: {f1_micro:.4f}, Macro-F1: {f1_macro:.4f}")

    # 모델 저장
    model_save_path = f"model_batch_{start_idx//batch_size + 1}.json"
    model.save_model(model_save_path)
    logging.info(f"Saved model to {model_save_path}")

logging.info("Training process completed")
