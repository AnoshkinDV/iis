import random
import time
import requests

ML_SERVICE_URL = "http://ml_service:8000/api/prediction"


def generate_features():
    return {
        "battery_power": random.uniform(500.0, 2000.0),
        "blue": random.choice([0.0, 1.0]),
        "clock_speed": random.uniform(0.5, 3.0),
        "dual_sim": random.choice([0.0, 1.0]),
        "fc": random.uniform(0.0, 20.0),
        "four_g": random.choice([0.0, 1.0]),
        "int_memory": random.uniform(2.0, 64.0),
        "m_dep": random.uniform(0.1, 1.0),
        "mobile_wt": random.uniform(80.0, 200.0),
        "n_cores": random.choice([1.0, 2.0, 4.0, 6.0, 8.0]),
        "pc": random.uniform(0.0, 20.0),
        "px_height": random.uniform(0.0, 2000.0),
        "px_width": random.uniform(0.0, 2000.0),
        "ram": random.uniform(256.0, 4000.0),
        "sc_h": random.uniform(5.0, 20.0),
        "sc_w": random.uniform(5.0, 20.0),
        "talk_time": random.uniform(2.0, 20.0),
        "three_g": random.choice([0.0, 1.0]),
        "touch_screen": random.choice([0.0, 1.0]),
        "wifi": random.choice([0.0, 1.0]),
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
