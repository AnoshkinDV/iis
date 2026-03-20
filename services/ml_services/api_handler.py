import cloudpickle
import pandas as pd


class FastAPIHandler:

    def __init__(self):
        with open("/models/model.pkl", "rb") as f:
            self.model = cloudpickle.load(f)

    def predict(self, features: dict):
        df = pd.DataFrame([features])
        if hasattr(self.model, "feature_names_in_"):
            df = df[list(self.model.feature_names_in_)]
        prediction = self.model.predict(df)[0]

        return float(prediction)
