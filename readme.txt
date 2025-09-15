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
*Sayara

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
*Sayara

=========================================================================================================

task 8: Fitness and Health Tracking
*Nat

I found this task challenging as I kept getting stuck on different parts and had to do a lot of googling
After the functions lecture we had I decided to break this problem into multiple functions to 
avoid blob code since originally i had the whole function rack_fitness_and_health() check and do multiple things

I believe that each function is self contained and can be reused:
calculate_average()
calculate_standard_deviation()
check_most_active_day()
check_least_active_day()
rack_fitness_and_health()

WHts i struggled the most with was how to on how to print only the last most/ least active day in case of 
multiple same entires.

my solution:
-I create a weekdays list with same order of days as the input of steps list.
-I initialized the most_active_day_index variable 
-Then i decided on suing the for loop to iterate through the steps list in the range of the amount of items 
in the list (6)
-Each time I found a value equal to the max_steps I updated most_active_day_index to be the iterating index
-This meant that if there is a same max_steps value at the end of the steps list it will update the
most_active_day_index to the last appearance of the max_steps value.
-Finally, I created most_active_day by selecting the weekday list element (weekday string) corresponding to 
most_active_day_index which was used in the final print output

same was applied to the least solution.

Concepts used:
-variables      -for loops                  -functions
-input          -lists                      -conditionals
-printing       -string manipulation


=========================================================================================================

task 9: 

Task 1: Menu error Nat/Harshani ✅

Task 2: No hashtags found error Nat ✅

Task 5: Invalid type Nat ✅

task 6: Invalid month index 

task 7: missing inputs 

task 8: Invalid input Nat ✅

=========================================================================================================