import requests

def request_meal(filters):
    url = "http://localhost:5005/meal"

    try:
        response = requests.post(url, json=filters)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.json().get('error', 'Unknown error')}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to meal microservice: {e}")
        return None