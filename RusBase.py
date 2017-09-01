#!usr/bin/env python3
#RusBase Software
#Author: Ruslan Shakirov
#https://github.com/ruslanski/RusBase
#Date: 08/21/2017

from tkinter import *
import random
import time;
import subprocess
import urllib

class Application(Frame):
    """GUI application with twelve buttons"""

    def __init__(self,master):
        self.master = master
        self.logo()
        self.create_widgets()
        
    def logo(self):
        #Set frame size and style for Logo 
        Tops=Frame(root, width=800, height=50,bg="powder blue",relief=SUNKEN)
        Tops.pack(side=TOP)
        #Set attributes of Logo
        lblInfo=Label(Tops, font=('arial',20,'bold'), text="RusBase",fg="Steel Blue", bd=10, anchor="w")
        #Place Logo
        lblInfo.grid(row=0, column=0)
        localtime=time.asctime(time.localtime(time.time()))

        #Set attributes of Time 
        lblInfo=Label(Tops, font=('arial',8,'bold'), text=localtime,fg="Steel Blue", bd=10, anchor="w")
        #Place Time
        lblInfo.grid(row=1,column=0)

    def create_widgets(self):
        """Function below sets attributes for left and right sides.
        Creates 12 buttons. 6 on the left side. 6 on the right side
        """
        #Left Side(For Buttons)
        f1=Frame(root,width=200, height=300, bg="powder blue", relief=SUNKEN)
        f1.pack(side=LEFT)

        #Right Side (For Buttons)
        f2=Frame(root,width=200, height=300, bg="powder blue", relief=SUNKEN)
        f2.pack(side=RIGHT)

        #Create first buttom
        btn1=Button(f1, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
                    text="Button 1",bg="powder blue",command=lambda: btnClick(1)).grid(row=0,column=0)
        #Create second button
        btn2=Button(f1, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
                    text="Button 2",bg="powder blue",command=lambda: btnClick(2)).grid(row=1,column=0)
        #Create third button
        btn3=Button(f1, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
                    text="Button 3",bg="powder blue",command=lambda: btnClick(3)).grid(row=2,column=0)
        #Create fourth button
        btn4=Button(f1, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
                    text="Button 4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)
        #Create fivth button
        btn5=Button(f1, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
                    text="Button 5",bg="powder blue",command=lambda: btnClick(5)).grid(row=4,column=0)
        #Create sixth button
        btn6=Button(f1, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
                    text="Button 6",bg="powder blue",command=lambda: btnClick(6)).grid(row=5,column=0)

        #Right Side
        #Create seventh button
        btn7=Button(f2, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
            text="Button 7",bg="powder blue",command=lambda: btnClick(7)).grid(row=0,column=0)

        #Create eights button
        btn8=Button(f2, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
            text="Button 8",bg="powder blue",command=lambda: btnClick(8)).grid(row=1,column=0)

        #Create nineth button
        btn9=Button(f2, padx=8,pady=3,bd=2,fg="black",font=('arial',15,'bold'),
            text="Button 9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=0)
        #Create tenth button
        btn10=Button(f2, padx=8,pady=3,bd=2,fg="black",font=('arial',14,'bold'),
            text="Button10",bg="powder blue",command=lambda: btnClick(10)).grid(row=3,column=0)
        #Create eleventh button
        btn11=Button(f2, padx=8,pady=3,bd=2,fg="black",font=('arial',14,'bold'),
            text="Button11",bg="powder blue",command=lambda: btnClick(11)).grid(row=4,column=0)
        #Create twelveth button
        btn12=Button(f2, padx=8,pady=3,bd=2,fg="black",font=('arial',14,'bold'),
            text="Button12",bg="powder blue",command=lambda: btnClick(12)).grid(row=5,column=0)
        
        
#Size of Window Frame and its Title.
root = Tk()
root.title("RusBase PC")
root.geometry("400x600+0+0")
app = Application(root)
root.mainloop()
