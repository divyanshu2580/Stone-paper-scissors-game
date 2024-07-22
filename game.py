from tkinter import *
import tkinter as tk 
from random import randint 
from PIL import Image  ,ImageTk
import pygame

# root file

root = tk.Tk()
root.geometry('1000x700+0+0')
root.title("Stone Paper Scissors Game")
root.iconbitmap("images/icon.ico")

def res_updation(a):
    canvas_home.itemconfig(result_text, text=a)

def score_updation_comp():
    final_comp = int(canvas_home.itemcget(score_comp, 'text'))
    final_comp += 1
    canvas_home.itemconfig(score_comp, text=str(final_comp))

def score_updation_user():
    final_user = int(canvas_home.itemcget(score_user, 'text'))
    final_user += 1
    canvas_home.itemconfig(score_user, text=str(final_user))

def winner_check(p,c):
    if p == c:
        res_updation("IT IS A TIE !!")
        effect3.play()

    elif p == "rock":
        if c== "paper":
            res_updation("COMPUTER WINS !! ")
            effect2.play()
            score_updation_comp()

        else :
            res_updation("PLAYER WINS !! ")
            effect1.play()
            score_updation_user()

    elif p == "scissors":
        if c == "rock":
            res_updation("COMPUTER WINS !! ")
            effect2.play()
            score_updation_comp()
        else :
            res_updation("PLAYER WINS !! ")
            effect1.play()
            score_updation_user()

    elif p == "paper":
        if c== "scissors":
            res_updation("COMPUTER WINS !! ")
            effect2.play()
            score_updation_comp()
        else :
            res_updation("PLAYER WINS !! ")
            effect1.play()
            score_updation_user()
    else:
        pass

to_select = ["rock","paper","scissors"]

def choose_hand(a):
    choise_comp = to_select[randint(0,2)]
    if choise_comp == "rock":
        comp_label.config(image=comp_rock)
    elif choise_comp == "paper":
        comp_label.config(image=comp_paper)
    else:
        comp_label.config(image=comp_scissors)

    if a=="rock":
        user_label.config(image=user_rock)
    elif a == "paper":
        user_label.config(image=user_paper)
    else:
        user_label.config(image=user_scissors)
    
    winner_check(a, choise_comp)

def reset_game():
    canvas_home.itemconfig(score_user, text="00")
    canvas_home.itemconfig(score_comp, text="00")
    canvas_home.itemconfig(result_text, text="")
    user_label.config(image=user_bg)
    comp_label.config(image=comp_bg)

def show_frame(frame):
    frame.tkraise()

container = tk.Frame(root)
container.pack(fill="both", expand=True)

# images 

image_path = "images/background.jpeg"
image_back = Image.open(image_path)
image_back = image_back.resize((1000, 700), Image.LANCZOS)
bg_image_home = ImageTk.PhotoImage(image_back)

image_path1 = "images/user_bg.png"
image_back1= Image.open(image_path1)
image_back1 = image_back1.resize((200,160), Image.LANCZOS)
user_bg = ImageTk.PhotoImage(image_back1)

image_path2 = "images/comp_bg.png"
image_back2 = Image.open(image_path2)
image_back2 = image_back2.resize((200,160), Image.LANCZOS)
comp_bg = ImageTk.PhotoImage(image_back2)

image_path3 = "images/btn_scissors.png"
image = Image.open(image_path3)
image = image.resize((80,80), Image.LANCZOS)
btn_scissors = ImageTk.PhotoImage(image)

image_path4 = "images/user_scissors.png"
image_back4 = Image.open(image_path4)
image_back4 = image_back4.resize((200,160), Image.LANCZOS)
user_scissors = ImageTk.PhotoImage(image_back4)

image_path5 = "images/btn_rock.png"
image2 = Image.open(image_path5)
image2 = image2.resize((80,80), Image.LANCZOS)
btn_rock = ImageTk.PhotoImage(image2)

image_path6 = "images/btn_paper.png"
image3 = Image.open(image_path6)
image3 = image3.resize((80,80), Image.LANCZOS)
btn_paper= ImageTk.PhotoImage(image3)

image_path7 = "images/user_paper.png"
image_back7 = Image.open(image_path7)
image_back7 = image_back7.resize((200,160), Image.LANCZOS)
user_paper = ImageTk.PhotoImage(image_back7)

image_path8 = "images/user_rock.png"
image_back8 = Image.open(image_path8)
image_back8 = image_back8.resize((200,160), Image.LANCZOS)
user_rock = ImageTk.PhotoImage(image_back8)

image_path9 = "images/comp_scissors.png"
image_back9 = Image.open(image_path9)
image_back9 = image_back9.resize((200,160), Image.LANCZOS)
comp_scissors = ImageTk.PhotoImage(image_back9)

image_path10 = "images/comp_rock.png"
image_back10 = Image.open(image_path10)
image_back10 = image_back10.resize((200,160), Image.LANCZOS)
comp_rock = ImageTk.PhotoImage(image_back10)

image_path11 = "images/comp_paper.png"
image_back11 = Image.open(image_path11)
image_back11 = image_back11.resize((200,160), Image.LANCZOS)
comp_paper = ImageTk.PhotoImage(image_back11)

# sound

pygame.mixer.init()
sound_bg = pygame.mixer.Sound("sounds/bg_sound.wav")
sound_bg.set_volume(0.6)
sound_bg.play(-1)

effect1 = pygame.mixer.Sound("sounds/win.wav")
effect1.set_volume(0.3)

effect2 = pygame.mixer.Sound("sounds/lose.wav")
effect2.set_volume(0.5)

effect3 = pygame.mixer.Sound("sounds/tie.wav")
effect3.set_volume(0.5)

# Home frame

home_frame = tk.Frame(container)

canvas_home = tk.Canvas(home_frame, width=800, height=600)
canvas_home.place(relx=0, rely=0, relwidth=1, relheight=1)

button_exit = tk.Button(home_frame , text="EXIT" , border=5, bg="lightsalmon4",fg="white",width=10,font=("futura",20,"bold"),command= lambda: root.destroy())
button_window_exit = canvas_home.create_window(990,50,anchor="e",window=button_exit)

button_reset = tk.Button(home_frame , text="RESET" , border=5, bg="lightsalmon4",fg="white",width=10,font=("futura",20,"bold"),command= reset_game)
button_window_reset = canvas_home.create_window(10,50,anchor='w',window=button_reset)

canvas_home.create_image(0, 0, anchor="nw", image=bg_image_home)

canvas_home.create_text(500, 50, text="ROCK PAPER SCISSORS", font=("futura", 30, "bold"), fill="white")

canvas_home.create_line(200, 75, 800,75, fill="white", width=3)

canvas_home.create_text(500,90, text="RESULT",font=("futura",30,"bold"),fill="white",anchor="n")

result_rect = canvas_home.create_rectangle(280, 150,710, 250, fill="",outline="white" ,width=5)

result_text = canvas_home.create_text(500,200 , text="" ,fill="white",font=("futura",25,"bold") , anchor="center")

canvas_home.create_text(500,300,text="SCORECARD",font=("futura",25,"bold"),fill="white", anchor="center")

canvas_home.create_text(70,300, text=" USER ",font=("futura",30,"bold"),fill="white",anchor="w")

user_label= tk.Label(home_frame,image=user_bg, bg="tomato4",width=210, height=170)
user_label_window= canvas_home.create_window(30,410 , anchor="w" , window=user_label)

canvas_home.create_text(940,300, text=" COMP. ",font=("futura",30,"bold"),fill="white",anchor="e")

comp_label= tk.Label(home_frame ,image=comp_bg, bg="tomato4",width=210 , height=170)
comp_label_window= canvas_home.create_window(970,410 , anchor="e" , window=comp_label)

canvas_home.create_text(450,350, text=" USER ",font=("futura",23,"bold"),fill="white",anchor="e")

rect_user_score = canvas_home.create_rectangle(370, 390, 450, 470,fill="", outline="white" ,width=5)

score_user = canvas_home.create_text(440, 430, text="00", font=("futura", 40), fill="white", anchor="e")

canvas_home.create_text(550,350, text=" COMP. ",font=("futura",23,"bold"),fill="white",anchor="w")

rect_comp_score = canvas_home.create_rectangle(550, 390, 630, 470, fill="", outline="white" ,width=5)

score_comp = canvas_home.create_text(560, 430, text="00", font=("futura", 40), fill="white", anchor="w")

canvas_home.create_line(300, 370, 700, 370, fill="white", width=3)

canvas_home.create_line(500, 330, 500, 480, fill="white", width=3)

button = tk.Button(home_frame, image=btn_scissors, border=5, bg="lightsalmon4",font=("futura",15,"bold") ,pady=5, fg="white" , width=130,text="SCISSORS",compound="top", command=lambda:choose_hand("scissors"))
button_window = canvas_home.create_window(200, 600, anchor="w", window=button)

button = tk.Button(home_frame, image=btn_rock, border=5, bg="lightsalmon4",font=("futura",15,"bold") ,pady=5, fg="white" , width=130,text="ROCK",compound="top", command=lambda:choose_hand("rock"))
button_window = canvas_home.create_window(500, 600, anchor="center", window=button)

button = tk.Button(home_frame, image=btn_paper, border=5, bg="lightsalmon4",font=("futura",15,"bold") ,pady=5, fg="white" , width=130,text="PAPER",compound="top", command=lambda:choose_hand("paper"))
button_window = canvas_home.create_window(800, 600, anchor="e", window=button)

canvas_home.create_text(990, 690, text="© Divyanshu",font=("futura",13),fill="white",anchor="se")

home_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

show_frame(home_frame)
root.mainloop()