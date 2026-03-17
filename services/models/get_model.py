import mlflow
import mlflow.sklearn
import pickle
from pathlib import Path

RUN_ID = "8a53557b6bb24b9681270b3a8a2f70bc"

mlflow.set_tracking_uri("http://localhost:5000")
model_uri = f"runs:/{RUN_ID}/model"

model = mlflow.sklearn.load_model(model_uri)
print(f"Тип загруженной модели: {type(model)}")

save_path = Path(__file__).resolve().parent / "model.pkl"
with open(save_path, "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")