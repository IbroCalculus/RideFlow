import requests
import sys

BASE_URL = "http://localhost:8000"
EMAIL = "rider@example.com"
PASSWORD = "password123"

def register():
    print(f"Registering user {EMAIL}...")
    response = requests.post(f"{BASE_URL}/auth/register", json={
        "email": EMAIL,
        "password": PASSWORD,
        "phone_number": "+1234567890",
        "full_name": "Rider One",
        "is_driver": False
    })
    if response.status_code == 200:
        print("✅ Registration successful!")
        return True
    elif "already registered" in response.text:
        print("⚠️ User already exists, proceeding to login.")
        return True
    else:
        print(f"❌ Registration failed: {response.text}")
        return False

def login():
    print(f"Logging in user {EMAIL}...")
    response = requests.post(f"{BASE_URL}/auth/token", data={
        "username": EMAIL,
        "password": PASSWORD
    })
    if response.status_code == 200:
        print(f"✅ Login successful! Token: {response.json()['access_token'][:20]}...")
        return True
    else:
        print(f"❌ Login failed: {response.text}")
        return False

if __name__ == "__main__":
    if register():
        login()
