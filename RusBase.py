#!usr/bin/env python3
#RusBase
#Version 0.0.6
#Author: Ruslan Shakirov
#https://github.com/ruslanski/RusBase
#Start Date: 08/21/2017

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random
import time
import Links

class Application(Frame):
    """GUI application with twelve buttons"""

    def __init__(self,master):
        self.master = master
        self.logo()
        self.menu_bar()
        self.tab_buttons()

    def logo(self):
        #Set frame size and style for Top Logo 
        #Tops=Frame(root)
        #Tops.pack(side=TOP)
        #Set frame size and style for Bottom Logo
        Bots=Frame(root)
        Bots.pack(side=BOTTOM)
        #Set attributes of Top Logo
        lblInfo=Label(root, font=('arial',22,'bold'), text="RusBase",fg="Steel Blue",bg="white smoke",height=1)
        #Place Top Logo
        lblInfo.pack(fill=BOTH, expand=1)
        #lblInfo.grid(row=1, column=0)
        #Set attributes of Bottom Logo
        blInfo=Label(Bots,text="By Ruslan Shakirov. rshak02@gmail.com")
        blInfo.pack(fill=BOTH, expand=1)
        #Place Bottom Logo
        blInfo.grid(row=15,column=0)
        tblInfo = Label(root, font=('arial', 15, 'bold'),fg="Steel Blue",bg="white smoke")
        tblInfo.pack(fill=BOTH, expand=1)
        
        def tick():
            # get the current local time from the PC
            time2 = time.strftime('%H:%M:%S')
            # if time string has changed, update it
            tblInfo.config(text=time2)
            # calls itself every 200 milliseconds
            # to update the time display as needed
            # could use >200 ms, but display gets jerky
            tblInfo.after(200,tick)
        tick()
        
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
         """This function creates tab1,tab2,tab3 inside main Window Frame.
            With the following attributes in paranthesis.
         """
         tab1 = Frame(note, bg="white smoke")
         tab2 = Frame(note, bg="white smoke")
         tab3 = Frame(note,bg="white smoke")
         tab1.configure(width=800, height=650)
         tab2.configure(width=800, height=650)
         tab3.configure(width=800, height=650)
         note.add(tab1, text = "OS Tools")
         note.add(tab2, text = "End-User Software")
         note.add(tab3, text = "Remove")
         note.pack()

         #First Column of tab1.
         #Each button has two variables with a link and a name of software.
         #Gets passed to btn1Click function of file Link.py
         Crystaldisk="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUm5JdXRic1FMN00"
         CrystaldiskFile="CrystalDisk.exe"
         btn1=Button(tab1,padx=41,bd=2,fg="black",font=('arial',10,'bold'),text="Crystal Disk",bg="light cyan",command=lambda: Links.L.btn1Click(CrystalDisk,CrystalDiskFile))
         btn1.place(x=8,y=10)

         Hddguardian=""
         HddguardianFile=""
         btn2=Button(tab1,padx=32,bd=2,fg="black",font=('arial',10,'bold'),text="HDD Guardian",bg="light cyan",command=lambda: Links.L.btn1Click(Hddguardian,HddguardianFile))
         btn2.place(x=8,y=50)

         Victoria=""
         VictoriaFile=""
         btn3=Button(tab1,padx=37,bd=2,fg="black",font=('arial',10,'bold'),text="Victoria HDD",bg="light cyan",command=lambda: Links.L.btn1Click(Victoria,VictoriaFile))
         btn3.place(x=8, y=90)

         Autoruns=""
         AutorunsFile=""
         btn4=Button(tab1,padx=49,bd=2,fg="black",font=('arial',10,'bold'),text="Autoruns",bg="light cyan",command=lambda: Links.L.btn1Click(Autoruns,AutorunsFile))
         btn4.place(x=8, y=130)

         Msconfig=""
         MsconfigFile=""
         btn5=Button(tab1,padx=46,bd=2,fg="black",font=('arial',10,'bold'),text="MSConfig",bg="light cyan",command=lambda: Links.L.btn1Click(Msconfig,MsconfigFile))
         btn5.place(x=8, y=170)

         btn6=Button(tab1,padx=18,bd=2,fg="black",font=('arial',10,'bold'),text="Check LAN+WLAN",bg="light cyan",command=lambda: Links.L.btn1Click(CrystalDisk,CrystalDiskFile))
         btn6.place(x=8,y=210)
         
         Ccleaner=""
         CcleanerFile=""
         btn7=Button(tab1,padx=47,bd=2,fg="black",font=('arial',10,'bold'),text="CCleaner",bg="light cyan",command=lambda: Links.L.btn1Click(Ccleaner,CcleanerFile))
         btn7.place(x=8,y=250)

         Rkill=""
         RkillFile=""
         btn8=Button(tab1,padx=62,bd=2,fg="black",font=('arial',10,'bold'),text="RKill",bg="light cyan",command=lambda: Links.L.btn1Click(Rkill,RkillFile))
         btn8.place(x=8,y=290)

         Roguekiller=""
         RoguekillerFile=""
         btn9=Button(tab1,padx=39,bd=2,fg="black",font=('arial',10,'bold'),text="RogueKiller",bg="light cyan",command=lambda: Links.L.btn1Click(Roguekiller,RoguekillerFile))
         btn9.place(x=8, y=330)

         Malwarebytes=""
         MalwarebytesFile=""
         btn10=Button(tab1,padx=33,bd=2,fg="black",font=('arial',10,'bold'),text="Malwarebytes",bg="light cyan",command=lambda: Links.L.btn1Click(Malwarebytes,MalwarebytesFile))
         btn10.place(x=8, y=370)

         Adwcleaner=""
         AdwcleanerFile=""
         btn11=Button(tab1,padx=36,bd=2,fg="black",font=('arial',10,'bold'),text="Adw Cleaner",bg="powder blue",command=lambda: Links.L.btn1Click(Adwcleaner,AdwcleanerFile))
         btn11.place(x=8, y=410)
         
         Revo=""
         RevoFile=""
         btn12=Button(tab1,padx=61,bd=2,fg="black",font=('arial',10,'bold'),text="Revo",bg="powder blue",command=lambda: Links.L.btn1Click(Revo,RevoFile))
         btn12.place(x=8,y=450)
         
         #Second Column of tab1.
         Windirstat=""
         WindirstatFile=""
         btn13=Button(tab1,padx=41,bd=2,fg="black",font=('arial',10,'bold'),text="WinDirStat",bg="powder blue",command=lambda: Links.L.btn1Click(CrystalDisk,CrystalDiskFile))
         btn13.place(x=230,y=10)
         """
         btn14=Button(tab1,padx=20,bd=2,fg="black",font=('arial',10,'bold'),text="Console Portable",command=self.btn14Click)
         btn14.place(x=230,y=50)

         btn15=Button(tab1,padx=21,bd=2,fg="black",font=('arial',10,'bold'),text="Process Explorer",command=self.btn15Click)
         btn15.place(x=230, y=90)

         btn16=Button(tab1,padx=45,bd=2,fg="black",font=('arial',10,'bold'),text="WinAudit",command=self.btn16Click)
         btn16.place(x=230, y=130)

         btn17=Button(tab1,padx=34,bd=2,fg="black",font=('arial',10,'bold'),text="Patch My PC",command=self.btn17Click)
         btn17.place(x=230, y=170)

         btn18=Button(tab1,padx=7,bd=2,fg="black",font=('arial',10,'bold'),text="Sys Restore Manager",command=self.btn18Click)
         btn18.place(x=230,y=210)

         btn19=Button(tab1,padx=40,bd=2,fg="black",font=('arial',10,'bold'),text="GPU Shark",command=self.btn19Click)
         btn19.place(x=230,y=250)
         
         btn20=Button(tab1,padx=24,bd=2,fg="black",font=('arial',10,'bold'),text="GeekUninstaller",command=self.btn20Click)
         btn20.place(x=230,y=290)

         btn21=Button(tab1,padx=51,bd=2,fg="black",font=('arial',10,'bold'),text="Recuva",command=self.btn21Click)
         btn21.place(x=230, y=330)

         btn22=Button(tab1,padx=7,bd=2,fg="black",font=('arial',10,'bold'),text="Complete Win Repair",command=self.btn22Click)
         btn22.place(x=230, y=370)

         btn23=Button(tab1,padx=13,bd=2,fg="black",font=('arial',10,'bold'),text="Win System Control",command=self.btn23Click)
         btn23.place(x=230, y=410)

         btn24=Button(tab1,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="Revo",command=self.btn24Click)
         btn24.place(x=230,y=450)

        
         #Place buttons in first column of tab2.
         btn25=Button(tab2,padx=60,bd=2,fg="black",font=('arial',10,'bold'),text="Ninite",command=self.btn25Click)
         btn25.place(x=8,y=10)

         btn26=Button(tab2,padx=28,bd=2,fg="black",font=('arial',10,'bold'),text="Google Chrome",command=self.btn26Click)
         btn26.place(x=8,y=50)

         btn27=Button(tab2,padx=8,bd=2,fg="black",font=('arial',10,'bold'),text="Chrome Cleanup Tool",command=self.btn27Click)
         btn27.place(x=8, y=90)

         btn27=Button(tab2,padx=31,bd=2,fg="black",font=('arial',10,'bold'),text="Mozilla Firefox",command=self.btn28Click)
         btn27.place(x=8, y=130)

         btn28=Button(tab2,padx=58,bd=2,fg="black",font=('arial',10,'bold'),text="Opera",command=self.btn29Click)
         btn28.place(x=8, y=170)

         btn29=Button(tab2,padx=63,bd=2,fg="black",font=('arial',10,'bold'),text="7-Zip",command=self.btn30Click)
         btn29.place(x=8,y=210)

         btn30=Button(tab2,padx=53,bd=2,fg="black",font=('arial',10,'bold'),text="WinRaR",command=self.btn31Click)
         btn30.place(x=8,y=250)
         
         btn31=Button(tab2,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="Skype",command=self.btn32Click)
         btn31.place(x=8,y=290)

         btn32=Button(tab2,padx=40,bd=2,fg="black",font=('arial',10,'bold'),text="Thunderbird",command=self.btn33Click)
         btn32.place(x=8, y=330)

         btn33=Button(tab2,padx=52,bd=2,fg="black",font=('arial',10,'bold'),text="Dropbox",command=self.btn34Click)
         btn33.place(x=8, y=370)

         btn34=Button(tab2,padx=38,bd=2,fg="black",font=('arial',10,'bold'),text="Google Drive",command=self.btn35Click)
         btn34.place(x=8, y=410)

         btn35=Button(tab2,padx=50,bd=2,fg="black",font=('arial',10,'bold'),text="OneDrive",command=self.btn36Click)
         btn35.place(x=8,y=450)
         
         #Place buttons in second column of tab1.
         
         btn36=Button(tab2,padx=53 ,bd=2,fg="black",font=('arial',10,'bold'),text="ITunes",command=self.btn37Click)
         btn36.place(x=230,y=10)

         btn37=Button(tab2,padx=61,bd=2,fg="black",font=('arial',10,'bold'),text="VLC",command=self.btn38Click)
         btn37.place(x=230,y=50)

         btn38=Button(tab2,padx=57,bd=2,fg="black",font=('arial',10,'bold'),text="AIMP",command=self.btn39Click)
         btn38.place(x=230, y=90)

         btn39=Button(tab2,padx=48,bd=2,fg="black",font=('arial',10,'bold'),text="Winamp",command=self.btn40Click)
         btn39.place(x=230, y=130)

         btn40=Button(tab2,padx=31,bd=2,fg="black",font=('arial',10,'bold'),text="K-Lite Codecs",command=self.btn41Click)
         btn40.place(x=230, y=170)

         btn41=Button(tab2,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="GOM",command=self.btn42Click)
         btn41.place(x=230,y=210)

         btn42=Button(tab2,padx=52,bd=2,fg="black",font=('arial',10,'bold'),text="Spotify",command=self.btn43Click)
         btn42.place(x=230,y=250)
         
         btn43=Button(tab2,padx=54,bd=2,fg="black",font=('arial',10,'bold'),text="Java 8",command=self.btn44Click)
         btn43.place(x=230,y=290)

         btn44=Button(tab2,padx=39,bd=2,fg="black",font=('arial',10,'bold'),text="NotePad++",command=self.btn45Click)
         btn44.place(x=230, y=330)

         btn45=Button(tab2,padx=48,bd=2,fg="black",font=('arial',10,'bold'),text="WinSCP",command=self.btn46Click)
         btn45.place(x=230, y=370)

         btn46=Button(tab2,padx=58,bd=2,fg="black",font=('arial',10,'bold'),text="Putty",command=self.btn47Click)
         btn46.place(x=230, y=410)

         btn47=Button(tab2,padx=49,bd=2,fg="black",font=('arial',10,'bold'),text="FileZilla",command=self.btn48Click)
         btn47.place(x=230,y=450)
    """
   


if __name__ == '__main__':
    root = Tk()
    #Title of Window Frame.
    root.title("RusBase 0.0.6")
    #Size of Window Frame.
    root.geometry("400x650+0+0")
    #Sets icon for Window Frame.
    root.iconbitmap(r'files\icon.ico')
    #Attach tabs to Window Frame.
    note = ttk.Notebook(root)
    #Fixed size of frame
    root.resizable(width=False, height=False)
    app = Application(root)
    root.mainloop()
