from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.geometry("250x200+500+300")
def tatas():
    s=" "
    fp=open("Brand_Sorted.txt")
    fp.seek(6)
    for i in range(0,3):
        s+=fp.readline()
    messagebox.showinfo("Tata",s)
def mahindras():
    s=" "
    fp=open("Brand_Sorted.txt")
    fp.seek(91)
    for i in range(0,5):
        s+=fp.readline()
    messagebox.showinfo("Mahindra",s)
def mgs():
    s=" "
    fp=open("Brand_Sorted.txt")
    fp.seek(175)
    for i in range(0,4):
        s+=fp.readline()
    messagebox.showinfo("MG",s)
def marutis():
    s=" "
    fp=open("Brand_Sorted.txt")
    fp.seek(270)
    for i in range(0,3):
        s+=fp.readline()
    messagebox.showinfo("Maruti",s)
def hyundais():
    s=" "
    fp=open("Brand_Sorted.txt")
    fp.seek(222)
    for i in range(0,4):
        s+=fp.readline()
    messagebox.showinfo("Hyundai",s)
def kias():
    s=" "
    fp=open("Brand_Sorted.txt")
    fp.seek(54)
    for i in range(0,4):
        s+=fp.readline()
    messagebox.showinfo("Kia",s)

Button(tk,text="Tata",command=tatas).place(x=10,y=10)
Button(tk,text="Mahindra",command=mahindras).place(x=60,y=10)
Button(tk,text="MG",command=mgs).place(x=10,y=60)
Button(tk,text="Maruti",command=marutis).place(x=60,y=60)
Button(tk,text="Hyundai",command=hyundais).place(x=10,y=120)
Button(tk,text="Kia",command=kias).place(x=90,y=120)
