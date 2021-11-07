from turtle import *

edge = int(input("Input number of edges: "))

for i in range(edge):
    forward(100)
    left(360 / edge)

mainloop()