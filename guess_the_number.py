import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}\n'))
        if guess < random_number:
            print('sorry, guess agian. too low')
        elif guess > random_number:
            print('sorry, guess agian. too high')
    print(guess)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        elif low == high:
            print('start new game, its good to you to remember, guess number or the number you guessed')
        else:
            guess = low
        feedback = input(f'Is {guess} too high (h), too low (l), correct (c)\n')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'the computer guessed th number and, {guess} you sayed correct ')


computer_guess(200)