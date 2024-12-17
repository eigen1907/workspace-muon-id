# evaluate_model.py
import numpy as np
from sklearn.metrics import hamming_loss, f1_score
from logging_utils import get_logger

logger = get_logger(__name__, log_file='logs/evaluation.log')

def evaluate_model(model, X_test, Y_test):
    Y_pred_reg = model.predict(X_test)
    Y_prob = 1 / (1 + np.exp(-Y_pred_reg))
    Y_pred_bin = (Y_prob > 0.5).astype(int)

    hl = hamming_loss(Y_test, Y_pred_bin)
    f1_micro = f1_score(Y_test, Y_pred_bin, average='micro')
    f1_macro = f1_score(Y_test, Y_pred_bin, average='macro')

    logger.info(f"Hamming Loss: {hl:.4f}")
    logger.info(f"Micro-F1: {f1_micro:.4f}")
    logger.info(f"Macro-F1: {f1_macro:.4f}")

