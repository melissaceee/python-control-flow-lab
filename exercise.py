#exercise 1
def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    def weather_advice():
    # Prompt the user to determine if it's cold
    cold = input("Is it cold? (yes/no): ").strip().lower()
    # Prompt the user to determine if it's raining
    raining = input("Is it raining? (yes/no): ").strip().lower()
    
    # Determine clothing advice based on the conditions
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    elif cold == "no" and raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please enter 'yes' or 'no' for both questions.")

# Call the function
weather_advice()
