from tkinter import *
def encode_msg2():
    tip=Tk()
    tip.title("ENCODE")
    def identer(x):
        if x=="a" or x=="A":
            return(0)
        if x=="b" or x=="B":
            return(1)
        if x=="c" or x=="C":
            return(2)
        if x=="d" or x=="D":
            return(3)
        if x=="e" or x=="E":
            return(4)
        if x=="f" or x=="F":
            return(5)
        if x=="g" or x=="G":
            return(6)
        if x=="h" or x=="H":
            return(7)
        if x=="i" or x=="I":
            return(8)
        if x=="j" or x=="J":
            return(9)
        if x=="k" or x=="K":
            return(10)
        if x=="l" or x=="L":
            return(11)
        if x=="m" or x=="M":
            return(12)
        if x=="n" or x=="N":
            return(13)
        if x=="o" or x=="O":
            return(14)
        if x=="p" or x=="P":
            return(15)
        if x=="q" or x=="Q":
            return(16)
        if x=="r" or x=="R":
            return(17)
        if x=="s" or x=="S":
            return(18)
        if x=="t" or x=="T":
            return(19)
        if x=="u" or x=="U":
            return(20)
        if x=="v" or x=="V":
            return(21)
        if x=="w" or x=="W":
            return(22)
        if x=="x" or x=="X":
            return(23)
        if x=="y" or x=="Y":
            return(24)
        if x=="z" or x=="Z":
            return(25)
    def identer2(x1):
        if x1==0:
            return("A")
        if x1==1:
            return("B")
        if x1==2:
            return("C")
        if x1==3:
            return("D")
        if x1==4:
            return("E")
        if x1==5:
            return("F")
        if x1==6:
            return("G")
        if x1==7:
            return("H")
        if x1==8:
            return("I")
        if x1==9:
            return("J")
        if x1==10:
            return("K")
        if x1==11:
            return("L")
        if x1==12:
            return("M")
        if x1==13:
            return("N")
        if x1==14:
            return("O")
        if x1==15:
            return("P")
        if x1==16:
            return("Q")
        if x1==17:
            return("R")
        if x1==18:
            return("S")
        if x1==19:
            return("T")
        if x1==20:
            return("U")
        if x1==21:
            return("V")
        if x1==22:
            return("W")
        if x1==23:
            return("X")
        if x1==24:
            return("Y")
        if x1==25:
            return("Z")
    def save():
        dool=coding()
        #print(dool)
        data,key=dool
        file_name="secret_file_"+str(key)
        #print(file_name)
        fw=open(file_name+".text","a")
        fw.write(data)
        fw.write("\n")
        fw.close()
        
    def coding():
        k=E2.get()
        k=int(k)
        data=E1.get()
        #print(k,data)
        rel_data=[]
        for i in data:
            if i==" ":
                rel_data.append(" ")
            else:
                v=identer(i)
                v1=(v+k)%26
                #print(v1)
                rel_data.append(identer2(v1))
        encode_data="".join(rel_data)
        print(encode_data)
        print(rel_data)
        L4.config(text=encode_data,fg="green",padx=10,pady=10,font=("italic",28))
        B2=Button(tip,text="Save --> File",bg="red",fg="white",font=(10,),command=save)
        B2.grid(row=10,column=0,columnspan=6)
        return(encode_data,k)



    #structure***********

    photo = PhotoImage(file = 'index.png')
    photo = photo.subsample(1)
    lbl = Label(tip,image = photo)
    lbl.image = photo
    lbl.grid(row=0,column=0,columnspan=6)
    L1=Label(tip,text="ENTER MESSAGE :",font=("bold",20),padx=10,pady=10)
    L1.grid(row=1,column=0)
    E1=Entry(tip,bd=5)
    E1.grid(row=1,column=1,padx=40)
    L2= Label(tip,text="KEY :",font=("bold",20),padx=10,pady=5)
    L2.grid(row=2,column=0)
    E2=Entry(tip,bd=5)
    E2.grid(row=2,column=1,padx=40)
    lbl1=Label(tip)
    lbl1.grid(row=5,column=0)
    B1=Button(tip,text="ENCODE \n MSG",bg="red",fg="white",font=("bold",14),command=coding)
    B1.grid(row=6,column=0,columnspan=6)
    lbl2=Label(tip)
    lbl2.grid(row=7,column=0)
    L3=Label(tip,text="DECODED MSG\n    ||\n    ||",font=(10,))
    L3.grid(row=8,column=0,columnspan=6)
    L4=Label(tip,text="")
    L4.grid(row=9,column=0,columnspan=6)
    


    tip.mainloop()
#encode_msg2()
