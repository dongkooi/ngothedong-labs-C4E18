from Turtle_exercise3 import draws_square
from turtle import *
speed(-1)

# def draws_square(length_of_square, color_of_square):
#     color(color_of_square)
#     for i in range(4):
#         forward(length_of_square)
#         left(90)


for i in range(30):
    draws_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()