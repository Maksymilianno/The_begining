import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount == 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
    rolls_sum: int = sum(rolls)

    return rolls, rolls_sum




def main():
    while True:
        try:
            user_input : str = input('Iloma kostkami chcesz rzucic? ')

            if user_input.lower() == 'koniec':
                print('Do zobaczenia!')
                break

            print(roll_dice(int(user_input)))
        except ValueError:
            print('Podaj poprawną liczbę')


if __name__ == '__main__':
    main()