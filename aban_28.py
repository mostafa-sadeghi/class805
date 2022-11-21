# for i in range(8):
#     print("hello")


# string = 'abcd'
# for s in string:
#     print(s)

# x = range(8)
# print(x)

# numbers = [1, 2, 3, 4, 5, 6]
# for x in numbers:
#     print(x)

# names = ['ali', 'erfan']
# for name in names:
#     print(name, end=' ')
#  لیستی از اعداد 10000 تا 20000
# x = list(range(10000, 20000))
# print(x)

# فقط عددهای زوج

# even_numbers = list(range(10000, 20001, 2))
# print(even_numbers)

# exercise : برنامه ای بنویسید که پیغام hello student1 تا hello student100 را نمایش دهد


# حلقه های تودرتو

# numbers = [1, 2, 3]
# for i in numbers:
#     for j in numbers:
#         print((i, j))


result = 0
for number in range(10, 21):
    result = result + number

print("sum of numbers is: ", result)
