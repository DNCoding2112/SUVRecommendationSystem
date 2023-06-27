from tkinter import *
from tkinter import messagebox
tk=Tk()
tk.geometry("250x200+750+300")
def petrols():
    s=""
    fp=open("Fuel_Sorted.txt")
    l=fp.read()
    i=l.index("Petrol")
    fp.seek(i+7)
    for i in range(0,18):
        s+=fp.readline()
    messagebox.showinfo("Petrol", s)

def diesels():
    s=""
    fp=open("Fuel_Sorted.txt")
    l=fp.read()
    i=l.index("Diesel")
    fp.seek(i+17)
    for i in range(0,13):
        s+=fp.readline()
    messagebox.showinfo("Diesel", s)

def evs():
    s=""
    fp=open("Fuel_Sorted.txt")
    l=fp.read()
    i=l.index("EV")
    fp.seek(i+35)
    for i in range(0,4):
        s+=fp.readline()
    messagebox.showinfo("EV", s)

def hybrids():
    s=""
    fp=open("Fuel_Sorted.txt")
    l=fp.read()
    i=l.index("Hybrid")
    fp.seek(i+43)
    for i in range(0,3):
        s+=fp.readline()
    messagebox.showinfo("Hybrid", s)
    
Button(tk,text="Petrol",command=petrols).place(x=10,y=10)
Button(tk,text="Diesel",command=diesels).place(x=60,y=10)
Button(tk,text="EV",command=evs).place(x=10,y=60)
Button(tk,text="Petrol + Diesel Hybrid",command=hybrids).place(x=60,y=60)
tk.mainloop()
