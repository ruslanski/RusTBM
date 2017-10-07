#!usr/bin/env python3
#RusBase Software
#Author: Ruslan Shakirov
#https://github.com/ruslanski/RusBase
#Date: 08/21/2017

from tkinter import *
from tkinter import ttk
import random
import time;
import subprocess
import urllib

class Application(Frame):
    """GUI application with twelve buttons"""

    def __init__(self,master):
        self.master = master
        self.logo()
        self.menu_bar()
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
        
    def menu_bar(self):
        #This is a menu of the main Window. 'menu' is smth we make. 'Menu' is reference from Tkinter
        menu=Menu(self.master)
        #Define instance of the menu
        self.master.config(menu=menu)
        #First bar of the menu
        file = Menu(menu)
        #Add buttons to first bar of the menu.
        file.add_command(label='Save', command='')
        file.add_command(label='Exit', command=root.destroy)
        #Add 'file' to the menu.
        menu.add_cascade(label='File', menu=file)

        #Second bar in the menu.
        edit=Menu(menu)
        edit.add_command(label='Undo', command='')
        #Add 'edit' to the menu.
        menu.add_cascade(label='Edit',menu=edit)

    def create_widgets(self):
         """
         Creates 12 buttons. 6 on the left side. 6 on the right side
         """
         tab1 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         tab2 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         tab3 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         note.add(tab1, text = "Tab One")
         note.add(tab2, text = "Tab Two")
         note.add(tab3, text = "Tab Three")
         note.pack()
         
         #Placing first six buttons in tab1.
         btn1=Button(tab1,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 1",bg="powder blue",command='')
         btn1.place(x=40,y=5)

         btn2=Button(tab1,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 2",bg="powder blue",command='')
         btn2.place(x=40,y=70)

         btn3=Button(tab1,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 3",bg="powder blue",command='')
         btn3.place(x=40, y=140)

         btn4=Button(tab1,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 4",bg="powder blue",command='')
         btn4.place(x=40, y=210)

         btn5=Button(tab1,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 5",bg="powder blue",command='')
         btn5.place(x=40, y=280)

         btn6=Button(tab1,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 6",bg="powder blue",command='')
         btn6.place(x=40,y=350)

         #Placing stack of buttons into tab2.

         btn7=Button(tab2,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 7",bg="powder blue",command='')
         btn7.place(x=40,y=5)

         btn8=Button(tab2,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 8",bg="powder blue",command='')
         btn8.place(x=40,y=70)

         btn9=Button(tab2,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 9",bg="powder blue",command='')
         btn9.place(x=40, y=140)

         btn10=Button(tab2,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 10",bg="powder blue",command='')
         btn10.place(x=40, y=210)

         btn11=Button(tab2,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 11",bg="powder blue",command='')
         btn11.place(x=40, y=280)

         btn12=Button(tab2,padx=140,bd=2,fg="black",font=('arial',18,'bold'),text="Button 12",bg="powder blue",command='')
         btn12.place(x=40,y=350)
        
        
#Size of Window Frame and its Title.
root = Tk()
root.title("RusBase PC")
root.geometry("500x600+0+0")
note = ttk.Notebook(root)

app = Application(root)
root.mainloop()
if __name__ == '__main__':
    main()
