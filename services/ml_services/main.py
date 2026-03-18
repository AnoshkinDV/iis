from fastapi import FastAPI, Request
from pydantic import BaseModel
from api_handler import FastAPIHandler
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

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

ERROR_COUNT = Counter(
    "prediction_errors_total",
    "Total number of prediction errors by status code class",
    ["status_code"]
)

REQUEST_COUNT = Counter(
    "prediction_requests_total",
    "Total number of prediction requests"
)

PREDICTION_HISTOGRAM = Histogram(
    "prediction_value_histogram",
    "Histogram of model prediction values",
    buckets=(0, 1, 2, 3, 4, 5)
)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/api/prediction")
def predict(item_id: int, features: PhoneFeatures):
    REQUEST_COUNT.inc()
    
    prediction = handler.predict(features.model_dump())
    PREDICTION_HISTOGRAM.observe(prediction)
    return {
        "item_id": item_id,
        "predict": prediction
    }


@app.middleware("http")
async def track_errors(request: Request, call_next):
    response = await call_next(request)

    if 400 <= response.status_code < 500:
        ERROR_COUNT.labels(status_code="4xx").inc()
    elif 500 <= response.status_code < 600:
        ERROR_COUNT.labels(status_code="5xx").inc()

    return response
