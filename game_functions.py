import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = poss_values[len(poss_values) // 2]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val and user_input == 'h':
        return True
    elif next_val < current_val and user_input == 'l':
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    for index, character in enumerate(word):
        if character == letter:
            board[index] = letter
    for index, character in enumerate(word):
        if letter in word:
            print(f"Well done! {letter} is in the word")
            return True
        else:
            print(f"Sorry, {letter} is not in the word")
            return False
