from tkinter import *
import pygame.mixer
from tkinter.messagebox import askokcancel

app=Tk()
app.title("head first mix")

sound_file="hello.wav"

mixer=pygame.mixer
mixer.init()

def track_start():
    track.play(loops=-1)

def track_stop():
    track.stop()

def shutdown():
    if askokcancel(title='are you sure?',message='you really want to quit?'):
        app.destroy()
        track.stop()

track=mixer.Sound(sound_file)
start_button=Button(app,command=track_start,text="start")
start_button.pack(side=LEFT)
stop_button=Button(app,command=track_stop,text="stop")
stop_button.pack(side=RIGHT)
app.protocol("WM_DELETE_WINDOW",shutdown)
app.mainloop()
