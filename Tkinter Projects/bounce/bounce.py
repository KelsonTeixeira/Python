from tkinter import *
import time
import random

root = Tk()
root.title("Bounce Game")
root.geometry("500x500")
root.resizable(0,0)

vel_ball = 0.6
vel_bar = 50

game = Canvas(root, width=500, height=500, bg="white")
game.pack()

class ball:
    def __init__(self, color, game, the_bar):
        self.game = game
        self.the_bar = the_bar
        self.id = self.game.create_oval(0,0,20,20, fill=color)
        self.game.move(self.id, 250, 350)
        self.x = vel_ball
        self.y = vel_ball
    
    def move(self):
        pos_ball = self.game.coords(self.id)
        if pos_ball[2] >= 500:
            self.x = -vel_ball
        elif pos_ball[0] <= 0:
            self.x = vel_ball
        else:
            None
        if pos_ball[1] <= 0:
            self.y = vel_ball
        elif pos_ball[3] >= 500:
            self.y = 0
            self.game.itemconfigure(game_over, text="GAME OVER")
        else:
            None
        self.game.move(self.id, self.x, self.y)
    
    def shock(self):
        pos_bar = self.game.coords(self.the_bar.id)
        pos_ball = self.game.coords(self.id)
        if pos_ball[0] >= pos_bar[0] and pos_ball[2] <= pos_bar[2]:
            if pos_ball[3] >= pos_bar[1] and pos_ball[3] <= pos_bar[3]:
                self.y = -vel_ball
            else:
                None
        else:
            None
    
    def chage(self):
        self.y = vel_ball


class bar:
    def __init__(self, game, color):
        self.game = game
        self.id = self.game.create_rectangle(0,0,100,15, fill=color)
        self.game.move(self.id, 250, 400)
        self.x = vel_bar
    
    def move_left(self, event):
        pos_bar = self.game.coords(self.id)
        if pos_bar[0] <= 0:
            self.x = 0
        else:
            self.x = -vel_bar
        self.game.move(self.id, self.x, 0)
    
    def move_right(self, event):
        pos_bar = self.game.coords(self.id)
        if pos_bar[2] >= 500:
            self.x = 0
        else:
            self.x = vel_bar
        self.game.move(self.id, self.x, 0)

class squares:
    def __init__(self, game, color, ball, x, y):
        self.game = game
        self.ball = ball
        self.x = x 
        self.y = y
        self.id = self.game.create_rectangle(self.x, self.y, self.x+25, self.y+25, fill = color)
    def shock(self):
        pos_ball = self.game.coords(self.ball.id)
        pos_square = self.game.coords(self.id)
        if pos_ball[0] >= pos_square[0] and pos_ball[2] <= pos_square [2]:
            if pos_ball[1] <= pos_square[3]:
                the_ball.chage()
                self.game.move(self.id, 0, -500)
    
the_bar = bar(game, "grey")
the_ball = ball("red", game, the_bar)
game_over = game.create_text(250,250, text="", font=("arial", 30, "bold"))

root.bind("<Left>", the_bar.move_left)
root.bind("<Right>", the_bar.move_right)

x_sq = 0
y_sq = 0
list_square = []
color_list = ["red", "green", "yellow", "blue", "orange", "purple", "pink"]
for i in range(60):
    list_square.append(squares(game, random.choice(color_list), the_ball, x_sq, y_sq))
    x_sq +=25
    if x_sq == 500:
        y_sq +=25
        x_sq = 0
    else:
        None


while True:
    the_ball.move()
    the_ball.shock()
    root.update_idletasks()
    root.update()
    for i in list_square:
        i.shock()
    time.sleep(0.001)

root.mainloop()