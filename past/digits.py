number = int(input('enter a number: '))
while number != 0:
    m = number % 10
    print(m)
    number = number // 10
