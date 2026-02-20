import requests

def get_quote(category='motivational'):
    url = "http://localhost:5004/quote"
    
    quote_data = {
        'category': category
    }
    
    try:
        response = requests.post(url, json=quote_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.json().get('error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to quote microservice: {e}")
        return None