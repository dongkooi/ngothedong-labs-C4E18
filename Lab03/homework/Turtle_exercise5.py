from turtle import *
speed(-1)

def draw_star(x, y, length_of_star):
    penup()
    setpos(x, y)
    pendown()
    for i in range(5):
        forward(length_of_star)
        right(144)
# https://stackoverflow.com/questions/14713037/python-turtle-set-start-position
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.setpos
draw_star(1, 1, 100)
mainloop()