from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(width=800,height= 600)

colors = [ 'green','orange','yellow','blue', 'red', 'purple']
racers = []
y=280
x=-350
pos = 0
for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    racers.append(t)

for racer in racers:
    y-=35
    racer.goto(x,y)
user_bet = screen.textinput(title="Make your bet", prompt="Who wins the race? Enter a color:")


for i in range(0, 800,1 ):
    myrand = randint(0,5)
    racers[myrand].forward(1)

screen.exitonclick()