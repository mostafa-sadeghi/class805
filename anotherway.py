import random
CHOICES = ("r", "p", "s")

result = {
    'user': 0,
    'system': 0
}

done = True

while done:

    user_choice = input('enter your choice please (r, p, s) ')
    system_choice = random.choice(CHOICES)

    if user_choice == "r":
        if system_choice == "p":
            msg = "you lose"
            result["system"] += 1

        elif system_choice == "s":
            msg = "you won"
            result["user"] += 1
        else:
            msg = "draw"
    elif user_choice == "p":
        if system_choice == "r":
            msg = "you won"
            result["user"] += 1

        elif system_choice == "s":
            msg = "you lose"
            result["system"] += 1

        else:
            msg = "draw"
    else:
        if system_choice == "r":
            msg = "you lose"
            result["system"] += 1

        elif system_choice == "p":
            msg = "you won"
            result["user"] += 1

        else:
            msg = "draw"
    print("user selected: ", user_choice)
    print("system selected: ", system_choice)
    print(msg)
    play_again = input('Do you want to play again? (y or n)')
    if play_again == 'n':
        break


print("user's score: ", result["user"])
print("system's score: ", result["system"])
