from prompts import post_action_prompt

# Track your water
def log_water():
    global daily_water, last_action
    amount = 8
    daily_water += amount
    last_action = {"type": "water", "amount": amount}
    
    print(f"\nSuccess! You added {amount}oz of water to your daily water intake.")
    post_action_prompt()