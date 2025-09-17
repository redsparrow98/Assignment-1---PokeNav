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
8. Fitness and Health Tracking
"""
    
    print(menu)
    option = int(input("Type your option: "))
    return option

def identify_hashtags(post_str):
    """
    Take a post parameter and extract words that contain a hashtag (#),
    and if # is found print the unique hashtags, if no # found print no hashtags found.

    Steps:
        1. create a word_list from the post parameter by splitting the string.
        2. Check each word for the '#' character.
        3. Add the word to a hashtag list if not already included.
        4. Print all hashtags found.
    """
    words_list = post_str.split()

    hashtag_list = []
    for word in words_list:
        for char in word:
            if char == "#" and word not in hashtag_list:
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

    for i in name:
        reversed_name = i + reversed_name

    if name.lower() == reversed_name.lower():
        print(f"The name ‘{name}’ is a palindrome.")
    else:
        print(f"The name ‘{name}’ is not a palindrome.")

def get_pokemon_traits(name, type):
    """
    Take Pokemon name and type parameters, then print a message showing its strengths and weaknesses against each type.

    Rules:
        - Fire is strong against Grass, weak against Water.
        - Water is strong against Fire, weak against Grass.
        - Grass is strong against Water, weak against Fire.
    """

    if type == "Fire":
        print(f"{name} is a {type}-type Pokemon! It is strong against Grass-type Pokemons and weak against Water-type Pokemons.")
    elif type == "Water":
        print(f"{name} is a {type}-type Pokemon! It is strong against Fire-type Pokemons and weak against Grass-type Pokemons.")
    elif type == "Grass":
        print(f"{name} is a {type}-type Pokemon! It is strong against Water-type Pokemons and weak against Fire-type Pokemons.")
    else:
        print("Error - The Pokemon type provided is not valid. Valid types: Water, Fire, Grass.")

def find_zodiac_and_eeveelution():
    """ 
    Ask the user for birth_month.
    Print the zodiac corresponding to the birth_month.
    print the element and eeveelution corresponding to the zodiac.

    """
    zodiac_sign = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

    birth_month = (int(input("Type your birth month: "))) - 1

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
    Gets a sum value of all the integer list of items
    and returns a sum
    """
    sum = 0
    for i in integer_list:
        sum += i
    return sum

def get_max_value(integer_list):
    """
    Gets the biggest value from the list of integers
    returns the max_value
    """
    max_value = integer_list[0]
    for i in integer_list:
        if i > max_value:
            max_value = i
    return max_value

def get_min_value(integer_list):
    """
    Gest the smallest value in the list of integers
    returns the min_value
    """
    min_value = integer_list[0]
    for i in integer_list:
        if i < min_value:
            min_value = i
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

    required parameters:
        integer_list (list of integers) - which will be the data set for calculation
        average - needs to be the mean of the data set (integer_list)

    returns std_deviation, a single float value representing the population standard deviation.
    """
    squared_diff = []
    for i in integer_lis:
        squared_diff.append((i - average) ** 2)
    std_deviation = math.sqrt(get_sum(squared_diff) / len(integer_lis))
    return std_deviation

def check_most_active_day(integer_list):
    """
    -It keeps a list of weekdays that matches each index of the users step input.
    -It finds the largest number in the step list.
    -It loops through the list to compare each value with that largest number.
    -When it finds a match, it updates the most_active_day_index. If there are multiple matches, the index of the last match is kept.
    -It uses that index to get the weekday from the weekday list.

    required parameter:
        integer_list (list pf integers)

    It returns the weekday string as the most active day.
    """
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    max_steps = get_max_value(integer_list)
    most_active_day_index = None

    for index in range(len(integer_list)):
        if integer_list[index] == max_steps:
            most_active_day_index = index
    most_active_day = weekdays[most_active_day_index]
    return most_active_day

def check_least_active_day(integer_list):
    """
    -It keeps a list of weekdays that matches each index of the users step input.
    -It finds the smallest number in the integer_list.
    -It loops through the list to compare each value with that smallest number.
    -When it finds a match, it updates the least_active_day_index. If there are multiple matches, the index of the last match is kept.
    -It uses that index to get the weekday from the weekday list.
    -It returns the weekday as the least active day.

    required parameter:
        integer_list (list pf integers)

    It returns the weekday string as the least active day.
    """

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    min_steps = get_min_value(integer_list)
    least_active_day_index = None

    for index in range(len(integer_list)):
        if integer_list[index] == min_steps:
            least_active_day_index = index
    least_active_day = weekdays[least_active_day_index]
    return least_active_day

def track_fitness_and_health(steps):
    """
    The function tracking_fitness_and_health(steps) processes a users weekly step counts and prints fitness statistics.
    It takes the input steps as a string of numbers separated by commas.
    It splits the string and converts each number into an integer so calculations can be done.
    It checks if the user entered exactly 7 numbers (one for each day of the week). If not, it prints an error message.
    
    If the input is valid:
    It calculates the average daily steps.
    It calculates the standard deviation of the steps.
    It finds the most active day (highest steps).
    It finds the least active day (lowest steps).

    Finally, it prints the average with standard deviation, and shows which day was most active and least active.
    """
    # Create a list of steps of type integer so we can do calculations.
    steps_list = steps.split(",")
    steps_list_integers = []
    for x in steps_list:
        type_cast = int(x)
        steps_list_integers.append(type_cast)

    if len(steps_list) != 7:
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {len(steps_list_integers)} numbers.")
    else:
        average = calculate_average(steps_list_integers)
        std_steps = calculate_standard_deviation(steps_list_integers, average)
        
        most_active_day = check_most_active_day(steps_list_integers)
        least_active_day = check_least_active_day(steps_list_integers)

        print(f"Steps Statistics: {average:.2f} + / - {std_steps:.2f} per day.")
        print(f"Most active day: {most_active_day}. Least active day: {least_active_day}.")


option = 0

while option != 1:
    option = menu_screen()

    if option == 1:
        print("Thank you for playing! See you next time!")
    elif option == 2:
        post = input("Type your post: ")
        identify_hashtags(post)
    elif option == 3:
        detect_palindrome()
    elif option == 4:
        print("Create an acronym")
    elif option == 5:
        name = input("Type your Pokemon name: ")
        type = input("Type your Pokemon type: ").capitalize()
        get_pokemon_traits(name, type)
    elif option == 6:
        find_zodiac_and_eeveelution()
    elif option == 7:
        print("BMI calculator")
    elif option == 8:
        steps_input = input("Step count per day: ")
        track_fitness_and_health(steps_input)
    else:
        print("Error - Invalid option. Please input a number between 1 and 8.")
