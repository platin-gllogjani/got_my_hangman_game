A Game of Thrones-themed ASCII Hangman game in Python



## Project Description

The game presents the player with a Game of Thrones-related word or phrase, and they must guess it one letter at a time. The game features ASCII art to visually display the hangman state and remaining lives in the form of hearts. The player can choose between three difficulty levels: Easy, Medium, and Hard. Higher difficulties contain more complex and longer phrases but do not affect the number of lives.

---

## How to Run

1. Ensure Python 3 is installed on your machine.
2. Download or clone this repository.
3. Navigate to the project folder in a terminal.

## Project Requirements and How They Were Met

- **Functions**: Met by using `play_game()`, `get_random_word()`, `display_state()`, and `get_difficulty()` to structure the code.
  
- **Lists, Dictionaries, Tuples**:  
  - Lists store guessed letters and word banks.  
  - Dictionaries hold ASCII art for the hangman.  
  - Tuples group visual states for game progress.

- **User Input & Validation**:  
  User input is collected for difficulty and guesses, with checks to ensure valid entries.

- **If/Else Statements & Loops**:  
  Used to control game flow, check win/loss conditions, and repeat prompts.

- **Random Generation**:  
  Words are selected randomly from predefined lists using `random.choice()`.

