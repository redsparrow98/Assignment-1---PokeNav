* We used Git/GitHub version control while working on this assignment to make independent and separated
team work possible.

below is the requested explanation on how we separated the tasks and on which ones we worked together

=========================================================================================================

Task 1: Creating the PokéNav Menu
*Nat and Harshani

Initially we had a variable storing an f-string with the menu options, but after discussing and agreeing
that this program will need to run on a while loop and the fact that the menu will need to keep showing
after each section is finalized we agreed to create a menu_scree() function.

This makes the whole code more readable and modular which makes it easier to update and change over time

Concepts used:
-variables
-input
-printing 

=========================================================================================================

Task 2: Identify Hashtags
*Nat

I completed this task by creating a function to detect the # in a post.
explanation of the function:
- Reads user post input and creates a words_list by splitting each word in the post.
- Declares an empty list for storing the hashtags.
- Uses a nested for loop to iterate trough all the words in the words_list and then to iterate trough
  each character in that word.
- while iterating trough the character in each word checks if any character is # AND if it does match 
  also check that word is not already in the hashtags_list if both are true the words gets appended to the list.
- Prints the items in the list

The reason why I used a function is for code readability and ease of updating and maintaining
each aspect of the of the program in the future.


Concepts used:
-variables      -for loops                  -functions
-input          -lists                      -conditionals
-printing       -string manipulation

=========================================================================================================

Task 3: Detect a Palindrome
*Harshani

=========================================================================================================

Task 4: Create an Acronym
*Tharaka

=========================================================================================================

Task 5: Get Pokémon Traits
*Nat

Created another function for this module of the program.
The function asks for name of the Pokemon and the type of the pokemon, I decided to capitalize the type
input due to the assignment specifications stating that this input is case sensitive and i wanted to ensure
to avoid any errors in case input is not capitalized.

I then created a conditional to check for the users type input and based on that i created a print output
to the user to show them the weaknesses and strengths against other types f Pokemons

I used below given guide on the the Types.
# Fire-types are weak against Water-types and strong against Grass-types
# Water-types are weak against Grass-types and strong against Fire-types
# Grass-types are weak against Fire-types and strong against Water-types


Concepts used:
-variables      -functions
-input          -conditionals
-printing       -string manipulation

=========================================================================================================

Task 6: Zodiac Sign and Eeveelution
*Harshani

=========================================================================================================

Task 7: Implement Body Mass Index (BMI) Based on Height and Weight
*Tharaka

=========================================================================================================

task 8:

=========================================================================================================

task 9: 

=========================================================================================================