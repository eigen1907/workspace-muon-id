nohup python XGBoost.py \
    --workflow=train \
    --data_dir=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/TrackDetMatches \
    --detid_table_path=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/muon_system_det_raw_id.csv \
    --input_model_dir=model/241218-init \
    --output_model_dir=model/241218-train \
    --n_files=300 \
    --batch_size=300 &