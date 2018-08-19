from tkinter import *
import pygame.mixer

app=Tk()
app.title("hello flip")
flipper=IntVar()

def check_f():
    if(flipper.get()==1):
        print("cool")
    else:
        print("not so cool")


Checkbutton(app,command=check_f,variable=flipper,text="flip").pack()
