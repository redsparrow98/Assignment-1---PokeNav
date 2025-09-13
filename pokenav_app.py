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
"""
    
    print(menu)
    option = int(input("Type your option: "))
    return option

def identify_hashtags():
    """
    Ask the user to enter a post, extract words that contain a hashtag (#),
    and print the unique hashtags found.

    Steps:
        1. Read user input and split() it into list of words.
        2. Check each word for the '#' character.
        3. Add the word to a hashtag list if not already included.
        4. Print all hashtags found.
    """
    post = input("Type your post: ")
    words_list = post.split()

    hashtag_list = []
    for word in words_list:
        for char in word:
            if char == "#" and word not in hashtag_list:
                hashtag_list.append(word)
    
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

def get_pokemon_traits():
    """
    Ask the user for a Pokemon name and type, then print a message
    showing its strengths and weaknesses against each type.

    Rules:
        - Fire is strong against Grass, weak against Water.
        - Water is strong against Fire, weak against Grass.
        - Grass is strong against Water, weak against Fire.
    """

    name = input("Type your Pokemon name: ")
    type = input("Type your Pokemon type: ").capitalize()

    if type == "Fire":
        print(f"{name} is a {type}-type Pokemon! It is strong against Grass-type Pokemons and weak against Water-type Pokemons.")
    elif type == "Water":
        print(f"{name} is a {type}-type Pokemon! It is strong against Fire-type Pokemons and weak against Grass-type Pokemons.")
    else:
        print(f"{name} is a {type}-type Pokemon! It is strong against Water-type Pokemons and weak against Fire-type Pokemons.")

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


game_on = True

while game_on:
    option = menu_screen()

    if option == 1:
        print("Thank you for playing! See you next time!")
        game_on = False
    elif option == 2:
        identify_hashtags()
    elif option == 3:
        detect_palindrome()
    elif option == 4:
        print("Create an acronym")
    elif option == 5:
        get_pokemon_traits()
    elif option == 6:
        find_zodiac_and_eeveelution()
    elif option == 7:
        print("BMI calculator")

