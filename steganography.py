# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:57:44 2020

@author: mohin
"""


import cv2
import os
d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
  
x=cv2.imread("ganache.jpg")

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("Enter key to secure : ")
text=input("Enter text to hide : ")

kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]
    n=n+1
    m=m+1
    m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
    kl=(kl+1)%len(key)
    
cv2.imwrite("encrypted_img.jpg",x) 
os.startfile("encrypted_img.jpg")
print("Data Hiding in Image completed successfully.")
#x=cv2.imread(“encrypted_img.jpg")
    

kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column

ch = input("\nDo you want to extract data from Image :(Y/N)")

if ch == ("y"):
    key1=input("\n\nRe enter key to extract text : ")
    decrypt=""

    if key == key1 :
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[kl]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            kl=(kl+1)%len(key)
        print("Encrypted text was : ",decrypt)
    else:
        print("Key doesn't match.")
else:
    print("Thank you. EXITING.")
  