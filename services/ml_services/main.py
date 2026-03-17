from fastapi import FastAPI
from pydantic import BaseModel
from api_handler import FastAPIHandler

app = FastAPI()
handler = FastAPIHandler()
# api принимает те признаки, которые ожидает модель
class PhoneFeatures(BaseModel):
    n_cores: float
    sc_h: float
    touch_screen: float

    ram_2: float
    ram_battery_power: float
    battery_power_2: float

    px_height_0_0: float
    px_height_1_0: float
    px_height_2_0: float
    px_height_3_0: float

    px_width_0_0: float
    px_width_1_0: float
    px_width_3_0: float

    int_memory_0_0: float
    int_memory_1_0: float
    int_memory_3_0: float


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/prediction")
def predict(item_id: int, features: PhoneFeatures):
    prediction = handler.predict(features.model_dump())

    return {
        "item_id": item_id,
        "predict": prediction
    }


