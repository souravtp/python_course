import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('you have used these letters:', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        user_letter = input('guess the letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('lives:', lives)

            else:
                lives -= 1
                print('letter is not in the word. lives:', lives)

        elif user_letter in used_letters:
            print('you have already used that letter. Try different one. Lives: ', lives)

        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('you died, the word was', word)
    else:
        print('you guessed the word', word, '!!')

    play_again = input('press R to play again. Any key to exit').upper()
    if play_again == 'R':
        hangman()


hangman()
