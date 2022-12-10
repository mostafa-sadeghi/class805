
# for i in range(4):
#     print('*************************************')
#     print(i)
#     print('*************************************')
#     for j in range(4):
#         print(j)

# exercise1 :
'''پنج عدد از کاربر در یافت نماید و حالضرب آن اعداد را نمایش دهد
2:
برنامه ای بنیوسید که پنج عدد از کاربر دریافت نماید و حاصجمع اعداد زوج وارد شده را نمایش دهد
'''
# numbers = []
# for i in range(5):
#     n = int(input('enter a number > '))
#     numbers.append(n)

# numbers = list(range(0, 1000, 2))
# string = 'abc'
# s = string
# print(s)
# string_list = list(s)
# print(string_list)

# exercise:
'''
برنامه ای بنویسید که اسم پنج نفر را از ورودی بگیرد و در کنار هم نمایش دهد
'''
# string = ''

# for i in range(5):
#     name = input('enter your name> ')
#     string += name + ' '  # string = string + name
# print(string)

# max value between five input numbers:
# first solution
# max_number = 0

# for i in range(5):
#     number = int(input('enter a number '))
#     if number > max_number:
#         max_number = number
# print('max_number is', max_number)


# second solution

numbers = []
for i in range(5):
    number = int(input('enter a number> '))
    numbers.append(number)
max_number = max(numbers)
print('max number is', max_number)
