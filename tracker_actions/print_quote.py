from middleware.quote_generator import get_quote

def print_quote():
    # Call quote microservice
    result = get_quote('motivational')
    
    if result:
        print(f"\n\"{result['quote']}\"")
        print(f"\n- {result['source']}")
    
    input("\nPress ENTER to return to the main menu.")