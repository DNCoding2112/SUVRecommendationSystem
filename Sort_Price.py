from tkinter import *
from tkinter import messagebox
tk1=Tk()

def ttb():
    s=" "
    fp=open("Price_Sorted.txt")
    s=fp.read()
    messagebox.showinfo("Low-High",s)

def btt():
    s=" "
    fp=open("Price_Sortedhl.txt")
    s=fp.read()
    messagebox.showinfo("Low-High",s)

def g20():
    s=" "
    fp=open("Price_Sortedhl.txt")
    for i in range(3):
        s+=fp.readline()
    messagebox.showinfo("Above 2000000",s)

def f20t10():
    s=" "
    fp=open("Price_Sortedhl.txt")
    fp.seek(69)
    for i in range(10):
        j=i+1
        if i<6:
            s+=fp.readline()[2:]+"\n"+str(j)
        elif i>=6 and i<9:
            s+=fp.readline()[3:]+"\n"+str(j)
        else:
            s+=fp.readline()[3:]
    messagebox.showinfo("1000000-2000000",s)

def b10():
    s=" "
    fp=open("Price_Sorted.txt")
    for i in range(10):
        s+=fp.readline()
    messagebox.showinfo("Below 1000000",s)
tk1.geometry("250x200+250+300")
B1=Button(tk1,text="Low-High",command=ttb)
B1.place(x=10,y=10)
B2=Button(tk1,text="High-Low",command=btt)
B2.place(x=110,y=10)
L1=Label(tk1,text="By Cost:")
L1.place(x=10,y=50)
B3=Button(tk1,text=">20,00,000",command=g20)
B3.place(x=10,y=70)
B4=Button(tk1,text="10,00,000-20,00,000",command=f20t10)
B4.place(x=10,y=100)
B5=Button(tk1,text="<10,00,000",command=b10)
B5.place(x=10,y=130)
tk1.mainloop
