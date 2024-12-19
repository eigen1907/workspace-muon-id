#!/bin/bash

python model_evaluate.py \
    --data_dir=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/TrackDetMatches/ \
    --detid_table_path=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/muon_system_det_raw_id.csv \
    --n_test=10 \
    --model_path=XGBoost_1.json

