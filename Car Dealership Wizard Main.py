from tkinter import *

from tkinter import messagebox

from PIL import ImageTk,Image


tk = Tk()

tk.geometry("1000x300+0+0")

def contactwindow():

    contactwin=Toplevel(tk)

    contactwin.geometry=("200x200+0+0")

    contactwin.title("Contact Us")

    conlab=Label(contactwin, text="Contact Number:99999XXXXX\nE-Mail:xyz@cardealership.com\nFor Any Queries Contact Us On:\nqueries@xyzdealership.com")

    conlab.place(x=10,y=10)

def wiz():

    import SUV_Recommendation_Wizard

def exitp():
    tk.destroy()


def buttons():

    b1=Button(tk, text="FAQs", fg="lightgreen", bg="black", activeforeground="yellow", activebackground="grey",height=2,width=10)

    b1.place(x=580,y=20)


    b2=Button(tk, text="Contact Us", fg="lightgreen", bg="black", activeforeground="yellow", activebackground="grey",command=contactwindow,height=2,width=20)

    b2.place(x=545,y=70)


    b3=Button(tk, text="Privacy Policy", fg="lightgreen", bg="black", activeforeground="yellow", activebackground="grey",height=2,width=18)

    b3.place(x=550,y=120)


    bmain=Button(tk, text="0",font=("bold"))
    bmain.place(x=510,y=0)


Entrytext=Label(tk, font=('Proxima Nova',18,'italic'), fg='cyan', bg='black', text="Welcome to the\nSmart SUV Suggestion System\nI'm Norman,\nHow Can I help You?")

Entrytext.place(x=10,y=30)


canvas = Canvas(tk, width = 300, height = 300)  

canvas.pack()  


img = ImageTk.PhotoImage(Image.open("VirtualAssistant.png"))  

canvas.create_image(10, 10, anchor=NW, image=img)


bmain=Button(tk, text="1",font=("bold"), fg="white", bg="red", command=buttons)
bmain.place(x=510,y=0)


B1=Button(tk, text="SUV Suggestion Wizard", font=('Times New Roman', 14,"underline"), fg="#F04A00", bg="lightgrey", activeforeground="red", activebackground="lightgrey", height=2, width=20, command=wiz)

B1.place(x=20, y=200)


B2=Button(tk, text="Exit", font=('Times New Roman', 14,"underline"), fg="#F04A00", bg="lightgrey", activeforeground="red", activebackground="lightgrey", height=2, width=20, command=exitp)

B2.place(x=550, y=200)


tk.mainloop
