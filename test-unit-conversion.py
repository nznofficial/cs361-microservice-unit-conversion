import requests

response = requests.get(
    "http://localhost:8006/convert",
    params={"value": 350, "from_unit": "F", "to_unit": "C"},
)

if response.status_code == 200:
    print(response.json()["converted_value"])
else:
    print(response.json()["error"])
