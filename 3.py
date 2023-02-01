'''
*
* *
* * *
* * * *
* * *
* *
*
'''
# print('* '*1)
# print('* '*2)
# print('* '*3)
# print('* '*4)
# print('* '*3)
# print('* '*2)
# print('* '*1)

# for i in range(7):
#     if i < 7/2:
#         print('* '*(i+1))
#     else:
#         print(('* '*(7-i)))

# Exercise 1:  while loop
# Exercise 2 :
'''
      *
    * *
  * * *
* * * *
  * * *
    * *
      *
'''

#     *
#   * *
# * * *
#   * *
#     *

n = int(input('> '))
i = 0
j = 2
while i < n:
    if i < n/2:
        print(' ' * (n-2*i-1) + '* '*(i+1))
    else:
        print(' ' * j + '* '*(n-i))
        j += 2

    i += 1
'''
      *
    * * *
  * * * * *
* * * * * * * 


'''
