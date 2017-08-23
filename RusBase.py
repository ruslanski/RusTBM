#!usr/bin/env python3
#RusBase Software
#Author: Ruslan Shakirov
#https://github.com/ruslanski/RusBase
#Date: 08/21/2017

from tkinter import *
import random
import time;
import subprocess

#Size of Windows Frame and its Title.
root=Tk()
root.geometry("800x600+0+0")
root.title("RusBase PC")

text_Input=StringVar()

#Frame for Top Name 
Tops=Frame(root, width=800, height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

#Left Side(For Buttons)
f1=Frame(root,width=800, height=600, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

#Right Side (For Buttons)
f2=Frame(root,width=800, height=600, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

#Time
localtime=time.asctime(time.localtime(time.time()))

#Top Name and Local Time
lblInfo=Label(Tops, font=('arial',20,'bold'), text="RusBase",fg="Steel Blue", bd=10, anchor="w")
lblInfo.grid(row=0, column=0)
lblInfo=Label(Tops, font=('arial',8,'bold'), text=localtime,fg="Steel Blue", bd=10, anchor="w")
lblInfo.grid(row=1,column=0)

#BUTTONS 
def btnClick(btn):
    # Code below is from Stack Overflow(User 'extraneon'). URL:stackoverflow.com/questions/1811691/running-an-outside-program-executable-in-python
    btn = subprocess.Popen(["RogueKiller.exe"], \
    stderr=subprocess.PIPE)
    if btn.stderr:
        print (btn.stderr.readlines())
    

#Left Side
btn1=Button(f1, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 1",bg="powder blue",command=lambda: btnClick(1)).grid(row=0,column=0)

btn2=Button(f1, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 2",bg="powder blue",command=lambda: btnClick(2)).grid(row=1,column=0)

btn3=Button(f1, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 3",bg="powder blue",command=lambda: btnClick(3)).grid(row=2,column=0)

btn4=Button(f1, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f1, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 5",bg="powder blue",command=lambda: btnClick(5)).grid(row=4,column=0)

btn6=Button(f1, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 6",bg="powder blue",command=lambda: btnClick(6)).grid(row=5,column=0)

#Right Side
btn7=Button(f2, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 7",bg="powder blue",command=lambda: btnClick(7)).grid(row=0,column=0)

btn8=Button(f2, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 8",bg="powder blue",command=lambda: btnClick(8)).grid(row=1,column=0)

btn9=Button(f2, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=0)

btn10=Button(f2, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 10",bg="powder blue",command=lambda: btnClick(10)).grid(row=3,column=0)

btn11=Button(f2, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 11",bg="powder blue",command=lambda: btnClick(11)).grid(row=4,column=0)

btn12=Button(f2, padx=8,pady=4,bd=2,fg="black",font=('arial',20,'bold'),
            text="Button 12",bg="powder blue",command=lambda: btnClick(12)).grid(row=5,column=0)

root.mainloop()
