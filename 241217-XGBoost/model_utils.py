# model_utils.py
import os
from xgboost import XGBRegressor

def save_model(model, model_path):
    if not os.path.exists('model'):
        os.makedirs('model')
    full_path = os.path.join('model', model_path)
    model.save_model(full_path)

def load_model(model_path):
    full_path = os.path.join('model', model_path)
    model = XGBRegressor()
    model.load_model(full_path)
    return model

def create_model_save_callback(logger, model_save_prefix):
    model_save_count = [0]

    def callback(model, batch_index):
        model_save_count[0] += 1
        model_path = f"{model_save_prefix}_{model_save_count[0]}.json"
        save_model(model, model_path)
        logger.info(f"Model saved after batch {model_save_count[0]}: {model_path}")

    return callback
