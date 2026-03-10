from prompts import post_action_prompt
import state

# Track your water
def log_water():
    amount = 8
    state.daily_water += amount
    state.last_action = {"type": "water", "amount": amount}
    
    print(f"\nSuccess! You added {amount}oz of water to your daily water intake.")
    post_action_prompt()