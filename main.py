# Global State
daily_water = 0
daily_meditation = 0
last_action = {"type": None, "amount": 0}  

# Welcome Screen
def main():
    print("—" * 21)
    print("Wellness Tracker v1.0")
    print("—" * 21)
    print("Get healthier by keeping track of your daily health goals.\n")
    print("Getting started takes less than 2 seconds!\n")

    name = input("Please enter your name: ").strip()

    print(f"\nWelcome, {name}! Opening your personal Wellness Tracker.")
    
    show_main_menu(name)

# Main Menu 
def show_main_menu(name):
    while True:
        print("\n" + "—" * 15)
        print("Main Menu")
        print("—" * 15)
        print(f"\n{name}, what would you like to do?\n")
        print("1) Add 8oz water         (type '1' or 'water')")
        print("2) Add meditation time   (type '2' or 'meditation')")
        print("3) View daily stats      (type '3' or 'stats')")
        print("4) Exit program          (type '4' or 'exit')")

        choice = input("\nSelection: ").strip().lower()

        if choice in ['1', 'water']:
            track_water()
        elif choice in ['2', 'meditation']:
            track_meditation(name)
        elif choice in ['3', 'stats']:
            view_stats()
        elif choice in ['4', 'exit']:
            print("Closing tracker. Stay healthy!")
            break

# Track your water
def track_water():
    global daily_water, last_action
    amount = 8
    daily_water += amount
    last_action = {"type": "water", "amount": amount}
    
    print(f"\nSuccess! You added {amount}oz of water to your daily water intake.")
    post_action_prompt()

# Track your meditation
def track_meditation(name):
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
                post_action_prompt()
                break 

            # User enters a number that is out of range
            else:
                print("\nInvalid Input. Please provide a number between 1 and 1440")
        
        # User enters words or special characters
        except ValueError:
            print("\nInvalid Input. Please provide a number between 1 and 1440")

# Prompt after doing an action
def post_action_prompt():
    print("\nPress ENTER to return to the main menu.")
    print("Press 'U' to Undo previous entry")
    
    if input("\nSelection: ").strip().lower() == 'u':
        confirm_undo()

# Confirm whether you want to undo the previous action
def confirm_undo():
    global daily_water, daily_meditation, last_action
    
    confirm = input("\nAre you sure you want to undo the previous entry? This cannot be reversed (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        if last_action["type"] == "water":
            daily_water -= last_action["amount"]
            print("\nWater entry undone.")
        elif last_action["type"] == "meditation":
            daily_meditation -= last_action["amount"]
            print("\nMeditation entry undone.")
        
        last_action = {"type": None, "amount": 0} 
        input("Press ENTER to continue...")

# View your daily stats
def view_stats():
    print("\n" + "—" * 12)
    print("Daily Stats")
    print("—" * 12)
    print("\nHere are your stats for today:")
    print(f"\nWater Intake (oz): {daily_water}")
    print(f"\nTime meditated (minutes): {daily_meditation}")
    input("\nPress ENTER to return to the main menu.")

if __name__ == "__main__":
    main()