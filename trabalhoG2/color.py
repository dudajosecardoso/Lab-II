import random

def coloring(secret_word, user_attempt):
    WHITE = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

    word_letters = []

    for letter in secret_word:
        word_letters += letter
    
    letter1 = user_attempt[0]
    letter2 = user_attempt[1]
    letter3 = user_attempt[2]
    letter4 = user_attempt[3]
    letter5 = user_attempt[4]


    if letter1 == secret_word[0]:
            letter1 = f'{GREEN}{user_attempt[0]}{WHITE}'
    elif letter1 in word_letters:
        letter1 = f'{YELLOW}{user_attempt[0]}{WHITE}'
    
    if letter2 == secret_word[1]:
            letter2 = f'{GREEN}{user_attempt[1]}{WHITE}'
    elif letter2 in word_letters:
        letter2 = f'{YELLOW}{user_attempt[1]}{WHITE}'
    
    if letter3 == secret_word[2]:
            letter3 = f'{GREEN}{user_attempt[2]}{WHITE}'
    elif letter3 in word_letters:
        letter3 = f'{YELLOW}{user_attempt[2]}{WHITE}'

    if letter4 == secret_word[3]:
            letter4 = f'{GREEN}{user_attempt[3]}{WHITE}'
    elif letter4 in word_letters:
        letter4 = f'{YELLOW}{user_attempt[3]}{WHITE}'
    
    if letter5 == secret_word[4]:
            letter5 = f'{GREEN}{user_attempt[4]}{WHITE}'
    if letter5 in word_letters:
        letter5 = f'{YELLOW}{user_attempt[4]}{WHITE}'
    
    print(f'\n| {letter1} | {letter2} | {letter3} | {letter4} | {letter5} |\n')
