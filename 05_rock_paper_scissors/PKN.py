import random

def pkn():
    moves: str = ['P', 'K', 'N']

    username: str = input('Jak masz na imię? >> ')
    user_move: str = input('Co wybierasz? ')

    computer_choice: str = random.choice(moves)

    if computer_choice == user_move:
        print('Remis')
    elif user_move == 'K' and computer_choice == 'N':
        print(f'{username} wygrał!')
    elif user_move == 'P' and computer_choice == 'K':
        print(f'{username} wygrał!')
    elif user_move == 'N' and computer_choice == 'P':
        print(f'{username} wygrał!')
    else:
        print('Komputer wygrał!')

    print(f'komputer {computer_choice}')
    print(f'gracz {user_move}')
if __name__ == '__main__':
    pkn()