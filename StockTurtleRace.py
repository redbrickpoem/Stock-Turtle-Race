import time
from turtle import Turtle as Turt, Screen
import random
import yfinance as yf

class StockTurtle:

    def __init__(self,name,initial_price):
        self.name = name
        # self.color = color
        self.price = initial_price
        self.tur_obj = Turt()
        # self.tur_obj.color(color)
        self.tur_obj.shape("turtle")

    def set_pos(self, x, y):
        self.position = (x, y)
        self.tur_obj.penup()
        self.tur_obj.goto(x, y)

    def stock_price(self,symbol):
        self.symbol = symbol
        start = "2025-01-01"
        end = "2025-03-31"
        data = yf.download(symbol,start,end)
        self.data = data['Close']

    def set_color(self,color):
        self.color = color
        self.tur_obj.color(color)

    def race_step(self,index, scale=5):
        if index == 0: return
        change = float(self.data.iloc[index] - self.data.iloc[index -1])
        self.tur_obj.forward(change * scale)


screen = Screen()
screen.setup(500,400)


finish_line = Turt()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(200,-150)
finish_line.pendown()
finish_line.pensize(5)
finish_line.left(90)
finish_line.forward(300)


Tim = StockTurtle("Tim", 100)
Tom = StockTurtle("Tom", 101)
Jerry = StockTurtle("Jerry", 102)
Luis = StockTurtle("Luis", 103)
Bugs = StockTurtle("Bugs", 104)
Jack = StockTurtle("Jack", 105)
Max = StockTurtle("Max", 106)

symbols = ["AAPL", "GOOG", "TSLA", "MSFT", "META", "NVDA", "AMZN"]
colors = ["red", "blue", "green", "orange", "purple", "yellow", "brown"]
turtles = [Tim, Tom, Jerry, Luis, Bugs, Jack, Max]

for turtle,symbol, color in zip(turtles,symbols,colors):
    turtle.stock_price(symbol)
    turtle.set_color(color)

Tim.set_pos(-200,-130)
Tom.set_pos(-200,-105)
Jerry.set_pos(-200,-80)
Luis.set_pos(-200,-55)
Bugs.set_pos(-200,-30)
Jack.set_pos(-200,-5)
Max.set_pos(-200, 20)

for turtle,symbol, color in zip(turtles,symbols,colors):
    turtle.stock_price(symbol)
    turtle.set_color(color)

is_race_on = True
while is_race_on:
    days = len(Tim.data)

    for i in range(1, 50):
        for turtle in turtles:
            turtle.race_step(i, scale=3)
            if turtle.tur_obj.xcor() >= 200:
                print(f"{turtle.name} wins the race represnting {turtle.symbol}! 🏁")
                is_race_on = False
                break
        if not is_race_on:
            break
    time.sleep(0.1)


screen.exitonclick()