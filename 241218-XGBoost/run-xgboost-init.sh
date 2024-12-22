OUTDIR=model/241218-init-file300-e100-d10
mkdir ${OUTDIR}
nohup python XGBoost.py \
    --workflow=init \
    --data_dir=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/TrackDetMatches \
    --detid_table_path=/users/hep/eigen1907/Workspace/Workspace-DL/241215-track_det_raw_id/muon_system_det_raw_id.csv \
    --output_model_dir=${OUTDIR} \
    --n_files=300 > ${OUTDIR}/nohup.out 2>&1 &


