import random


# def rock_paper_scissors():
#     choices = ['rock', 'paper', 'scissors']
#     comp_point = 0
#     user_point = 0
#     while comp_point != 5 and user_point != 5:
#         comp_choice = random.choice(choices)
#         user_choice = input('enter your choice, rock(R), paper(P), scissors(S):').lower()
#         print(comp_choice)
#         if comp_choice == 'rock':
#             if user_choice == 's':
#                 comp_point += 1
#             elif user_choice == 'p':
#                 user_point += 1
#             elif user_choice == 'r':
#                 user_point += 0
#                 comp_point += 0
#         elif comp_choice == 'paper':
#             if user_choice == 's':
#                 user_point += 1
#             elif user_choice == 'p':
#                 user_point += 0
#                 comp_point += 0
#             elif user_choice == 'r':
#                 comp_point += 1
#         else:
#             if user_choice == 'r':
#                 user_point += 1
#             elif user_choice == 'p':
#                 comp_point += 1
#             elif user_choice == 's':
#                 comp_point += 0
#                 user_point += 0
#         print(f'computer: {comp_point}\nuser:{user_point}')
#     if comp_point == 5:
#         print('computer wins!')
#     elif user_point == 5:
#         print('user wins!')
#
#
# rock_paper_scissors()


def play():
    user = input("what's your choice 'r' for rock 'p' for paper 's' for scissors:")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'You Won!'

    return 'You Lost!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(play())