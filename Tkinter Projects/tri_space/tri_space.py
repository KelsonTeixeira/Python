from tkinter import *
from tkinter import messagebox
import random
import time

#___________window definitions_______________
window = Tk()
window.geometry("550x630")
window.title("TRI-SPACE")
window.resizable(0,0)
window.config(bg="#353b48")
#____________________________________________

#__________record capture____________________
record_file = open("./record.txt", 'r')
high_score = int(record_file.readline())
record_file.close()
#____________________________________________

#__________Global variables__________________
score = 0
keep_score = 0
dificulty = 0.75
#____________________________________________

#___________Window Division__________________

frame_button = Frame(window)
frame_button.grid(row=2, column=1, padx=15)

frame_label = Frame (window, bg="#353b48")
frame_label.grid(row=0, column=1, pady=2)

game = Canvas(width=500, height=500, bg="black")
game.grid(row=1, column=1, pady=10)

frame_1 = Frame(window)
frame_1.grid(row=1, column=0, padx=12.5)
#_____________________________________________

#_______________objects_______________________

#the ship
class space_ship:
    def __init__(self, game, color):
        self.game = game
        self.id = game.create_polygon(0,20,0,5,5,15,20,15,25,0,30,15,45,15,50,5,50,20,25,30, fill=color)
        self.game.move(self.id, 230,430)
        self.x1 = 20
        self.y = 0

    def move_right(self, event):
        position = self.game.coords(self.id)
        if position [16] >= 500:
            self.x1 = 0
        else:
            self.x1 = 20
        self.game.move(self.id, self.x1, self.y)      
        
    def move_left(self, event):
        position = self.game.coords(self.id)
        if position [0] <= 0:
            self.x1 = 0
        else:
            self.x1 = -20
        self.game.move(self.id, self.x1, self.y)

#the triangles
class ast:
    def __init__(self, game, ship, color, score_painel):
        self.game = game
        self.ship = ship
        self.score_painel = score_painel
        self.x_create = random.randint(1,500)
        self.y = random.randint(-500,0)
        self.x = 0
        self.y_move = 0.75
        self.z = random.randint(15,25)
        self.w = random.randint(10,30)
        self.id = game.create_polygon(self.x_create, 0, self.x_create+self.z, 0, self.x_create+self.z/2, self.w, fill=color)
        self.game.move(self.id, self.x, self.y)

    def move(self, dificulty):
        global score
        position = self.game.coords(self.id)
        if position[1] >= 500:
            self.y=-500
            self.x=random.randint(-position[0], 500 - position[0])
            score +=1
            self.game.itemconfigure(self.score_painel, text = score)
        else: 
            self.y= dificulty
            self.x=0
        self.game.move(self.id, self.x, self.y)

    def lose (self):
        ship_position = self.game.coords(self.ship.id)
        ast_position = self.game.coords(self.id)
        if ast_position [4] >= ship_position[0] and ast_position[4] <= ship_position[16]:
            if ast_position [5] >= ship_position [7] and ast_position[5] <= ship_position[19]:
                print ("LOSE")
                return False
        else: 
            return True

    def restart(self):
        position = self.game.coords(self.id)
        self.x=random.randint(-position[0], 500 - position[0])
        self.game.move(self.id, self.x, -500)
    
class stars:
    def __init__(self, color, game):
        self.game = game
        self.color = color
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        self.id = game.create_oval(self.x, self.y, self.x+3, self.y+3, fill=self.color)
    def move(self):
        position = self.game.coords(self.id)
        if position[1] >= 500:
            self.y=-500
        else: 
            self.y= 0.5
        self.game.move(self.id, 0, self.y)

#________________________________________________________________

#_____________________itens creation______________________________

#stars creation
star = []
for i in range(50):
    star.append(stars("white", game))

#Labels
game_label = Label(frame_label, text="TRI-SPACE", font=("device", 20), bg="#353b48", width=20, fg="white")
game_label.grid(row=0, column=1)

high_score_label = Label(frame_label, text="HIGH SCORE: "+str(high_score), font=("device", 9, "italic"), bg="#353b48", width=21, fg="white")
high_score_label.grid(column=1, row=1)

#Canva text creation
game_over = game.create_text(250,220, text="", font=("Courier", 22), fill="white")
end_score = game.create_text(250,270, text="", font=("Courier", 14), fill="white")
new_record = game.create_text(250,295, text="", font=("Courier", 14), fill="white")

#score painel
squad_score_painel = game.create_rectangle(440,20, 485, 40, fill="white")
score_painel = game.create_text(470, 30, text=score, fill="black")

#ship creation
ship = space_ship(game, "#95afc0")

#triangles creation
asteroid=[]
colors_list = ["#feca57", "#ff9f43", "#e84118", "#ea2027"]
for i in range(9):
    x = random.choice(colors_list)
    asteroid.append(ast(game, ship, x, score_painel))
#_____________________________________________________________________

#____________________________Functions_________________________________
def high_score_verify():
    global score, high_score, game, high_score_label
    if score > high_score:
        high_score_label.config(text="HIGH SCORE: "+str(score))
        messagebox.showinfo("Record", "New Record!\nCongrats!")
        record_file = open('/home/kelson/GITHUB/Tkinter_estudo/Projetos/tri_space/record.txt', 'w')
        record_file.write(str(score))
        record_file.close()
    else:
        None

def play_fun ():
    global asteroid, dificulty, game, keep_score, score, game_over, end_score, colors_list, ship, score_painel, star
    verify = True
    x = ""
    while verify:
        window.update_idletasks()
        window.update()
        if score >= keep_score + 50:
            dificulty +=0.1
            keep_score = score
        for st in star:
            st.move()
        for asts in asteroid:
            asts.move(dificulty)
            asts.lose()
            if asts.lose() == False:
                verify = False
                break
        time.sleep(0.0005)
        print (dificulty)
    else:
        game.itemconfigure(game_over, text = "GAME OVER")
        game.itemconfigure(end_score, text = "SCORE: "+str(score))
        high_score_verify()
        
        
def restart_fun ():
    global score, game, game_over, end_score, asteroid, score_painel, dificulty, keep_score

    game.itemconfigure(game_over, text = "")
    game.itemconfigure(end_score, text = "")
    game.itemconfigure(new_record, text = "")
    score = 0
    game.itemconfigure(score_painel, text = score)
    dificulty = 0.75
    keep_score = 0
    for asts in asteroid:
        asts.restart()
    play_fun()

def change_button():
    play_button.config(text="RESTART", command=restart_fun)
    play_fun()
#___________________________________________________________________

#________________________Controls____________________________________
play_button = Button(frame_button, text="PLAY", command = change_button)
play_button.grid(row=0, column=0)

window.bind("<Right>", ship.move_right)
window.bind("<Left>", ship.move_left)
#_______________________________________________________________________

window.mainloop()