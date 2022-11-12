# import turtle
# import time

# screen = turtle.Screen()

# t = turtle.Pen()


# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)

# t.goto(0, 0)
# time.sleep(2)
# t.seth(45)
# time.sleep(2)
# t.fd(100)
# print(t.xcor())
# print(t.ycor())
# t.stamp()
# t.home()
# time.sleep(2)

# print(t.xcor())
# print(t.ycor())
# just clears the drawings off the screen
# t.clear()
# clears the drawing off the screen and resets the turtle
# t.reset()
# t.goto(100, 0)
# screen.exitonclick()

# alternative:
# input()


#######################################

# section 2:

# import turtle
# import time

# screen = turtle.Screen()

# t = turtle.Pen()
# t.speed(0)
# t.speed("slow")
# t.speed(3)

# t.color('#000000')

# t.forward(100)

# turtle_stamp = t.stamp()

# t.backward(100)
# time.sleep(2)
# t.clearstamp(turtle_stamp)

# time.sleep(1)
# t.undo(s)


# screen.exitonclick()


# section 3

import turtle

screen = turtle.Screen()

t = turtle.Pen()


# print(t.towards(100, 100))
heading = t.towards(100, 100)

t.setheading(heading)

t.forward(200)

screen.exitonclick()
