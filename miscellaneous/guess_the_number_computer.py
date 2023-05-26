import random


def guess(n):
    random_number = random.randint(1, n)
    guess = 0
    while guess != random_number:
        guess = int(input(f'enter the number between 1 and {n}:'))
        if guess < random_number:
            print('sorry, guess again, too low.')
        elif guess > random_number:
            print('sorry, guess again. Too high.')
    print(f'Yay. congrats. You have guessed the number {random_number} correctly!')


guess(10)
