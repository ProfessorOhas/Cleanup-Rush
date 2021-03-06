from turtle import Screen
from turtle import Turtle
from random import randint

item = 0
lives = 3
score = 0

wn = Screen()
wn.title("CLEANUP RUSH")
wn.screensize(5,5)
wn.addshape("river.gif")
wn.addshape("fish.gif")
wn.addshape("heart.gif")
wn.addshape("plasticbag.gif")
wn.addshape("bottle.gif")

def scenes():
  wn.bgpic("first.gif")
  text = input("Press enter to play!")
  if text == "":
    wn.bgpic("second.gif")
    text = input("Press enter to continue!")
    if text == "":
      wn.bgpic("third.gif")
      text = input("Press enter to continue!")
      if text == "":
        wn.bgpic("four.gif")
        text = input("Press enter to continue!")
        if text == "":
          wn.bgpic("river.gif")

class Life:
  def __init__(self):
    self.turtle = Turtle()
    self.turtle.shape("heart.gif")
    self.turtle.penup()
    self.turtle.hideturtle()
  
  def gotoInitialPosition(self, x, y):
    self.turtle.goto(x, y)
    self.turtle.showturtle()

class Fish:
  def __init__(self):
    self.turtle = Turtle()
    self.turtle.shape("fish.gif")
    self.x = 0
    self.y = 0
    self.turtle.penup()
    self.turtle.hideturtle()

  def fish_click(self, x,y):
    global lives
    self.x=0
    self.y=230
    self.turtle.goto(self.x,self.y)
    self.turtle.hideturtle()
    lives = lives - 1

  def fish_stuff(self):
    self.y=randint(-1000,100)
    self.x=-600
    self.turtle.hideturtle()
    self.turtle.goto(self.x,self.y)
    self.turtle.showturtle()
    while self.x <= 600 and self.y!= 230:
      self.turtle.goto(self.x,self.y)
      self.x += 5
    self.turtle.hideturtle()

class PlasticBag:
  def __init__(self):
    self.turtle = Turtle()
    self.turtle.shape("plasticbag.gif")
    self.x = 0
    self.y = 0
    self.turtle.penup()
    self.turtle.hideturtle()


  def plasticbag_click(self, x,y):
    global lives, score
    self.x=0
    self.y=230
    self.turtle.goto(self.x,self.y)
    self.turtle.hideturtle()
    lives += 1
    score += 5
  

  def plasticbag_stuff(self):
    global lives
    self.y=randint(-150,150)
    self.x=-600
    self.turtle.hideturtle()
    self.turtle.goto(self.x,self.y)
    self.turtle.showturtle()
    while self.x <= 600 and self.y!= 230:
      self.turtle.goto(self.x,self.y)
      self.x += 5
    lives -= 1
    self.turtle.hideturtle()

class Bottle:
  def __init__(self):
    self.turtle = Turtle()
    self.turtle.shape("bottle.gif")
    self.x = 0
    self.y = 0
    self.turtle.penup()
    self.turtle.hideturtle()

  def bottle_click(self,x,y):
    global lives, score
    self.x=0
    self.y=230
    self.turtle.goto(self.x,self.y)
    self.turtle.hideturtle()
    lives += 1
    score += 2

  def bottle_stuff(self):
    global lives
    self.y=randint(-150,150)
    self.x=-600
    self.turtle.hideturtle()
    self.turtle.goto(self.x,self.y)
    self.turtle.showturtle()
    while self.x <= 600 and self.y!= 230:
      self.turtle.goto(self.x,self.y)
      self.x += 5
    lives -= 1
    self.turtle.hideturtle()

wn.listen()

scenes()
life1 = Life()
life2 = Life()
life3 = Life()
life1.gotoInitialPosition(230,150)
life2.gotoInitialPosition(250,150)
life3.gotoInitialPosition(270,150)
fish = Fish()
fish.turtle.onclick(fish.fish_click)
plasticbag = PlasticBag()
plasticbag.turtle.onclick(plasticbag.plasticbag_click)
bottle = Bottle()
bottle.turtle.onclick(bottle.bottle_click)

game_loop = True

while game_loop:
  if item == 1:
    fish.fish_stuff()
  elif item == 2:
    plasticbag.plasticbag_stuff()
  elif item == 3:
    bottle.bottle_stuff()
  if lives == 2:
    life3.turtle.hideturtle()
  elif lives == 1:
    life2.turtle.hideturtle()
  item = randint(1,3)
  print("Your score is " + str(score) + " out of 15.")

  if lives == 0 or score>=15:
    life1.turtle.hideturtle()
    print("YOU LOST AND THE ENVIRONMENT HAS DIED!")
    game_loop = False

  elif score >= 15:
    print("YOU WON AND SAVED PROFESSOR GREENIE AND HIS FRIENDS!")
    game_loop = False

if lives == 0:
  wn.bgpic("lose.gif")
else:
  wn.bgpic("win.gif")

wn.exitonclick()