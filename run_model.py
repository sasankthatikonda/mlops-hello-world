

import argparse
import json
from pathlib import Path
import numpy as np
import joblib


MODEL_PATH = Path("artifacts/model.pkl")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"model file not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help= "Feature list as JSON string. Example: \"[4.5, 4.5 3.5 0.3]\"")
    args = parser.parse_args()
    
    try:
        features = json.loads(args.input)
    except json.JSONDecodeError:
        raise ValueError("invalid Input. use Json list, e.g. --input \"[4.5, 4.5 3.5 0.3]\"")
    
    X = np.array(features).reshape(1,-1) 
    
    model = load_model()
    pred = model.predict(X)

    print(json.dumps({"prediction": pred.tolist()}))

if __name__ == "__main__":
    main()

    