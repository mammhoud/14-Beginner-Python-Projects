import random

print('welcome would you like to generate password!, for your youtube')

chars = input('what is the character you needs in the password: ')
number = input('how many pass you need: ')
number = int(number)

length = input('what the pass length: ')
length = int(length)

print('\nhere your passwords:\n')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
