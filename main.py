from tkinter import *
from Ball import Ball


root=Tk()
root.geometry('250x250')
canvas=Canvas(bg='green')
canvas.pack()

ball_1=Ball(canvas,10,150,color='cyan',size=20)
ball_1.motion(root,delay=1,WIDTH=250,HEIGHT=250)

ball_2=Ball(canvas,200,150,color='cyan',size=20)
ball_2.motion(root,delay=1,WIDTH=250,HEIGHT=250)
root.mainloop()
