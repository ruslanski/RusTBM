#!usr/bin/env python3
#RusBase Software
#Author: Ruslan Shakirov
#https://github.com/ruslanski/RusBase
#Date: 08/21/2017

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
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
        Tops=Frame(root)
        Tops.pack(side=TOP)
        #Set attributes of Logo
        lblInfo=Label(Tops, font=('arial',20,'bold'), text="RusBase",fg="Steel Blue", bd=10,anchor="w")
        #Place Logo
        lblInfo.grid(row=1, column=0)
        localtime=time.asctime(time.localtime(time.time()))

        #Set attributes of Time 
        lblInfo=Label(Tops, font=('arial',8,'bold'), text=localtime,fg="Steel Blue", bd=10, anchor="w")
        #Place Time
        lblInfo.grid(row=2,column=0)
        
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
         """
         tab1 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         tab2 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         tab3 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         note.add(tab1, text = "OS Tools")
         note.add(tab2, text = "Audit 2")
         note.add(tab3, text = "Remove")
         note.pack()

         """T = Text(tab1, height=1, width=5, bg="powder blue",fg="black",font=('arial',13,'bold'))
         T.pack()
         T.insert(END, "HDD")
         T.place(x=0,y=10)"""
         
         #Placing first six buttons in tab1.
         btn1=Button(tab1,padx=41,bd=2,fg="black",font=('arial',10,'bold'),text="Crystal Disk",command=self.btn1Click)
         btn1.place(x=8,y=10)

         btn2=Button(tab1,padx=32,bd=2,fg="black",font=('arial',10,'bold'),text="HDD Guardian",command='')
         btn2.place(x=8,y=50)

         btn3=Button(tab1,padx=37,bd=2,fg="black",font=('arial',10,'bold'),text="Victoria HDD",command='')
         btn3.place(x=8, y=90)

         btn4=Button(tab1,padx=49,bd=2,fg="black",font=('arial',10,'bold'),text="Autoruns",command='')
         btn4.place(x=8, y=130)

         btn5=Button(tab1,padx=46,bd=2,fg="black",font=('arial',10,'bold'),text="MSConfig",command='')
         btn5.place(x=8, y=170)

         btn6=Button(tab1,padx=18,bd=2,fg="black",font=('arial',10,'bold'),text="Check LAN+WLAN",command='')
         btn6.place(x=8,y=210)

         btn7=Button(tab1,padx=47,bd=2,fg="black",font=('arial',10,'bold'),text="CCleaner",command='')
         btn7.place(x=8,y=250)
         
         btn8=Button(tab1,padx=62,bd=2,fg="black",font=('arial',10,'bold'),text="RKill",command='')
         btn8.place(x=8,y=290)

         btn9=Button(tab1,padx=39,bd=2,fg="black",font=('arial',10,'bold'),text="RogueKiller",command='')
         btn9.place(x=8, y=330)

         btn10=Button(tab1,padx=33,bd=2,fg="black",font=('arial',10,'bold'),text="Malwarebytes",command='')
         btn10.place(x=8, y=370)

         btn11=Button(tab1,padx=35,bd=2,fg="black",font=('arial',10,'bold'),text="ADW Cleaner",command='')
         btn11.place(x=8, y=410)

         btn12=Button(tab1,padx=62,bd=2,fg="black",font=('arial',10,'bold'),text="Revo",command='')
         btn12.place(x=8,y=450)


         
         
         btn13=Button(tab1,padx=41,bd=2,fg="black",font=('arial',10,'bold'),text="WinDirStat",command=self.btn1Click)
         btn13.place(x=230,y=10)

         btn14=Button(tab1,padx=20,bd=2,fg="black",font=('arial',10,'bold'),text="Console Portable",command='')
         btn14.place(x=230,y=50)

         btn15=Button(tab1,padx=21,bd=2,fg="black",font=('arial',10,'bold'),text="Process Explorer",command='')
         btn15.place(x=230, y=90)

         btn16=Button(tab1,padx=45,bd=2,fg="black",font=('arial',10,'bold'),text="WinAudit",command='')
         btn16.place(x=230, y=130)

         btn17=Button(tab1,padx=34,bd=2,fg="black",font=('arial',10,'bold'),text="Patch My PC",command='')
         btn17.place(x=230, y=170)

         btn18=Button(tab1,padx=7,bd=2,fg="black",font=('arial',10,'bold'),text="Sys Restore Manager",command='')
         btn18.place(x=230,y=210)

         btn19=Button(tab1,padx=40,bd=2,fg="black",font=('arial',10,'bold'),text="GPU Shark",command='')
         btn19.place(x=230,y=250)
         
         btn20=Button(tab1,padx=24,bd=2,fg="black",font=('arial',10,'bold'),text="GeekUninstaller",command='')
         btn20.place(x=230,y=290)

         btn21=Button(tab1,padx=51,bd=2,fg="black",font=('arial',10,'bold'),text="Recuva",command='')
         btn21.place(x=230, y=330)

         btn22=Button(tab1,padx=7,bd=2,fg="black",font=('arial',10,'bold'),text="Complete Win Repair",command='')
         btn22.place(x=230, y=370)

         btn23=Button(tab1,padx=13,bd=2,fg="black",font=('arial',10,'bold'),text="Win System Control",command='')
         btn23.place(x=230, y=410)

         btn24=Button(tab1,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="Revo",command='')
         btn24.place(x=230,y=450)

    def btn1Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
    def btn2Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
    def btn2Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
    def btn3Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
    def btn4Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
    def btn5Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
    def btn6Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
    def btn7Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkdkQyN0gtaUxNNkU', 'rufus-2.15.exe')
        file="rufus-2.15.exe"
        btn=subprocess.call([file], shell=True)
        
        
#Size of Window Frame and its Title.
root = Tk()
root.title("RusBase PC")
root.geometry("400x600+0+0")
note = ttk.Notebook(root)

app = Application(root)
root.mainloop()
if __name__ == '__main__':
    main()
