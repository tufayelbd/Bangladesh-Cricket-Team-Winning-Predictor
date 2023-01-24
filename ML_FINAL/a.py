#import BangladeshWinningPredictor as BD
import pandas as pd
import math
import numpy as np
from tkinter import *
from tkinter import ttk

from tkinter import messagebox


global labelR
global venueT
global opnentT
global tamimF
global shakibF
global fizzF
global musiF
global x
x=pd.read_csv("test_test.csv")

#global x=pd.read_csv("test_test.csv")


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Bangladesh Winning Predictor !")
        self.minsize(640, 400)
        self.maxsize(640,400)
        self.wm_iconbitmap("icon.ico")
        self.configure(background="#4D4D4D")
                       
        self.img=PhotoImage(file="imoji.png")

        l=Label(image=self.img,background="#4D4D4D")
        l.place(x=450,y=100)
        
        self.Design()
    def CloseWindow(self):
        root.destroy()

    def FindResult(self):
        global labelR

        global venueT
        global opnentT
        global tamimF
        global shakibF
        global fizzF
        global musiF
        Venue=venueT.get()
        Oponent=opnentT.get()
        tamimR=tamimF.get()
        shakibR=shakibF.get()
        musiR=musiF.get()
        fizzW=fizzF.get()
        print(Venue)
        print(Oponent)

        labelR.configure(text="HELO"+Venue)
        print("Passed Result ")
        if Venue =="Select Venue ?" or Oponent =="Select Oponent ?":

            if Venue =="Select Venue ?":
                messagebox.showerror("Error", "Please Select Field !")
            else:
                messagebox.showwarning("Warning", "Sure This Is New Opponent !")
        Data=[Venue,Oponent,tamimR,shakibR,musiR,fizzW]

        FindEuclideanDistance(Data)



        

        #self.label.config(text="HJKL: ", bg="#4D4D4D")

    # self.labelR.config(text="dhjk")
        #labelR.config (text="djknzmc")
        #
        #labelR.config(text="PK")


    def Design(self):
        global labelR
        global venueT
        global opnentT
        global tamimF
        global shakibF
        global fizzF
        global musiF
        labelR=Label(self,text=" ",width=70,height=3)
        labelR.place(x=70,y=330)
        label=Label(self,text=" Please Give The Information Below  ",bg="#4D4D4D")
        #label.grid(column=0,row=0)
        label.place(x=255,y=10)

        venueL=Label(self,text="Where The Venue Is : Home or Away ")

        venueL.place(x=70,y=95)
        venueT=ttk.Combobox(self,width=20,state="readonly")
        venueT["values"] = ("Select Venue ?", "Home", "Away")
        venueT.current(0)

        venueT.place(x=285,y=95)

        opnentL=Label(self,text=" Which is the Oponent Team  ")

        opnentL.place(x=70,y=125)
        opnentT=ttk.Combobox(self,width=20,state="readonly")
        opnentT["values"] = ("Select Oponent ?", "AFG", "AUS","IND","NZW","PAK","ENG","SA","SRI","ZIM","WID")

        opnentT.current(0)

        opnentT.place(x=285,y=125)
#Tamim Label
        labelT=Label(self,text="Tamim get Score : ")
        labelT.place(x=70,y=155)
        tamimF=ttk.Entry(self,width=20)
        tamimF.place(x=285,y=155)
#Shakib Label

        labelT = Label(self, text="Shakib get Score : ")
        labelT.place(x=70, y=185)
        shakibF = ttk.Entry(self, width=20)
        shakibF.place(x=285, y=185)
# Mushfique Label

        labelM = Label(self, text="Mushfique get Score : ")
        labelM.place(x=70, y=215)
        musiF = ttk.Entry(self, width=20)
        musiF.place(x=285, y=215)
# Fizz Label

        labelF = Label(self, text="Fizz get Wicket : ")
        labelF.place(x=70, y=245)
        fizzF = ttk.Entry(self, width=20)
        fizzF.place(x=285, y=245)
#Buttn
#        Button(top, text="Clicked Me", command=Pass)
        button =Button(self,
                   text="QUIT",
                   fg="red",
                   command=self.CloseWindow)
        button.place(x=590,y=360)
        button2 =Button(self,
                   text="Show Prediction Result ",
                   fg="red",width=40,
                   command=self.FindResult)
        button2.place(x=150,y=290)

class FindEuclideanDistance:
    
    def PassResult(wD,d,x):
        print(wD)
        print(d)
        print(x)
        
class FindEuclideanDistance:
    def __init__(self,Data):
        print("HSSHS")
        print(Data)
        global x
        print(x)
        fild=Data[0]
        opName=Data[1]
        oponentTeam=x[x["Oponent"]==opName]
        
        optVenueMatch=oponentTeam[oponentTeam["Venue"]==fild]
        if oponentTeam.empty:
            print(" Bangladesh Win This Match")
        elif optVenueMatch.empty:
            
            print("50 % ")
        else:
            print(oponentTeam)
            print()
            print("8888888888888888888 Venu and Oponent 88888888888888888888888")
            print(optVenueMatch)
            s=[]
            for length in optVenueMatch.Shakib:
                print("I",Data[3])
                t1=int(Data[3])
                t2=int(length)
                a=(t2-t1)**2
                s.append(a)
                print("Lengt",a)
            print("Shakib",s)
            t=[]
            for length in optVenueMatch.Tamim:
               # print("I",Player[1])
                t1=int(Data[2])
                t2=int(length)
                a=(t2-t1)**2
                t.append(a)
                print("Lengt",t)
            print("Tamim",t)
            f=[]
            for length in optVenueMatch.Fizz:
               # print("I",Player[2])
                t1=int(Data[5])
                t2=int(length)
                a=(t2-t1)**2
                f.append(a)
                print("Lengt",f)
            print("Fizz ",f)
            m=[]
            for length in optVenueMatch.Mushfiq:
              #  print("I",Player[3])
                t1=int(Data[4])
                t2=int(length)
                a=(t2-t1)**2
                m.append(a)
                print("Lengt",a)
            print("Mushfique ",m)
            
            
            d=[]
            for i in range(len(s)):
                
                print("IIIIIIII ",i)
                sumall=s[i]+t[i]+m[i]+f[i]
                dd=math.sqrt(sumall)
                print(dd,"D")
                d.append(dd)
                print("Dis ",d)
            print("DDDDDDDDDDDDD",d)
            print()
            wD={}
            winLostList=[]
            for i in optVenueMatch["Result"]:
                if i=="w":
                    winLostList.append("w")
                else:
                    winLostList.append("l")
            wD["Result"]=winLostList
                    
            print("Winning",wD)
            print()
            tt={}
            #list Korram Euclidean distance er satay Win Od Loss
            for i in range(len(d)):
                print(winLostList[i])
                print(d[i])
                tt[winLostList[i]]=d[i]
                
                print()
            print("TTTTTTT",tt)
            
            print("*************************************************************************")     
            print(wD)
            print(d)
            print(winLostList)       
            obED=FindEuclideanDistanceR(wD,d,winLostList)
           
class FindEuclideanDistanceR:
    
    def __init__(self,wD,d,winLostList):
        print("List OF Win Loss ",winLostList)
        print("Function D ",d)
        print("Function Win ",wD)
       
        print(".....................................Chowdhury Tufayel............................................................")
        
        L=[]
        for i in range(len(d)):
            DH={}
            print("D",d[i])
            print("W/L",winLostList[i])
            a=winLostList[i]
            b=d[i]
            DH[a]=b
            L.append(DH)
            print(L)
            print("DIC :",DH)
        print("LASt",L)
        FindList(L,d)
class FindList:
    def __init__(self,L,d):
        rank=[]
        print("Distance ",d)
        for i in range(1,4):
            b=min(d)
            rank.append(b)
            d.remove(b)
            print("rank : ",rank)
        print("R::::",rank)
        
        R=[]
        k=0
        for i in L:
            for j in i:
                print("J",j)
                r=j
                print(i[j])
                check=i[j]
                
                if k <4:
                    k=k+1
                    
                    if check in rank:
                        R.append(r)
                        print("R",R)
        print("**********R",R)
        
        w=0
        l=0
        for i in R:
            
            if i =="w":
                w=w+1
            else:
                l=l+1
        print("Win",w)
        print("lost",l)
        if w>l:
            print("Bangladesh Win ")
        else:
            print("Bangladesh Loss")
        
        
                    
                
        
        
        
            

root=Root()

root.mainloop()