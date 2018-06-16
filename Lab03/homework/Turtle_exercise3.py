from turtle import *
speed(-1)

def draws_square(length_of_square, color_of_square):
    color(color_of_square)
    for i in range(4):
        forward(length_of_square)
        left(90)

draws_square(100, "green")
mainloop()
        
