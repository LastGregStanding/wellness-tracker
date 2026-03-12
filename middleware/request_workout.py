import requests

def request_workout(filters):
    url = "http://localhost:5007/workout"
    response = requests.post(url, json=filters)
    if response.status_code == 200:
        return response.json()
    return None