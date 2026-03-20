import mlflow
import mlflow.sklearn
import cloudpickle
from pathlib import Path

RUN_ID = "8165633fb74d422da075b341cd030f41"

mlflow.set_tracking_uri("http://localhost:5000")
model_uri = f"runs:/{RUN_ID}/model"

model = mlflow.sklearn.load_model(model_uri)
print(f"Тип загруженной модели: {type(model)}")

project_root = Path(__file__).resolve().parents[2]
models_dir = project_root / "models"
models_dir.mkdir(parents=True, exist_ok=True)
save_path = models_dir / "model.pkl"
with open(save_path, "wb") as f:
    cloudpickle.dump(model, f)

print("Model saved successfully")
