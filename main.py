import numpy as np
from tkinter import *
from PIL import Image, ImageTk


def coinFlip():
    result = np.random.binomial(1,0.5)
    tfield.delete("1.0", "end")
 
    if(result == 1):
        tfield.insert(INSERT, " It's ————> HEADS")
        i.config(image = heads)
         
    else:
        tfield.insert(INSERT, " It's ————> TAILS")
        i.config(image = tails)
 

root = Tk()
root.title("Python Coin Flip")


#load heads image
load = Image.open("head.png")
heads = ImageTk.PhotoImage(load)
 
#load tails image
load = Image.open("tail.jpg")
tails = ImageTk.PhotoImage(load)

i = Label(root, image=heads)
i.pack()

root.geometry("500x500")

b1=Button(root, text="Toss the Coin", font=("Arial", 10), command=coinFlip, bg='teal', fg='white', activebackground="lightblue", padx=10, pady=10)
b1.pack()


tfield = Text(root, width=52, height=5)
tfield.pack()

tfield.insert(INSERT, "Click on the Button.. To Flip the Coin and get the result")


root.mainloop()



