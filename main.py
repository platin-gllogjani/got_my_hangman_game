# I used ASCII Art for this which you cann see below:
# Hangman: https://ascii.co.uk/art/hangman


import random

# tuples consdering these will not change
HANGMAN_PICS = (
    """
     ------
     |    |
     |    
     |   
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |   
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
    _|_
    """
)

hearts = ["❤️", "❤️", "❤️", "❤️", "❤️", "❤️"]

# Dictionary of words per difficulty
word_bank = {
    "easy": [
        "snow", "wolf", "king", "wall", "stark"
    ],
    "medium": [
        "winterfell", "dragons", "lannister", "wildling", "tyrion"
    ],
    "hard": [
        "winter is coming",
        "valar morghulis",
        "you know nothing",
        "fire and blood",
        "hold the door"
    ]
}


#Fun intro for those who have seen Game of Thrones
def intro():
    print("\n" + "="*60)
    print("🧝‍♂️ Welcome to 'Game of Thrones: The Final Guess' ⚔️")
    print("The fate of the Seven Kingdoms lies in your hands...")
    print("Each wrong guess brings you closer to the gallows.")
    print("You have 6 hearts. Choose wisely. Speak bravely.\n")
    print("Note: Difficulty affects the word's complexity (not lives).\n")
    print("="*60 + "\n")

def choose_word(difficulty):
    return random.choice(word_bank[difficulty])

def display_status(wrong_guesses):
    print(HANGMAN_PICS[wrong_guesses])
    print("Lives:", " ".join(hearts[:len(hearts) - wrong_guesses]))

def display_word_state(word, guessed_letters):
    return " ".join([char if char in guessed_letters or char == " " else "_" for char in word])

def play_game():
    intro()
    difficulty = input("Choose your challenge (easy / medium / hard): ").strip().lower()

    if difficulty not in word_bank:
        print("Unrecognized house... defaulting to 'easy'.")
        difficulty = "easy"

    word = choose_word(difficulty)
    guessed_letters = []
    wrong_guesses = 0
    max_guesses = len(HANGMAN_PICS) - 1

    while wrong_guesses < max_guesses:
        display_status(wrong_guesses)
        print("\nWord:", display_word_state(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Only one letter at a time, my lord.")
            continue

        elif guess in guessed_letters:
            print("You’ve spoken that letter already.")
            continue

        if guess in word:
            print("A wise move.")
        else:
            print("A dire mistake...")
            wrong_guesses += 1

        guessed_letters.append(guess)

        if all(char in guessed_letters or char == " " for char in word):
            print("\n🏆 You have triumphed! The realm is saved!")
            print("The word was:", word)
            break
    else:
        display_status(wrong_guesses)
        print("\n💀 You have fallen. The word was:", word)
        print("Your watch has ended...")

# Run the Game
play_game()
