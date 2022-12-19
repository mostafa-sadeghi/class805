'''
Enter Student Name
Enter python Score
Enter App inventor Score
Enter Scratch Score

Nikan's average in 3 lessons is : 20

'''
# name = input('Enter Student Name ')
# p_score = int(input('enter python score '))
# ap_score = int(input('enter app inventor score '))
# sc_score = int(input('enter scratch score '))

# ave = (p_score + ap_score + sc_score)/3

# print(f"{name}'s average is : {ave:.2f}")


# int : -1     -2     0    1     2
# float : 1.2   3.5    5.9    5.0

# n = int(input('enter a number'))
# n = float(input('enter a number'))
# print(n)


# از تهران به مشهد
# هزینه بنزین مصرفی رفت و برگشت
# 1000 کیلومتر

# ورودی برنامه : میزان مصرف بنزین


# تا 60 لیتر  1500
# آزاد 3000

n = int(input('> '))
m = n * 2000/100

if m <= 60:
    print(m * 1500)

else:
    x = m - 60
    print(60 * 1500 + x * 3000)
