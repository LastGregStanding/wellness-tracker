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

# Main Menu
def main_menu_prompt(name):
        print("\n" + "—" * 15)
        print("Main Menu")
        print("—" * 15)
        print(f"\n{name}, what would you like to do?\n")
        print("1) Log 8oz water         (type '1' or 'water')")
        print("2) Log meditation time   (type '2' or 'meditation')")
        print("3) View daily stats      (type '3' or 'stats')")
        print("4) Motivational Quote    (type '4' or 'quote')")
        print("5) Exit program          (type '5' or 'exit')")

# Prompt after doing an action
def post_action_prompt():
    print("\nPress ENTER to return to the main menu.")
    print("Press 'U' to Undo previous entry")
    
    if input("\nSelection: ").strip().lower() == 'u':
        confirm_undo()

# Welcome prompt
def welcome_prompt(): 
    print("—" * 21)
    print("Wellness Tracker v1.0")
    print("—" * 21)
    print("Get healthier by keeping track of your daily health goals.\n")
    print("Getting started takes less than 2 seconds!\n")

    name = input("Please enter your name: ").strip()

    print(f"\nWelcome, {name}! Opening your personal Wellness Tracker.")
    return name