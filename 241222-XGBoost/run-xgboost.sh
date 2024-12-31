N_FILES=300
N_EST=1000
N_DEPTH=5
LR=0.01
OUTDIR=model/file${N_FILES}-e${N_EST}-d${N_DEPTH}-lr${LR}
mkdir ${OUTDIR}
nohup python XGBoost.py \
    --data_dir=/users/hep/eigen1907/STORE/TrackDetMatches \
    --detid_table_path=/users/hep/eigen1907/Workspace/Workspace-DL/241222-det_raw_id/matched_det_raw_id.csv \
    --output_model_dir=${OUTDIR} \
    --n_files=${N_FILES} \
    --n_est=${N_EST} \
    --n_depth=${N_DEPTH} \
    --lr=${LR} \
    > ${OUTDIR}/nohup.out 2>&1 &
