#exercise 1
def check_letter():
    letter = input("Please enter a letter (a-z or A-Z): ").lower()


    if len(letter) == 1 and letter.isalpha():
   
        vowels = "aeiou"
        
    
        if letter in vowels:
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single letter (a-z or A-Z).")


check_letter()


def check_voting_eligibility():

    voting_age = 18
    

    try:
        age = int(input("Please enter your age: "))
        
    
        if age < 0:
            print("Invalid age. Age cannot be negative.")
        elif age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote yet.")

    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")


check_voting_eligibility()

#exercise 3

def calculate_dog_years():

    try:
        age = int(input("Input a dog's age: "))
        

        if age < 0:
            print("Invalid age. Age cannot be negative.")
        else:
   
            if age == 1:
                dog_years = 10
            elif age == 2:
                dog_years = 20
            else:
            
                dog_years = 20 + (age - 2) * 7

            print(f"The dog's age in dog years is {dog_years}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")


calculate_dog_years()


#exercise 4


def weather_advice():

    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()
    
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


weather_advice()

#exercise 5


def determine_season():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    month = input("Enter the month of the year (Jan - Dec): ").strip().title()
    
    if month not in months:
        print("Invalid month. Please enter a three-letter month abbreviation (e.g., Jan, Feb).")
        return
    
    try:
        day = int(input("Enter the day of the month: "))
        
        if day < 1 or day > 31:
            print("Invalid day. Please enter a day between 1 and 31.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric day.")
        return
    
    if (month == "Dec" and day >= 21) or month in ["Jan", "Feb"] or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month in ["Apr", "May"] or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month in ["Jul", "Aug"] or (month == "Sep" and day <= 21):
        season = "Summer"
    elif (month == "Sep" and day >= 22) or month in ["Oct", "Nov"] or (month == "Dec" and day <= 20):
        season = "Fall"
    else:
        print("Could not determine the season for the provided date.")
        return
    
    print(f"{month} {day:02d} is in {season}.")

determine_season()

