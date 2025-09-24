import math


def menu_screen():
    menu = f"""
Welcome to the Main Menu. Choose one of the options below:

1. Exit
2. Identify hashtags
3. Detect a palindrome
4. Create an acronym
5. Get Pokemon traits
6. Match zodiac sign and element
7. BMI calculator 
8. Fitness and health tracker
"""
    
    print(menu)
    option = int(input("Type your option: "))
    return option

def identify_hashtags():
    """
    Reads user input for a post.
    Extracts words that contain a hashtag (#),
    If # is found print the unique hashtags, if no # found prints no hashtags found.
    """
    post = input("Type your post: ")
    words_list = post.split()

    hashtag_list = []
    for word in words_list:
        if word.startswith("#") and len(word) > 1:
            if "#" not in word[1:] and word not in hashtag_list:
                hashtag_list.append(word)
    
    if len(hashtag_list) == 0:
        print("No hashtags found.")
    else:
        print("Hashtags found:")
        for i in hashtag_list:
            print(i)

def detect_palindrome():
    """ 
    Ask the user for Pokemon name 
    Reverse the name to check if it is a palindrome.

    """
    name = input("Type your Pokemon name: ")
    reversed_name = ""

    for character in name:
        reversed_name = character + reversed_name

    if name.lower() == reversed_name.lower():
        print(f"The name '{name}' is a palindrome.")
    else:
        print(f"The name '{name}' is not a palindrome.")

def create_acronym():
    """
    Steps:
-takes user input for name and shortening factor
-iterates through the name starting from n'th letter and takes every n'th letter afterwards
-each selected letter added to a new string
-eventually the final acronym is displayed in uppercase
    """
    name = input("Type your Pokemon name: ")
    shortening_factor = int (input("Type your shortening factor: "))
    acronym = ""
    if shortening_factor > len(name):
        print("Abbreviated name: ")
    else: 
        for i in range (shortening_factor-1, len(name), shortening_factor):
            acronym += name[i]
        print (f"Abbreviated name: {acronym.upper()}")

def get_pokemon_traits():
    """
    Reads Pokemon name and type,
    Then prints a message showing the pokemons strengths and weaknesses against other types.

    Rules:
        - Fire is strong against Grass, weak against Water.
        - Water is strong against Fire, weak against Grass.
        - Grass is strong against Water, weak against Fire.
    """
    name = input("Type your Pokemon name: ")
    type = input("Type your Pokemon type: ").capitalize()

    if type == "Fire":
        print(f"{name} is a {type}-type Pokemon! It is strong against Grass-type"
                "Pokemons and weak against Water-type Pokemons.")
    elif type == "Water":
        print(f"{name} is a {type}-type Pokemon! It is strong against Fire-type"
                "Pokemons and weak against Grass-type Pokemons.")
    elif type == "Grass":
        print(f"{name} is a {type}-type Pokemon! It is strong against Water-type"
                "Pokemons and weak against Fire-type Pokemons.")
    else:
        print("Error - The Pokemon type provided is not valid. Valid types: Water, Fire, Grass.")

def find_zodiac_and_eeveelution():
    """ 
    Ask the user for birth_month.
    Print the zodiac corresponding to the birth_month.
    print the element and eeveelution corresponding to the zodiac.

    """
    zodiac_sign = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
                    "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

    birth_month = int(input("Type your birth month: "))

    # error handling

    if birth_month >= 13 or birth_month <= 0:
        print("Error - The month index provided is not valid. Choose between 1 and 12.")

    else:
        birth_month = birth_month - 1

        zodiac = (zodiac_sign[birth_month])
        print(f"Zodiac sign: {zodiac}")

        if zodiac == "Cancer" or zodiac == "Scorpio" or zodiac == "Pisces":
            print("Element: Water")
            print("Eeveelution: Vaporeon")
        elif zodiac == "Aries" or zodiac == "Leo" or zodiac == "Sagittarius":
            print("Element: Fire")
            print("Eeveelution: Flareon")
        elif zodiac == "Taurus" or zodiac == "Virgo" or zodiac == "Capricorn":
            print("Element: Earth")
            print("Eeveelution: Leafeon")
        elif zodiac == "Gemini" or zodiac == "Libra" or zodiac == "Aquarius":
            print("Element: Air")
            print("Eeveelution: Jolteon")

def get_sum(integer_list):
    """
    Gets a sum value of all the elements in the list of integers
    Returns the sum
    """
    sum = 0
    for number in integer_list:
        sum += number
    return sum

def get_max_value(integer_list):
    """
    Gets the biggest value in the list of integers
    returns the max_value
    """
    max_value = integer_list[0]
    for number in integer_list:
        if number > max_value:
            max_value = number
    return max_value

def get_min_value(integer_list):
    """
    Gest the smallest value in the list of integers
    returns the min_value
    """
    min_value = integer_list[0]
    for number in integer_list:
        if number < min_value:
            min_value = number
    return min_value

def calculate_average(integer_list):
    """
    Calculates the average of any list of integers
    and return than average.
    """
    list = integer_list
    average = get_sum(list) / len(list)

    return average

def calculate_standard_deviation(integer_lis, average):
    """
    calculates the population standard deviation of a list of integers.
    returns std_deviation, a single float value representing the population standard deviation.
    """
    squared_diff = []
    for number in integer_lis:
        squared_diff.append((number - average) ** 2)
    std_deviation = math.sqrt(get_sum(squared_diff) / len(integer_lis))
    return std_deviation

def calculate_bmi():
    """
    Steps:
    -asks the user to input height and weight
    -calculates the bmi using the formula
    -bmi is then compared to the set of ranges to determine Pkemons health category
    -lastly it prints the calculaued bmi (rounded to 2 decimal values) along with it's health category....

    Underweight: x < 29
    Healthy: 29 <= x < 53
    Overweight: 53 <= x < 85
    Obese: x >= 85

    """
    height = float(input("Type your Pokemon's height in meters: "))
    weight= float(input("Type your Pokemon's weight in kilograms: "))
    if height < 0 and weight <= 0:
        print ("error - height and weight must be positive numbers. ")
    elif height < 0:
        print ("error - height must be a positive number.")
    elif weight <= 0:
        print ("error - weight must be a positive number.") 
    else: 
        bmi = weight / (height**2)
        round_bmi = round(bmi, 2)
        if bmi < 29:
            category = "underweight"
        elif 29 <= bmi <53:
            category = "healthy"
        elif 53 <= bmi < 85:
            category = "overweight"
        else:
            category = "obese"

        print(f"BMI = {round_bmi:.2f}. The Pokemon is {category}.")

def track_fitness_and_health():
    """
    The function tracking_fitness_and_health(steps) processes a users weekly step counts and prints
    fitness statistics:
    
    - average steps per day
    - standard population deviation
    - most active day
    - least active day
    """
    steps_input = input("Step count per day: ")
    steps_list = steps_input.split(",")

    # error handling checks
    if steps_input == "":
        print(f"Error - Invalid input. The program needs 7 numbers; you typed 0 numbers.")
    elif len(steps_list) != 7:
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {len(steps_list)} numbers.")
    else:
        steps_list_integers = []
        for item in steps_list:
            type_cast = int(item)
            steps_list_integers.append(type_cast)

        average = calculate_average(steps_list_integers)
        std_steps = calculate_standard_deviation(steps_list_integers, average)


        # find the most and least active day 
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        max_steps = get_max_value(steps_list_integers)
        most_active_day_index = None
        for i in range(len(steps_list_integers)):
            if steps_list_integers[i] == max_steps:
                most_active_day_index = i
        most_active_day = weekdays[most_active_day_index]


        min_steps = get_min_value(steps_list_integers)
        least_active_day_index = None
        for i in range(len(steps_list_integers)):
            if steps_list_integers[i] == min_steps:
                least_active_day_index = i
        least_active_day = weekdays[least_active_day_index]

        print(f"Steps Statistics: {average:.2f} + / - {std_steps:.2f} per day.")
        print(f"Most active day: {most_active_day}. Least active day: {least_active_day}.")


option = 0

while option != 1:
    option = menu_screen()

    if option == 1:
        print("Thank you for playing! See you next time!")
    elif option == 2:
        identify_hashtags()
    elif option == 3:
        detect_palindrome()
    elif option == 4:
        create_acronym()
    elif option == 5:
        get_pokemon_traits()
    elif option == 6:
        find_zodiac_and_eeveelution()
    elif option == 7:
        calculate_bmi()
    elif option == 8:
        track_fitness_and_health()
    else:
        print("Error - Invalid option. Please input a number between 1 and 8.")
