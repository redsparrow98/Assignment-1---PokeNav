* We used Git/GitHub version control while working on this assignment to make independent work also 
possible

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
- while iterating trough the character in each word checks if character is a # AND if it does match 
  check that word is not already in the hashtags_list if both are true the words gets appended to the list.
- As part of error handling if checks the length of the hashtag_list and if its 0 (meaning empty) it prints
  "No hashtags found."
- If the list is not empty then it prints the items in the list


Concepts used:
-variables      -for loops                  -functions
-input          -lists                      -conditionals
-printing       -string manipulation

=========================================================================================================

Task 3: Detect a Palindrome
*Harshani

This task requires to detect palindrome in user inputs(names).

I completed this task by creating a function which;
- reads a user input.
- iterates the user input (for loop) to rearrange each character in a reverse order.
- if else statements have been used to check if the name and the reversed name are a match or not.
- if it is a match, prints that "the name is palindrome".
- if not, prints that "the name is not a palindrome".


Concepts used:
-variables      -for loops                  -functions
-input          -conditionals
-printing       -string manipulation


=========================================================================================================

Task 4: Create an Acronym
*Sayara

I created a function that asks the user to enter a Pokemon name and a shortening factor(n). Then it starts with the n'th letter of the name and creates an acronym by combining all the n'th letters. Eventually the final acronym is displayed in uppercase.

Steps:
-takes user input for name and shortening factor
-iterates through the name starting from n'th letter and takes every n'th letter afterwards
-each selected letter added to a new string
-eventually the final acronym is displayed in uppercase

Concepts used:
-variables
-input
-printing
-conditionals (if....else)
-string manipulation 

=========================================================================================================

Task 5: Get Pokémon Traits
*Nat

Created another function for this module of the program.
Description of the function:
- The function asks for name of the Pokemon and the type of the pokemon, I decided to capitalize the type
  input due to the assignment specifications stating that this input is case sensitive and i wanted to ensure
  to avoid any errors in case input is not capitalized.
- Then the function runs a conditional to check for the users type input and based on the user type it prints 
  output to the user to show them the weaknesses and strengths against other types f Pokemons
- As part of error handling if the user inputted type doesn't match any of the criteria it prints an error 
  message and returns to main menu.

type strength rules:
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

I completed this task by creating a function to find zodiac sign and eeveelution.

explanation of the function:
- reads user input.
- creates a list of zodiac signs.
- prints the zodiac sign corresponding to the month.
- uses if elif statements to find the element and eeveelution corresponding to the zodiac and prints the result accordingly.
- covers the error handling with an if statement. (if the input is equal or less than 0 or greater than 12 and prints an error message.)

concepts used:
-variables      -functions
-input          -conditionals
-printing       -lists


=========================================================================================================

Task 7: Implement Body Mass Index (BMI) Based on Height and Weight
*Sayara

Created another unique function to calculate the BMI.

this time I kinda struggled with rounding the bmi value as this was a requirement and since we were not allowed to use the round function. Initially I was trying to use the round function to calculate the bmi but then I just decided to convert the final result to rounded to 2 decimal values rather than converting the whole calculation by using round function.

explanation of the function:
-takes user input for height and weight (declared the variables as float since they might be float values as well)
-checks if the values are valid or not which was essentially a part of the error handling.
-then if the values are valid then calculates the bmi using the formula.
-compares the bmi against a set of ranges to determine the health category of the Pokémon.
- finally prints the bmi with rounded value to 2 decimal places along with the health category.
-as a part of the error handling if the user inputs any negative number the program shows an error message and returns to main menu.

concepts used:
-variables                 
-input         
-printing 
-functions 
-conditionals (if, elif, else)  
=========================================================================================================

task 8: Fitness and Health Tracking
*Nat

Functions created because we are told we are not allowed to use the built in sum(), min(), max(), mean():
calculate_average()
get_sum()
get_max_value()
get_min_value()
calculate_standard_deviation()

main function for this task:
rack_fitness_and_health()


Function description:
- Reads user input for the steps per day
- Creates a steps list by splitting the user input string 
- since it was confirmed we are not allowed to use map() i had to iterate trough the steps list
  and cast each element in the list to an integer and append to a new list of the same elements just
  of integer type so i cna do all the calculations needed for this task.
- Error handling checks if the user had exactly 7 days worth of data separated by coma, if not prints an error
  and returns to main menu if the number of entries is correct proceeds with the rest of the code.
- Calculates the average
- Calculates the standard deviation
- Finds the most and least active day in the weekday
- Prints all the health tracking stats as requested

*What I struggled the most with was how to on how to print only the last most/ least active day in case of 
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

task 6: Invalid month index ✅

task 7: Invalid inputs Sayara ✅

task 8: Invalid input Nat ✅

=========================================================================================================