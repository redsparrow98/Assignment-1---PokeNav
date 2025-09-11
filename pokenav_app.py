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
    - Reads user post input and creates a words_list by splitting each word in the post.
    - Declares an empty list for storing the hashtags.
    - Uses a nested for loop to iterate trough all the words in the words_list and then to iterate
    trough each character in that word.
    - while iterating trough the character in each word checks if any character is # AND if it does match also
    check that word is not already in the hashtags_list if both are true the words gets appended to the list.
    - Prints the items in the list
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


game_on = True

while game_on:
    option = menu_screen()

    if option == 1:
        print("Thank you for playing! See you next time!")
        game_on = False
    elif option == 2:
        identify_hashtags()
    elif option == 3:
        print("Detect a palindrome")
    elif option == 4:
        print("Create an acronym")
    elif option == 5:
        print("Get Pokemon traits")
    elif option == 6:
        print("Match zodiac sign and elements")
    elif option == 7:
        print("BMI calculator")