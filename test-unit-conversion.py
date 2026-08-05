import requests

def print_conversion(json_object):
    val = json_object["converted_value"]
    unit = json_object["converted_unit"]
    print(f"{val} {unit}")


#F to C
tempInF = 350
print(f"Requesting to convert {tempInF} F to C")
response = requests.get(
    "http://localhost:5001/convert",
    params={"value": {tempInF}, "from_unit": "F", "to_unit": "C"},
)

if response.status_code == 200:
    print_conversion(response.json())
else:
    print(response.json()["error"])


#tbsp to cup
tablespoons = 10
print(f"Requesting to convert {tablespoons} tbsp to cups")
response = requests.get(
    "http://localhost:5001/convert",
    params={"value": {tablespoons}, "from_unit": "tbsp", "to_unit": "cup"},
)

if response.status_code == 200:
    print_conversion(response.json())
else:
    print(response.json()["error"])


# fl oz to l
fl_oz = 14
print(f"Requesting to convert {fl_oz} fl_oz to l")
response = requests.get(
    "http://localhost:5001/convert",
    params={"value": {fl_oz}, "from_unit": "fl_oz", "to_unit": "l"},
)

if response.status_code == 200:
    print_conversion(response.json())
else:
    print(response.json()["error"])

#C to F
tempInC = 30
print(f"Requesting to convert {tempInC} C to F")
response = requests.get(
    "http://localhost:5001/convert",
    params={"value": {tempInC}, "from_unit": "C", "to_unit": "F"},
)

if response.status_code == 200:
    print_conversion(response.json())
else:
    print(response.json()["error"])
