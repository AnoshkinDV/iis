import random
import time
import requests

ML_SERVICE_URL = "http://ml_service:8000/api/prediction"


def generate_features():
    return {
        "n_cores": random.choice([1.0, 2.0, 4.0, 6.0, 8.0]),
        "sc_h": random.uniform(5.0, 20.0),
        "touch_screen": random.choice([0.0, 1.0]),

        "ram_2": random.uniform(1000000.0, 25000000.0),
        "ram_battery_power": random.uniform(500000.0, 10000000.0),
        "battery_power_2": random.uniform(250000.0, 4000000.0),

        "px_height_0_0": random.choice([0.0, 1.0]),
        "px_height_1_0": random.choice([0.0, 1.0]),
        "px_height_2_0": random.choice([0.0, 1.0]),
        "px_height_3_0": random.choice([0.0, 1.0]),

        "px_width_0_0": random.choice([0.0, 1.0]),
        "px_width_1_0": random.choice([0.0, 1.0]),
        "px_width_3_0": random.choice([0.0, 1.0]),

        "int_memory_0_0": random.choice([0.0, 1.0]),
        "int_memory_1_0": random.choice([0.0, 1.0]),
        "int_memory_3_0": random.choice([0.0, 1.0]),
    }


def send_request():
    item_id = random.randint(1, 100000)
    params = {"item_id": item_id}
    json_data = generate_features()

    try:
        response = requests.post(ML_SERVICE_URL, params=params, json=json_data, timeout=10)
        print(f"STATUS: {response.status_code} | RESPONSE: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"REQUEST ERROR: {e}")


def main():
    while True:
        send_request()
        sleep_time = random.uniform(0, 5)
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()