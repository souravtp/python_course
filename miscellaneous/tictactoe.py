# # root = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9')]
# root = [[3*j+i+1 for i in range(3)] for j in range(3)]
# print(root)
import random


def table(lst):
    for i in range(3):
        for j in range(3):
            print('+-----', end='')
        print('+')
        for j in range(3):
            print('|  ' + lst[i][j] + '  ', end='')
        print('|')
    print('+-----' * 3 + '+')


def move(lst):
    user = int(input('enter your move:'))
    move_ = user - 1
    row = move_ // 3
    column = move_ % 3
    lst[row][column] = 'O'


def free_fields(lst):
    free = []
    for i in range(3):
        for j in range(3):
            if lst[i][j] not in ['O', 'X']:
                free.append((i, j))
    return free


def comp_move(lst):
    c_move = random.choice(free)
    row = c_move[0]
    col = c_move[1]
    lst[row][col] = 'X'


def win(lst, sgn):
    global who
    if sgn == 'O':
        who = 'player'
    elif sgn == 'X':
        who = 'comp'

    for r in range(3):
        if lst[r][0] == sgn and lst[r][1] == sgn and lst[r][2] == sgn:
            return who
        if lst[0][r] == sgn and lst[1][r] == sgn and lst[2][r] == sgn:
            return who
    if all(lst[r][r] == sgn for r in range(3)):
        return who
    if all(lst[i][2-i] == sgn for i in range(3)):
        return who

    return None


lst = [[str(3*j+i+1) for i in range(3)]for j in range(3)]
lst[1][1] = 'X'
free = free_fields(lst)
human_turn = True
while len(free):
    table(lst)
    if human_turn:
        move(lst)
        victor = win(lst, 'O')
    else:
        comp_move(lst)
        victor = win(lst, 'X')
    if victor is not None:
        break
    human_turn = not human_turn
    free = free_fields(lst)

table(lst)
if victor == 'player':
    print('you won!!')
elif victor == 'comp':
    print('comp won!!')
else:
    print('Tie!!')
