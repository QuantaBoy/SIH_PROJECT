import os 
import joblib

MODEL_PATH = os.path.dirname(__file__), "classifier.joblib"

_model = None

def load_model():
    global _model

    if _model is not None:
        return _model
    
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model File not Found at {MODEL_PATH}. Please train and svae the model"
        )
    
    _model = joblib.load(MODEL_PATH)

    return _model

def predict(features):
    model = load_model()

    prediction = model.predict([features])[0]

    return prediction