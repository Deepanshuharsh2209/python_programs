#GIVES HEART :)

import math as m
from turtle import *
def hearta(k):
    return 15*m.sin(k)**3

def heartb(k):
    return 12*m.cos(k)-5*\
           m.cos(2*k)-2*\
           m.cos(3*k)-\
           m.cos(4*k)

speed(10000)
bgcolor('black')
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)

done()

    
