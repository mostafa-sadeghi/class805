import turtle
import time

screen = turtle.Screen()
screen.bgcolor('orange')
t = turtle.Pen()
t.pensize(4)
t.speed('fast')
COLORS = ["red", "green", "blue", "black"]
for j in range(12):
    t.pencolor(COLORS[j % 4])
    for i in range(4):
        t.forward(100)
        t.left(90)
    # time.sleep(1.5)
    t.left(30)
    # time.sleep(1.5)


screen.exitonclick()


# تمرین : تغییر رنگ هر یک از مربع ها
#

# حلقه while
# people = []

# while True:
#     name = input('enter your name to add or "exit" to exit from the app: ')
#     if name == 'exit':
#         print(people)
#         exit()
#     people.append(name)
