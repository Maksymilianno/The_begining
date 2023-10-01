from random import choice

def hangman():
    word: str = choice(['kowal', 'samochód', 'motyl', 'księżyc', 'telefon', 'kwiatek', 'kawa', 'komputer', 'rowerek', 'smok'])

    username: str = input('Jak masz na imię? >> ')
    print(f'Witaj w wisielcu {username}!')

    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for letter in word:
            if letter in guessed:
                print(letter, end='')
            else:
                print('_', end='')
                blanks += 1

        print()

        if blanks == 0:
            print('Wygrałeś!')
            break

        guess: str = input('Wpisz jedną literę: ')
        if len(guess) == 1:
            continue
        else:
            print('Wprowadź tylko jedną literę!')

        if guess in guessed:
            print(f'Już uzywałeś tej litery: "{guess}". Wpisz inną literę!')
            continue

        guessed += guess
        if guess not in word:
            tries -= 1
            print(f'Wybacz ale to był zły wybór...(Ilość szans:{tries})')

            if tries == 0:
                print('Nie masz już więcej szans. Koniec gry')
                break

if __name__ == '__main__':
    hangman()
