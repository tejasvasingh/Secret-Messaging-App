from tkinter import *
from encode_msg import *
from open_file import *
def selections():
    top=Tk()
    top.title("selection")
    def encode_msg():
        top.destroy()
        encode_msg2()
    def file():
        top.destroy()
        openfile()
    
    l1=Label(top,text="ENCODE MESSAGES",font=("bold",30),bg="green",fg="white",padx=25)
    l1.pack()
    lbl1=Label(top)
    lbl1.pack()
    b1=Button(top,text="**ENCODE**",font=("bold",15),bg="red",fg="white",pady=5,command=encode_msg)
    b1.pack()
    lbl1=Label(top)
    lbl1.pack()
    l2=Label(top,text="SECRET FILE",font=("bold",30),bg="green",fg="white",padx=25)
    l2.pack()
    lbl1=Label(top)
    lbl1.pack()
    b2=Button(top,text="**FILE**",font=("bold",15),bg="red",fg="white",pady=5,command=file)
    b2.pack()
    lbl1=Label(top)
    lbl1.pack()
    l3=Label(top,text="DECODE MESSAGES",font=("bold",30),bg="green",fg="white",padx=25)
    l3.pack()
    lbl1=Label(top)
    lbl1.pack()
    b3=Button(top,text="**DECODE**",font=("bold",15),bg="red",fg="white",pady=5)
    b3.pack()
    top.mainloop()
#selections()    
