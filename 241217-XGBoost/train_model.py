# train_model.py
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from logging_utils import get_logger, StreamToLogger
import sys

logger = get_logger(__name__, log_file='logs/training.log')

sys.stdout = StreamToLogger(logger, level=20)

def train_model(data_generator, callback=None, model_path=None):
    model = None
    prev_model_path = model_path
    scaler = None
    batch_count = 0

    for (X_batch, Y_batch, scaler) in data_generator:
        X_train, X_val, Y_train, Y_val = train_test_split(X_batch, Y_batch, test_size=0.2, random_state=42)

        if model is None:
            model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
            if prev_model_path is not None:
                model.fit(X_train, Y_train, eval_set=[(X_val, Y_val)], verbose=True, xgb_model=prev_model_path)
            else:
                model.fit(X_train, Y_train, eval_set=[(X_val, Y_val)], verbose=True)
        else:
            model.fit(X_train, Y_train, eval_set=[(X_val, Y_val)], verbose=True, xgb_model=prev_model_path)

        batch_count += 1
        if callback is not None:
            callback(model, batch_count)

    return model, scaler


