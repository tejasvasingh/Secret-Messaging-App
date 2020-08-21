from tkinter import *
from selection import *
root=Tk()
root.title("SECRET_CODE")
def nextpage():
    root.destroy()
    selections()
    
L1=Label(root,text="2 WAY SECRET CODE",font=("bold",40,),bg="green",fg="white")
L1.pack()
l0=Label(root)
l0.pack()
l2=Label(root,text="MESSAGING",font=("bold",40,),bg="green",fg="white")
l2.pack()
blk_lab=Label(root)
blk_lab.pack()

#photo
photo = PhotoImage(file = 'Top_secret.png')
photo = photo.subsample(1)
lbl = Label(root,image = photo)
lbl.image = photo
lbl.pack()
blk_lab2=Label(root)
blk_lab2.pack()
but=Button(root,text="**SECRERT**",bg="red",fg="white",font=("bold",14,),padx=10,pady=10,command=nextpage)
but.pack()
root.mainloop()

