'''
    * 
   * *
  * * *
 * * * *
* * * * *
'''
# print(' '*4 + '* '*1)
# print(' '*3 + '* '*2)
# print(' '*2 + '* '*3)
# print(' '*1 + '* '*4)
# print(' '*0 + '* '*5)


for i in range(5):
    print(' '*(4-i) + '* '*(i+1))


i = 0
while i < 5:
    print(' '*(4-i) + '* '*(i+1))
    i += 1
