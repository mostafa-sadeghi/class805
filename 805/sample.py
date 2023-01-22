import turtle

s = turtle.Screen()
# s.register_shape("my", ((10, 0), (10, 10), (-10, 10), (-10, 0)))
s.register_shape("strawberry.gif")
p = turtle.Pen()
# print(p.pensize())

p.shape('arrow')
# p.shape('my')
# p.shape('strawberry.gif')
# p.showturtle()
# p.hideturtle()
p.forward(100)


s.exitonclick()
