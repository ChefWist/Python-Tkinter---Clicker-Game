
from tkinter import *

root = Tk()
root.title("Clicker")
root.geometry("300x300")

global score
global cpc 
cpc = 1
score = 0

def click(scoreed, cpc):
  global score
  score = scoreed
  score += cpc
  scoreDisplay.config(text=score)

def buy(give, cost):
  global score
  global cpc 
  if score >= cost:
    score-=cost
    cpc+=give
    scoreDisplay.config(text=score)
    CpcDisplay.config(text="Cpc: "+str(cpc))


scoreDisplay = Label(root, text=score, font="Ariel 25")
scoreDisplay.pack()
CpcDisplay = Label(root, text="Cpc: "+str(cpc), font="Ariel 25")
CpcDisplay.pack()


clicker = Button(root,
                 text="click me!",
                 command=lambda: click(score, cpc),
                 padx=10,
                 pady=10)
clicker.pack()

shopLabel = Label(root, text="shop", font="Ariel 20")
shopLabel.pack()

shop1 = Button(root, text="25 Money for 2 Cpc", padx=10, pady=10, command=lambda: buy(cost=25, give=2)).pack()
shop2 = Button(root, text="100 Money for 8 Cpc", padx=10, pady=10, command=lambda: buy(cost=100, give=8)).pack()
shop3 = Button(root, text="500 Money for 40 Cpc", padx=10, pady=10, command=lambda: buy(cost=500, give=40)).pack()

root.mainloop()
