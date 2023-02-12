import random


NUM_DIGITS = 3
MAX_GUESSES = 10


def generate_secret_number():
    secret_number = random.randrange(100, 1000)
    return secret_number


print(f'''Welcome to our bagels game.
we want to guess a {NUM_DIGITS} digits number. we have {MAX_GUESSES} times to guess it.
Wen I say :             That means:
Pico                        On digit is correct but not in the rigth postion.
Fermi                       On digit is correct and in the rigth postion.
Bagels                      Nothing is True.
''')

sec_num = generate_secret_number()
print(sec_num)
