import requests

def request_weather(zip_code):
    url = "http://localhost:5006/weather"
    response = requests.post(url, json={"zip_code": zip_code})
    result = response.json()
    return result