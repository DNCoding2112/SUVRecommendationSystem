from tkinter import *

from tkinter import messagebox

from PIL import ImageTk,Image


tk = Tk()

tk.geometry("1000x400")

def contactwindow():

    contactwin=Toplevel(tk)

    contactwin.geometry=("200x200")

    contactwin.title("Contact Us")

    conlab=Label(contactwin, text="Contact Number:99999XXXXX\nE-Mail:xyz@cardealership.com\nFor Any Queries Contact Us On:\nqueries@xyzdealership.com")

    conlab.place(x=10,y=10)


Entrytext=Label(tk, font=('Proxima Nova',18,'italic'), fg='cyan', bg='black', text="Welcome to the\nSmart Car Suggestion System\nI'm Norman,\nHow Can I help You?")

Entrytext.place(x=10,y=30)


canvas = Canvas(tk, width = 300, height = 300)  

canvas.pack()  


img = ImageTk.PhotoImage(Image.open("VirtualAssistant.png"))  

canvas.create_image(10, 10, anchor=NW, image=img)


bmain=Button(tk, text="!",font=("bold"), fg="white", bg="red")
bmain.place(x=510,y=0)

b1=Button(tk, text="FAQs", fg="lightgreen", bg="black", activeforeground="yellow", activebackground="grey",height=2,width=10)

b1.place(x=580,y=20)


b2=Button(tk, text="Contact Us", fg="lightgreen", bg="black", activeforeground="yellow", activebackground="grey",command=contactwindow,height=2,width=20)

b2.place(x=545,y=70)


b3=Button(tk, text="Privacy Policy", fg="lightgreen", bg="black", activeforeground="yellow", activebackground="grey",height=2,width=18)

b3.place(x=550,y=120)


B1=Button(tk, text="Car Suggestion Wizard", font=('Times New Roman', 14,"underline"), fg="#F04A00", bg="lightgrey", activeforeground="red", activebackground="lightgrey", height=2, width=20)

B1.place(x=20, y=200)


B2=Button(tk, text="Exit", font=('Times New Roman', 14,"underline"), fg="#F04A00", bg="lightgrey", activeforeground="red", activebackground="lightgrey", height=2, width=20)

B2.place(x=750, y=200)


tk.mainloop
