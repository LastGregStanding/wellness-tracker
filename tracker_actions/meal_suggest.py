from middleware.meal_recommender import request_meal

CALORIE_LIMITS = {
    "1": 600,
    "2": 900,
    "3": 1200,
    "600": 600,
    "900": 900,
    "1200": 1200,
}

# Cuisine options
CUISINES = [
    "Italian", "Mexican", "Japanese", "Chinese",
    "American", "Vegan", "Indian", "Thai", "Mediterranean",
]

# User chooses calorie goal
def get_calorie_choice():
    print("\nHow many calories are you trying to consume for the meal?")
    print("1) Under 600             (type '1' or '600')")
    print("2) Under 900             (type '2' or '900')")
    print("3) Under 1200            (type '3' or '1200')")

    while True:
        choice = input("\nSelection: ").strip()
        if choice in CALORIE_LIMITS:
            return CALORIE_LIMITS[choice]
        print("Invalid choice. Try again!")

# Ask user for protein preference
def get_protein_preference():
    while True:
        answer = input("\nDo you want the meal to be heavy on protein (yes/no)? ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Invalid choice. Try again!")

# User chooses cuisine
def get_cuisine_preference():
    print("\nWhat type of cuisine are you in the mood for?")
    print("1)  Italian              (type '1' or 'italian')")
    print("2)  Mexican              (type '2' or 'mexican')")
    print("3)  Japanese             (type '3' or 'japanese')")
    print("4)  Chinese              (type '4' or 'chinese')")
    print("5)  American             (type '5' or 'american')")
    print("6)  Vegan                (type '6' or 'vegan')")
    print("7)  Indian               (type '7' or 'indian')")
    print("8)  Thai                 (type '8' or 'thai')")
    print("9)  Mediterranean        (type '9' or 'mediterranean')")
    
    while True:
        choice = input("\nSelection: ").strip().lower()
        if choice.isdigit():
            choice_digit = int(choice)
            if 1 <= choice_digit <= len(CUISINES):
                return CUISINES[idx - 1]
        elif choice in [cuisine.lower() for cuisine in CUISINES]:
            return choice.capitalize()
        
        # Invalid choice
        print(f"Please enter a number between 1 and 9, or type the cuisine name.")

# Print meal to user
def display_meal(meal):
    print(f"\nMeal: {meal['name']}")
    print(f"Description: {meal['description']}")
    print(f"Calories: {meal['calories']}")

def meal_suggest():
    calorie_limit = get_calorie_choice()
    high_protein = get_protein_preference()
    cuisine = get_cuisine_preference()

    filters = {
        "calories": calorie_limit,
        "high_protein": high_protein,
        "cuisine": cuisine,
        "exclude": []
    }

    for _ in range(3):
        meal = request_meal(filters)
        display_meal(meal)
        filters["exclude"].append(meal["name"])

        # Offer a different meal
        again = input("\nWould you like another choice? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break
