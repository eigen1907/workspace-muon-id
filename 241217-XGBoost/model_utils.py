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
