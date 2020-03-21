# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:15:31 2020

@author: Vaibhav Haswani
"""

from random import randint
#from random import choice
from tkinter import *


def randChr(num=False,sym=False,up=False,low=False):
    chr_li=[]
    n=-1
    if num:     
        chr_li.append(randint(48,57)) #number generation
        n+=1
    if sym:
        chr_li.append(randint(33,45)) #Symbol "
        n+=1
        chr_li.append(randint(63,64))
        n+=1
    if up:
        chr_li.append(randint(65,90)) #UpperCase "
        n+=1
    if low:
        chr_li.append(randint(97,122)) #lowerCase "
        n+=1
    chr_li=list(map(chr,chr_li))       #casting list to its ascii chrs
    if(n==-1):
        return -1
    else:
        return str(chr_li[randint(0,n)])   #returning random chr from list as string



def generate(): 
    password=""
    
    
    
    for i in range(size.get()):
        temp=randChr(num=cn.get(),sym=cs.get(),up=cu.get(),low=cl.get())
        if temp==-1:
            password=-1
            break
        password=password+temp
    if password==-1:
        messagebox.showinfo("Alert!","Can't Generate Password without any selection")
    else:    
        pas.set(password)    
        msg=Label(app,text="(  Copy it on clipboard! )",font=("gabriola",11)).place(x=87,y=285)
        messagebox.showinfo("Congratulations!","Password Generated !!")
        
    


        
app=Tk()
app.geometry("300x400+500+100")
app.iconbitmap("icon.ico")
app.title("Password Generator v1.0")
pas=StringVar()
size=IntVar()
size.set(8)
cu=BooleanVar()
cu.set(True)
cl=BooleanVar()
cl.set(True)
cn=BooleanVar()
cn.set(True)
cs=BooleanVar()
cs.set(True)

appL=Label(app,text="Password Generator v1.0",bg="black",fg="white",relief="solid",font=("constantia",17,"bold"))
appL.pack(fill=BOTH,padx=2,pady=2)
sizeL=Label(app,text="Enter Size:",font=("gabriola",14))
sizeL.place(x=50,y=80)
sizeIn=Entry(app,textvar=size).place(x=130,y=90)


uc=Checkbutton(app,text="Include UpperCase Letters",font=("gabriola",12),variable=cu).place(x=60,y=130)
ul=Checkbutton(app,text="Include LowerCase Letters",font=("gabriola",12),variable=cl).place(x=60,y=160)
un=Checkbutton(app,text="Include Numbers",font=("gabriola",12),variable=cn).place(x=60,y=190)
us=Checkbutton(app,text="Include Symbols",font=("gabriola",12),variable=cs).place(x=60,y=220)
pasBox=Entry(app,width=30,textvar=pas).place(x=60,y=265)


btn=Button(app,text="GENERATE",fg="white",bg="gray",borderwidth=2,relief="groove",font=("garamond",15),command=generate).place(x=85,y=330)
msg=Label(app,text="Developed by ~ Vaibhav Haswani",font=("cambria",9)).place(x=65,y=40)
   
app.mainloop()






    
 
    
