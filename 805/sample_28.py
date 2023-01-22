# r = float(input('enter circle radius '))
# s = 3.14 * (r**2)
# print(f'circle with {r} radius has {s} area.')


numbers = input('enter numbers seprated with, ')
list_numbers = numbers.split(',')
print(list_numbers)


n = int(input('> '))
m = n * 2000/100

if m <= 60:
    print(m * 1500)

else:
    x = m - 60
    print(60 * 1500 + x * 3000)
