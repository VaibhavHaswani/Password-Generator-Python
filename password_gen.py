# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:15:31 2020

@author: Vaibhav Haswani
"""

from random import randint
#from random import choice


def randChr(num=True,sym=True,up=True,low=True):
    chr_li=[]
    if num:     
        chr_li.append(randint(48,57)) #number generation
    if sym:
        chr_li.append(randint(33,45)) #Symbol "
        chr_li.append(randint(63,64))
    if up:
        chr_li.append(randint(65,90)) #UpperCase "
    if low:
        chr_li.append(randint(97,122)) #lowerCase "
    chr_li=list(map(chr,chr_li))       #casting list to its ascii chrs
    return str(chr_li[randint(0,4)])   #returning random chr from list as string
        
        

size=int(input("Enter size to generate:"))
 
password=""


for i in range(size):
    temp=randChr()
    password=password+temp


print(f"Your Generated password is :  {password} \n(Copy it on clipboard)")    
    
