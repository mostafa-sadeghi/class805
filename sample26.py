'''
Enter Student Name
Enter python Score
Enter App inventor Score
Enter Scratch Score

Nikan's average in 3 lessons is : 20

'''
name = input('Enter Student Name ')
p_score = int(input('enter python score '))
ap_score = int(input('enter app inventor score '))
sc_score = int(input('enter scratch score '))

ave = (p_score + ap_score + sc_score)/3

print(f"{name}'s average is : {ave:.2f}")
