#!/bin/bash

nohup python model_train.py \
    --data_dir=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/TrackDetMatches/ \
    --detid_table_path=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/muon_system_det_raw_id.csv \
    --n_file=50 \
    --n_batch=10 \
    --model_prefix=XGBoost &

