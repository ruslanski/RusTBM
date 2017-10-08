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
        self.tab_buttons()

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

    def tab_buttons(self):
         """
         """
         tab1 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         tab2 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         tab3 = Frame(note, width=800, height=500, bg="powder blue", relief=SUNKEN)
         note.add(tab1, text = "OS Tools")
         note.add(tab2, text = "End-User Software")
         note.add(tab3, text = "Remove")
         note.pack()

         #Place buttons in first column of tab1.
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
         
         #Place buttons in second column of tab1.
         
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

        
         #Place buttons in first column of tab2.
         btn25=Button(tab2,padx=60,bd=2,fg="black",font=('arial',10,'bold'),text="Ninite",command=self.btn1Click)
         btn25.place(x=8,y=10)

         btn26=Button(tab2,padx=28,bd=2,fg="black",font=('arial',10,'bold'),text="Google Chrome",command='')
         btn26.place(x=8,y=50)

         btn27=Button(tab2,padx=8,bd=2,fg="black",font=('arial',10,'bold'),text="Chrome Cleanup Tool",command='')
         btn27.place(x=8, y=90)

         btn27=Button(tab2,padx=31,bd=2,fg="black",font=('arial',10,'bold'),text="Mozilla Firefox",command='')
         btn27.place(x=8, y=130)

         btn28=Button(tab2,padx=58,bd=2,fg="black",font=('arial',10,'bold'),text="Opera",command='')
         btn28.place(x=8, y=170)

         btn29=Button(tab2,padx=63,bd=2,fg="black",font=('arial',10,'bold'),text="7-Zip",command='')
         btn29.place(x=8,y=210)

         btn30=Button(tab2,padx=53,bd=2,fg="black",font=('arial',10,'bold'),text="WinRaR",command='')
         btn30.place(x=8,y=250)
         
         btn31=Button(tab2,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="Skype",command='')
         btn31.place(x=8,y=290)

         btn32=Button(tab2,padx=40,bd=2,fg="black",font=('arial',10,'bold'),text="Thunderbird",command='')
         btn32.place(x=8, y=330)

         btn33=Button(tab2,padx=52,bd=2,fg="black",font=('arial',10,'bold'),text="Dropbox",command='')
         btn33.place(x=8, y=370)

         btn34=Button(tab2,padx=38,bd=2,fg="black",font=('arial',10,'bold'),text="Google Drive",command='')
         btn34.place(x=8, y=410)

         btn35=Button(tab2,padx=50,bd=2,fg="black",font=('arial',10,'bold'),text="OneDrive",command='')
         btn35.place(x=8,y=450)
         
         #Place buttons in second column of tab1.
         
         btn36=Button(tab2,padx=53 ,bd=2,fg="black",font=('arial',10,'bold'),text="ITunes",command=self.btn1Click)
         btn36.place(x=230,y=10)

         btn37=Button(tab2,padx=61,bd=2,fg="black",font=('arial',10,'bold'),text="VLC",command='')
         btn37.place(x=230,y=50)

         btn38=Button(tab2,padx=57,bd=2,fg="black",font=('arial',10,'bold'),text="AIMP",command='')
         btn38.place(x=230, y=90)

         btn39=Button(tab2,padx=48,bd=2,fg="black",font=('arial',10,'bold'),text="Winamp",command='')
         btn39.place(x=230, y=130)

         btn40=Button(tab2,padx=31,bd=2,fg="black",font=('arial',10,'bold'),text="K-Lite Codecs",command='')
         btn40.place(x=230, y=170)

         btn41=Button(tab2,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="GOM",command='')
         btn41.place(x=230,y=210)

         btn42=Button(tab2,padx=52,bd=2,fg="black",font=('arial',10,'bold'),text="Spotify",command='')
         btn42.place(x=230,y=250)
         
         btn43=Button(tab2,padx=54,bd=2,fg="black",font=('arial',10,'bold'),text="Java 8",command='')
         btn43.place(x=230,y=290)

         btn44=Button(tab2,padx=39,bd=2,fg="black",font=('arial',10,'bold'),text="NotePad++",command='')
         btn44.place(x=230, y=330)

         btn45=Button(tab2,padx=48,bd=2,fg="black",font=('arial',10,'bold'),text="WinSCP",command='')
         btn45.place(x=230, y=370)

         btn46=Button(tab2,padx=58,bd=2,fg="black",font=('arial',10,'bold'),text="Putty",command='')
         btn46.place(x=230, y=410)

         btn47=Button(tab2,padx=49,bd=2,fg="black",font=('arial',10,'bold'),text="FileZilla",command='')
         btn47.place(x=230,y=450)

    def btn1Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkMWJlSDRlYTlmczA', 'CrystalDisk.exe')
        file="CrystalDisk.exe"
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
