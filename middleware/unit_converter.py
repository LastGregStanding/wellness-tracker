import requests

def convert_units(value, from_unit, to_unit):
    url = "http://localhost:5003/convert"
    
    unit_data = {
        'value': value,
        'from_unit': from_unit,
        'to_unit': to_unit
    }
    
    try:
        response = requests.post(url, json=unit_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.json().get('error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to unit converter microservice: {e}")
        return None