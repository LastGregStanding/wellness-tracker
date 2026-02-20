import requests

def convert_units(value, from_unit, to_unit):
    """
    Calls the unit converter microservice to convert values between units.
    
    Args:
        value: The numeric value to convert
        from_unit: The unit to convert from (e.g., 'minutes', 'oz', 'lbs')
        to_unit: The unit to convert to (e.g., 'hours', 'gallons', 'kg')
    
    Returns:
        dict: Response from the microservice with conversion result
    """
    url = "http://localhost:5003/convert"
    
    payload = {
        'value': value,
        'from_unit': from_unit,
        'to_unit': to_unit
    }
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.json().get('error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to unit converter microservice: {e}")
        return None