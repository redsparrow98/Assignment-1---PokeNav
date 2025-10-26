# Pokémon Utility Console App

A small Python console program for university assignment 1.  
You interact with a menu that lets you run different text and data tools inspired by Pokémon.
This was written as a first-year programming task.
Focus was on loops, conditionals, data processing, and basic validation.

## Features

Menu options in the app:

| Option | Feature | What you do | What it prints |
|--------|---------|--------------|----------------|
| 1 | Exit program | Quit the menu | Goodbye message |
| 2 | Identify hashtags | Enter a text post | List of valid hashtags |
| 3 | Detect palindrome | Enter a Pokémon name | Palindrome check result |
| 4 | Create acronym | Enter a Pokémon name + number | Abbreviation in uppercase |
| 5 | Pokémon traits | Enter Pokémon name + type | Strengths and weaknesses |
| 6 | Zodiac + Eeveelution | Enter birth month | Zodiac + matching element and eeveelution |
| 7 | BMI calculator | Enter height + weight | BMI value + category |
| 8 | Fitness tracker | Enter 7 step counts | Average, standard deviation, most and least active day |

## Requirements

- Python 3.8 or later
- Standard library only (no extra installations)

## How to Run

```bash
python main.py
Follow the menu and input prompts.
```
## Code Structure
- Menu loop in main()
- One function per feature
- Helper functions for stats:
  - get_sum()
  - get_max_value()
  - get_min_value()
  - calculate_average()
  - calculate_standard_deviation()
  - get_min_value()
  - calculate_average()
  - calculate_standard_deviation()

## What I Learned

- Designing user-driven console programs
- Validating and converting user input
- Working with lists, strings, and conditionals
- Writing reusable helper functions
- Basic numerical calculations (average, standard deviation)

## Future Improvements

- Better error handling and input retry
- Add tests for helper functions
- Replace magic numbers with clearer constants (BMI ranges, zodiac mapping)
- Cleaner separation of logic and user interaction
