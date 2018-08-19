from tkinter import *

app=Tk()
app.title("welcome Ronnie")
app.geometry('300x300+200+100')

b1=Button(app,text="correct",width=10)
b1.pack(side='right',padx=10,pady=10)
b2=Button(app,text="wrong",width=10)
b2.pack(side='left',padx=10,pady=10)

app.mainloop()
