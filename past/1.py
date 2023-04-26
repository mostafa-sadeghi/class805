# about while loop

# while True:
#     print('hi')

# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)

# write above code with while loop
# counter
# condition
# update counter

# i = 0

# while i < len(numbers):
#     print(numbers[i])
#     i += 1  # i = i + 1


import turtle
s = turtle.Screen()
s.bgcolor("orange")
p = turtle.Pen()
p.shape('turtle')
p.pencolor("red")
p.pensize(4)
p.penup()
p.setpos(-80, 0)
p.pendown()
p.begin_fill()
p.fillcolor("green")
# for i in range(5):
#     p.forward(200)
#     p.right(144)
i = 0
while i < 5:
    p.forward(200)
    p.right(144)
    i += 1
p.end_fill()
p.penup()
p.goto(-120, 200)
p.write("our first python app", font=("Arial", 20, "bold"))
p.ht()
s.exitonclick()


# exercise 1:
'''
با حلقه while 
شکل های مثلث، مربع و شش ضلعی توپر را رسم کنید.

'''
