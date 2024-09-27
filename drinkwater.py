import time

def drink_water_reminder():
    total_water_intake = 0
    goal_water_intake = 8
    interval = 60 * 30

    print("Welcome to the Drink Water Game!")
    print(f"Your goal today is to drink {goal_water_intake} glasses of water.")

    while total_water_intake < goal_water_intake:
        print("\nTime to drink water!")
        user_input = input("Did you drink a glass of water? (yes/no): ").lower()

        if user_input == "yes":
            total_water_intake += 1
            print(f"Good job! You've drunk {total_water_intake} out of {goal_water_intake} glasses of water today.")
        else:
            print("Don't forget to drink water. Staying hydrated is important!")

        if total_water_intake < goal_water_intake:
            print("Next reminder in 30 minutes.")
            time.sleep(interval)
    print("\nCongratulations! You've reached your daily water goal!")
    print(f"Total water intake: {total_water_intake} glasses.")

drink_water_reminder()
