from tkinter import *
from decode_file import *
def openfile():
    file=Tk()
    file.title("files")
    def open_files():
        global v
        v=E1.get()
        name="secret_file_"+str(v)
        fr=open(name+".text","r")
        r=fr.read()
        fr.close()
        file.destroy()
        #new window
        enc=Tk()
        enc.title("encoded_file")

        
        def decode():
            enc.destroy()
            decode_file(v)

            
        photo = PhotoImage(file = 'images.png')
        photo = photo.subsample(1)
        lbl5 = Label(enc,image = photo)
        lbl5.image = photo
        lbl5.grid(row=0,column=0,columnspan=6)
        lbl3=Label(enc)
        lbl3.grid(row=1,column=0)
        L1=Label(enc,text="Encoded File",font=("bold",35,),bg="red",fg="white",padx=40)
        L1.grid(row=2,column=0)
        L2=Label(enc,text=r,font=("bold",20,),fg="black")
        L2.grid(row=3,column=0)
        lbl8=Label(enc)
        lbl8.grid(row=4,column=0)
        B2=Button(enc,text="Decode File",font=("bold",14,),bg="yellow",fg="black",command=decode)
        B2.grid(row=5,column=0)
        enc.mainloop()
        
        
        
        
        
    photo = PhotoImage(file = 'key_PNG1174.png')
    photo = photo.subsample(1)
    lbl = Label(file,image = photo)
    lbl.image = photo
    lbl.grid(row=0,column=0,columnspan=6)
    L1=Label(file,text="ENTER KEY---->",font=("bold",20,),bg="yellow",fg="black")
    L1.grid(row=1,column=0)
    E1=Entry(file,bd=5)
    E1.grid(row=2,column=1,padx=30)
    lbl2=Label(file)
    lbl2.grid(row=2,column=0)
    L2=Label(file,text="TO OPEN FILE",font=("bold",20,),bg="yellow",fg="black")
    L2.grid(row=3,column=0)
    lbl3=Label(file)
    lbl3.grid(row=4,column=0)
    b1=Button(file,text="OPEN FILE",font=("bold",14,),bg="green",fg="white",command=open_files)
    b1.grid(row=5,column=0,columnspan=6)
    file.mainloop()
#openfile()    
    
