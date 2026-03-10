# View your daily stats
def view_stats():
    print("\n" + "—" * 12)
    print("Daily Stats")
    print("—" * 12)
    print("\nHere are your stats for today:")
    print(f"\nWater Intake (oz): {daily_water}")
    print(f"\nTime meditated (minutes): {daily_meditation}")

    input("\nPress ENTER to return to the main menu.")