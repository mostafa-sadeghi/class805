# exercise 1:
'''
برنامه ای بنویسید که اعداد زوج دو رقمی را در یک لیست ذخیره نماید

'''
# روش اول
from colorama import Fore, Back, Style
import colorama
# numbers = []
# for i in range(10, 100, 2):
#     numbers.append(i)
# print(numbers)
# روش دوم
# numbers = []
# for i in range(10, 100):
#     if i % 2 == 0:
#         numbers.append(i)
# print(numbers)
# روش سوم
# numbers = list(range(10, 100, 2))
# print(numbers)


print(Fore.BLACK + "hello every body")
print()
print(Fore.CYAN + "hello every body")


# exercise 2:
'''
برنامه ای بنویسید که مجموع اعداد فرد سه رقمی را نمایش دهد
'''

# exercise 3:
'''
برنامه ای بنویسید  که یک عدد را از ورودی دریافت نماید و در صورت زوج بودن پیغام مناسبی رانمایش دهد
مثلا ok
'''

number = int(input('enter a number> '))
if number % 2 == 0:
    print(Fore.GREEN + f'{number} is even')
else:
    print(Fore.RED + f'{number} is odd')
