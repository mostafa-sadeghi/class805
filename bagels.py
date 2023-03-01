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
            hints.append('Fermi')
        elif guess[i] in secNumber:
            hints.append('Pico')
    if len(hints) == 0:
        return "bagels"
    return hints


print(f'''Welcome to our bagels game.
we want to guess a {NUM_DIGITS} digits number. we have {MAX_GUESSES} times to guess it.
Wen I say :             That means:
Pico                        On digit is correct but not in the right postion.
Fermi                       On digit is correct and in the right postion.
Bagels                      Nothing is True.
''')
while True:
    sec_num = generate_secret_number()
    print("secret number generated!!!!")
    # print(sec_num)
    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            guess = input('> ')
        hint = getHint(guess, sec_num)
        print(hint)

        numGuesses += 1
        if guess == sec_num:
            break

    print('do you want to continue? (yes or no)')
    if not input('> ').lower().startswith('y'):
        break
print('Thank you for playing')
