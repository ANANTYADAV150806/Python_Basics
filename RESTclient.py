import requests
BASE_URL = "http://127.0.0.1:5000"
response = requests.get(f"{BASE_URL}/customers")
print("all customers",response.json())
response = requests.get(f"{BASE_URL}/customers/3")
print("customer3", response.json())
new_customer = {"name": "ishaan", "age": 20}
response = requests.post(f"{BASE_URL}/customers", json = new_customer)
print("created",response.json())
