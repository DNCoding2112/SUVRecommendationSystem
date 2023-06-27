from tkinter import *

from tkinter import messagebox

tk=Tk()

tk.geometry("250x200+0+300")

def Sortb():
    import Sort_Brand

def Sortp():
    import Sort_Price

def Sortf():
    import Sort_Fuel
    
names=Label(tk, text="Choose type of Sorting")

names.place(x=10,y=10)

var=IntVar()

var.set(0)

Button(tk,text=("Price"), command=Sortp).place(x=10,y=40)

Button(tk,text=("Brand"), command=Sortb).place(x=10,y=70)

Button(tk,text=("Fuel Type"), command=Sortf).place(x=10,y=100)

tk.mainloop
