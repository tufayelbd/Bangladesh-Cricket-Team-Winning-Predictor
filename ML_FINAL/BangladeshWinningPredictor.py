# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:26:21 2018

@author: Nabid's Laptop
"""


import pandas as pd
import math 
x=pd.read_csv("test_test.csv")

class Make_numeric:
    def __init__(self,opName,fild,Player):
        
        
        oponentTeam=x[x["Oponent"]==opName]
        
        optVenueMatch=oponentTeam[oponentTeam["Venue"]==fild]
        if oponentTeam.empty:
            print(" Bangladesh Win This Match")
        elif optVenueMatch.empty:
            
            print("50 % ")
        else:
            print(oponentTeam)
            print("******************************VenueMatch : Oponenet Valnue Wise Match : ************************************************************")
            print()
            print(optVenueMatch)
            print()
           
            print("****************TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT**************************************************************************")
                
           # o=[50,40,50,5]
            s=[]
            for length in optVenueMatch.Shakib:
                print("I",Player[0])
                print("O",Player)
                a=(length-Player[0])**2
                s.append(a)
                print("Lengt",a)
            print("Shakib",s)
            t=[]
            for length in optVenueMatch.Tamim:
                print("I",Player[1])
                print("O",Player)
                a=(length-Player[1])**2
                t.append(a)
                print("Lengt",t)
            print("Tamim",t)
            f=[]
            for length in optVenueMatch.Fizz:
                print("I",Player[2])
                print("O",Player)
                a=(length-Player[2])**2
                f.append(a)
                print("Lengt",f)
            print("Fizz ",f)
            m=[]
            for length in optVenueMatch.Mushfiq:
                print("I",Player[3])
                print("O",Player)
                a=(length-Player[3])**2
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
            R=[]
            #list Korram Euclidean distance er satay Win Od Loss
            for i in range(len(d)):
                print(winLostList[i])
                print(d[i])
                tt[winLostList[i]]=d[i]
                
                print()
            print("TTTTTTT",tt)
            
            print("*************************************************************************")       
            obED=FindEuclideanDistance(wD,d,winLostList)
            
            
             
class FindEuclideanDistance:
    
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
        
        
                    
                
        
        
        
            
            
       

    
opName=input("Enter Oponet ")
fild=(input("Enter Home Or Away Match : "))

Player=[]

for i in range(4):
    if i ==0:
        PalayerValue=int(input("Shakib"))

        Player.append(PalayerValue)
    elif i==1:
        PalayerValue=int(input("Tamim"))
        Player.append(PalayerValue)
        
    elif i==2:
        PalayerValue=int(input("Mushfique"))
        Player.append(PalayerValue)
    elif i==3:
        PalayerValue=int(input("Fizz"))
        Player.append(PalayerValue)
    else:
        Player.append(PalayerValue)


print("Player Value : ",Player)
#print("GSGG",oponentTeam)

ob=Make_numeric(opName,fild,Player)



