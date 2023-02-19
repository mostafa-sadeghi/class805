import random


NUM_DIGITS = 3
MAX_GUESSES = 10


def generate_secret_number():
    numbers = list('0123456789')
    random.shuffle(numbers)
    numbers = numbers[:3]
    result = ''
    for n in numbers:
        result += n
    return result


def getHint(guess, secNumber):
    if guess == secNumber:
        return 'You got it!'

    hints = []
    for i in range(len(guess)):
        if guess[i] == secNumber[i]:


print(f'''Welcome to our bagels game.
we want to guess a {NUM_DIGITS} digits number. we have {MAX_GUESSES} times to guess it.
Wen I say :             That means:
Pico                        On digit is correct but not in the rigth postion.
Fermi                       On digit is correct and in the rigth postion.
Bagels                      Nothing is True.
''')
while True:
    sec_num = generate_secret_number()
    print("secret number generated!!!!")
    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            guess = input('> ')
        hint = getHint(guess, sec_num)
