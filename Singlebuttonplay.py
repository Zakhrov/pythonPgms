from tkinter import *
import pygame.mixer
from tkinter.messagebox import askokcancel

app=Tk()
app.title("head first mix")

sound_file="hello.wav"

mixer=pygame.mixer
mixer.init()

flipper=IntVar()

def check_f():
    if flipper.get()==1:
        track.play(loops=-1)
        print("playing")
    else:
        track.stop()
        print("stopped")

def shutdown():
    if askokcancel(title='are you sure?',message='you really want to quit?'):
        app.destroy()
        track.stop()

track=mixer.Sound(sound_file)
Checkbutton(app,command=check_f,variable=flipper,text="flip").pack()

app.protocol("WM_DELETE_WINDOW",shutdown)
app.mainloop()
