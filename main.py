# Unlock Hacks Project
# Friday Jan 7, 2021


# Import turtle library 
from turtle import Screen
from turtle import Turtle
from turtle import tracer
from random import randint

scene = 1
wn = Screen()
wn.title("Environment Game UnlockHacks")
wn.screensize(5,5)
wn.addshape("river.gif")
wn.addshape("fish.gif")
wn.addshape("heart.gif")
wn.addshape("plasticbag.gif")
wn.addshape("bottle.gif")
wn.bgpic("river.gif")
wn.update()

class Fish:
  def __init__(self):
    self.fish = Turtle()
    self.fish.speed(0)
    self.fish.shape("fish.gif")
    self.fish.penup()
    self.fish.goto(randint(-600,-500),randint(-150,150))

class Plasticbag:
  def __init__(self):
    self.plasticbag = Turtle()
    self.plasticbag.speed(0)
    self.plasticbag.shape("plasticbag.gif")
    self.plasticbag.penup()
    self.plasticbag.goto(randint(-600,-500),randint(-150,150))

class Bottle:
  def __init__(self):
    self.bottle = Turtle()
    self.bottle.speed(0)
    self.bottle.shape("bottle.gif")
    self.bottle.penup()
    self.bottle.goto(randint(-600,-500),randint(-150,150))



class Lives:
  def __init__(self):
    self.life = Turtle()
    self.life.speed(0)
    self.life.hideturtle()
    self.life.shape("heart.gif")
    self.life.penup()


fishes = [Fish() for i in range(15)]
plasticbags = [Plasticbag() for i in range(10)]
bottles = [Bottle() for i in range(6)]
lives = [Lives() for i in range(3)]
for i in range(len(lives)):
  lives[i].life.goto(300 + 25*i, 190)
  lives[i].life.showturtle()

tracer(0)

while True:
  wn.update()
  
  for i in range(len(fishes)):
    fishes[i].fish.clear()
    x = fishes[i].fish.xcor()
    x += randint(1,9)
    fishes[i].fish.setx(x)

    if x>600: 
      x = randint(-1000,-500)
      y = randint(-150,150)
      fishes[i].fish.goto(x,y)

  for i in range(len(plasticbags)):
    plasticbags[i].plasticbag.clear()
    x = plasticbags[i].plasticbag.xcor()
    x += randint(1,7)
    plasticbags[i].plasticbag.setx(x)

    if x>600: 
      x = randint(-2000,-500)
      y = randint(-100,100)
      plasticbags[i].plasticbag.goto(x,y)

  for i in range(len(bottles)):
    bottles[i].bottle.clear()
    x = bottles[i].bottle.xcor()
    x += randint(1,7)
    bottles[i].bottle.setx(x)

    if x>600: 
      x = randint(-2000,-500)
      y = randint(-100,100)
      bottles[i].bottle.goto(x,y)


wn.mainloop()