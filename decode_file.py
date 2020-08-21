from tkinter import *
import time
def decode_file(f):
    global o;
    o=f
    o=int(o)
    #print(o)
    global dec
    global dat_num
    def identer3(x2):
        if x2==0:
            return("A")
        if x2==1:
            return("B")
        if x2==2:
            return("C")
        if x2==3:
            return("D")
        if x2==4:
            return("E")
        if x2==5:
            return("F")
        if x2==6:
            return("G")
        if x2==7:
            return("H")
        if x2==8:
            return("I")
        if x2==9:
            return("J")
        if x2==10:
            return("K")
        if x2==11:
            return("L")
        if x2==12:
            return("M")
        if x2==13:
            return("N")
        if x2==14:
            return("O")
        if x2==15:
            return("P")
        if x2==16:
            return("Q")
        if x2==17:
            return("R")
        if x2==18:
            return("S")
        if x2==19:
            return("T")
        if x2==20:
            return("U")
        if x2==21:
            return("V")
        if x2==22:
            return("W")
        if x2==23:
            return("X")
        if x2==24:
            return("Y")
        if x2==25:
            return("Z")
    def identer4(x):
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
    def deplot():
        dat=dec
        #print(dat)
        sec_rel_dat=[]
        for i in dat:
            for j in i:
                if j==" ":
                    sec_rel_dat.append(" ")
                elif j=="\n":
                    sec_rel_dat.append("\n")
                else:
                    num=identer4(j)
                    dat_num=num-o
                    if dat_num>=0:
                        sec_rel_dat.append(identer3(dat_num))
                    else:
                        ji=26+dat_num
                        sec_rel_dat.append(identer3(ji))
        #print(sec_rel_dat)
        lol="".join(sec_rel_dat)
        #print(lol)
        L2.config(text=lol)            
                    
                    
                
                
                
    
    decode=Tk()
    decode.title("DECODING")
    name1="secret_file_"+str(f)
    frr=open(name1+".text","r")
    dec=frr.readlines()
    #print(dec)
    #print(len(dec))
    frr.close()
    photo = PhotoImage(file = 'imageegwrs.png')
    photo = photo.subsample(1)
    lbl5 = Label(decode,image = photo)
    lbl5.image = photo
    lbl5.grid(row=0,column=0,columnspan=6)
    lbl3=Label(decode)
    lbl3.grid(row=1,column=0)
    L1=Label(decode,text="   Decode File  ",font=("bold",35,),bg="red",fg="white",padx=40)
    L1.grid(row=2,column=0)
    L1=Label(decode,text="   Decode File  ",font=("bold",35,),bg="red",fg="white",padx=40)
    L1.grid(row=2,column=0)
    blk=Label(decode,text="")
    blk.grid(row=3,column=0)
    L2=Label(decode,text="",font=("bold",20,),fg="black")
    L2.grid(row=3,column=0)
    B1=Button(decode,text="##Decode##",bg="green",fg="white",font=("bold",14,),command=deplot,padx=10,pady=10)
    B1.grid(row=4,column=0)
    
    
    
    
    
    decode.mainloop()
#decode_file(5)    
    
    
