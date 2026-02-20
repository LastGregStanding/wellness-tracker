import requests

def get_quote(category='motivational'):
    """
    Calls the quote generator microservice to get a random quote.
    
    Args:
        category: Type of quote - 'motivational', 'health', or 'video_game'
    
    Returns:
        dict: Response from the microservice with 'quote' and 'source' keys
    """
    url = "http://localhost:5004/quote"
    
    payload = {
        'category': category
    }
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.json().get('error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to quote microservice: {e}")
        return None