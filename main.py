from tracker_actions import print_quote
from tracker_actions import log_water, log_meditation, view_stats
from prompts import main_menu_prompt, welcome_prompt

# Welcome Screen
def main():
    name = welcome_prompt()
    show_main_menu(name)

# Main Menu 
def show_main_menu(name):
    while True:
        main_menu_prompt(name)
        choice = input("\nSelection: ").strip().lower()

        if choice in ['1', 'water']:
            log_water()
        elif choice in ['2', 'meditation']:
            log_meditation(name)
        elif choice in ['3', 'stats']:
            view_stats()
        elif choice in ['4', 'quote']:  
            print_quote()
        elif choice in ['5', 'exit']:  
            print("Closing tracker. Stay healthy!")
            break

if __name__ == "__main__":
    main()