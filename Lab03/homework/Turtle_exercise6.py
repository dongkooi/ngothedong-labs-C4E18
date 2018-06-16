from Turtle_exercise5 import draw_star
from turtle import *

# def draw_star(x, y, length_of_star):
#     penup()
#     setpos(x, y)
#     pendown()
#     for i in range(5):
#         forward(length_of_star)
#         right(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()