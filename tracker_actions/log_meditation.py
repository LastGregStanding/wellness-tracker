from middleware.unit_converter import convert_units
from prompts import post_action_prompt

# Log your meditation
def log_meditation(name):
    global daily_meditation, last_action
    
    while True: 
        val = input("\nHow many minutes did you meditate?\n\n> ").strip()
        
        try:
            minutes = int(val) 
            
            # Validate the number is within 1 through 1440
            if 1 <= minutes <= 1440:
                daily_meditation += minutes
                last_action = {"type": "meditation", "amount": minutes}
                
                print(f"\nGreat job, {name}! {minutes} minutes added to daily total.")
                user_wants_stats = input("\nWould you like to see how long you have meditated for (yes/no)? ")
                if user_wants_stats.lower() == 'yes':
                    print(f"\nYou meditation time in minutes: {daily_meditation}")
                    convert_time = convert_units(daily_meditation, 'minutes', 'hours')
                    hours = convert_time['converted_value']
                    print(f"\nYour meditation time in hours: {hours}") 
                post_action_prompt()
                break 

            # User enters a number that is out of range
            else:
                print("\nInvalid Input. Please provide a number between 1 and 1440")
        
        # User enters words or special characters
        except ValueError:
            print("\nInvalid Input. Please provide a number between 1 and 1440")