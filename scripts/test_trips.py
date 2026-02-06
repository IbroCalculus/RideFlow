import requests
import json

BASE_URL = "http://localhost:8000"

def request_ride():
    print("Requesting a ride...")
    payload = {
        "pickup_lat": 37.7749,
        "pickup_lng": -122.4194,
        "dest_lat": 37.7849,
        "dest_lng": -122.4094,
        "rider_id": 1
    }
    try:
        response = requests.post(f"{BASE_URL}/trips/request", json=payload)
        if response.status_code == 200:
            print(f"✅ Ride Requested! Response: {response.json()}")
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    request_ride()
