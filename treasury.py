import requests
import json
import urllib.request

def get_treasury_data():
    api_url = "https://api.stlouisfed.org/fred/category?category_id=125&api_key=e88a73f98d7c51c8a9ebb57d803200bc&file_type=json"

    response = urllib.request.urlopen(api_url)

    try:
        result = json.loads(response.read())
        return result
    except:
        return None


output = get_treasury_data()
processed = output

symbol = "number"
if output is not None:
    print(f"{symbol}: {processed}")
else:
    print("Failed to retrieve data.")