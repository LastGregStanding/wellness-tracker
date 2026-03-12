from middleware.request_workout import request_workout
from middleware.request_weather import request_weather
import state

# Ask user for zip code to get weather data
def get_location():
    zip_code = input(f"\nWhat is your zip code, {state.name}? ").strip()
    return zip_code

# Determine if user should workout inside or outside
def determine_indoor_outdoor(weather):
    # If temp is below 60 or WMO code is above 3, suggest indoor
    temp = float(weather["temperature_f"])
    wmo_code = int(weather["wmo_code"])

    if temp < 60 or wmo_code > 3:
        return "indoor"
    else:
        return "outdoor"

# Ask user what type of workout they desire
def get_workout_type():
    print("\nWould you like to do cardio, weight lifting, or something actually fun?")
    print("1) Cardio                          (type '1' or 'cardio')")
    print("2) Weight Lifting                  (type '2' or 'lifting')")
    print("3) Something actually fun          (type '3' or 'fun')")

    choice = input("\nSelection: ").strip().lower()

    if choice in ("1", "cardio"):
        return "cardio"
    elif choice in ("2", "lifting"):
        return "lifting"
    elif choice in ("3", "fun"):
        return "recreational"

# User chose lifting
def get_lifting_category():
    print("\nWhat would you like to work on?")
    print("1) Upper Body    (type '1' or 'upper')")
    print("2) Lower Body    (type '2' or 'lower')")
    print("3) Full Body     (type '3' or 'full')")

    choice = input("\nSelection: ").strip().lower()

    if choice in ("1", "upper"):
        return "upper"
    elif choice in ("2", "lower"):
        return "lower"
    elif choice in ("3", "full"):
        return "full"


def display_cardio(workout):
    print(f"\nWorkout:     {workout['name']}")
    print(f"Description: {workout['description']}")
    print(f"Calories burned in 30 min: {workout['calories_per_30_min']}")


def display_weightlifting(workout):
    print(f"\nWorkout: {workout['name']}")
    for exercise in workout["exercises"]:
        print(f"  - {exercise['name']}: {exercise['sets']} sets of {exercise['reps']} reps")


def display_recreational(workout):
    print(f"\nSport:       {workout['name']}")
    print(f"Description: {workout['description']}")
    print(f"Calories burned in 30 min: {workout['calories_per_30_min']}")


def workout_suggest():
    # Get user zip code
    zip_code = get_location()
    # Get weather data
    weather = request_weather(zip_code)
    
    city = weather["location"]
    temp = weather["temperature_f"]
    condition = weather["condition"]
    location_for_workout = determine_indoor_outdoor(weather)

    print(f"\nThat's awesome you live in {city}!")
    print(f"The temperature is currently {temp} degrees with {condition.lower()}.")
    print(f"For this weather, I suggest an {location_for_workout} exercise.")

    # Ask user what type of workout they desire
    workout_type = get_workout_type()

    exclude = []

    for _ in range(3):
        filters = {
            "workout_type": workout_type,
            "location": location_for_workout,
            "exclude": exclude,
        }

        if workout_type == "lifting" and not exclude:
            category = get_lifting_category()
            filters["category"] = category
        elif workout_type == "lifting":
            filters["category"] = category

        workout = request_workout(filters)

        # Ran out of workout options
        if not workout:
            print("\nNo more workouts to fit your preferences!")
            break

        if workout_type == "cardio":
            display_cardio(workout)
        elif workout_type == "lifting":
            display_weightlifting(workout)
        elif workout_type == "recreational":
            display_recreational(workout)

        exclude.append(workout["name"])

        # Ask user if they want a different workout
        again = input("\nWould you like a different recommendation? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break

    print(f"\nHave a great workout, {state.name}!")
