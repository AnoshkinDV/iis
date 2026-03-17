import pickle
import pandas as pd


class FastAPIHandler:

    def __init__(self):
        with open("/models/model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, features: dict):

        # преобразуем API имена в имена признаков модели
        model_features = {
            "n_cores": features["n_cores"],
            "sc_h": features["sc_h"],
            "touch_screen": features["touch_screen"],

            "ram^2": features["ram_2"],
            "ram battery_power": features["ram_battery_power"],
            "battery_power^2": features["battery_power_2"],

            "px_height_0.0": features["px_height_0_0"],
            "px_height_1.0": features["px_height_1_0"],
            "px_height_2.0": features["px_height_2_0"],
            "px_height_3.0": features["px_height_3_0"],

            "px_width_0.0": features["px_width_0_0"],
            "px_width_1.0": features["px_width_1_0"],
            "px_width_3.0": features["px_width_3_0"],

            "int_memory_0.0": features["int_memory_0_0"],
            "int_memory_1.0": features["int_memory_1_0"],
            "int_memory_3.0": features["int_memory_3_0"],
        }
        feature_order = [
        "n_cores",
        "sc_h",
        "touch_screen",
        "ram^2",
        "ram battery_power",
        "battery_power^2",
        "px_height_0.0",
        "px_height_1.0",
        "px_height_2.0",
        "px_height_3.0",
        "px_width_0.0",
        "px_width_1.0",
        "px_width_3.0",
        "int_memory_0.0",
        "int_memory_1.0",
        "int_memory_3.0"
    ]

        df = pd.DataFrame([model_features])[feature_order]
        print(self.model.feature_names_in_)
        print("INPUT FEATURES:")
        print(df)
        prediction = self.model.predict(df)[0]

        return float(prediction)