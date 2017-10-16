#!usr/bin/env python3
#RusBase
#Version 0.0.7
#Author: Ruslan Shakirov
#https://github.com/ruslanski/RusBase
#Start Date: 08/21/2017

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random
import time
import links

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
        lblInfo=Label(root, font=('arial',24,'bold'), text="Helpdesk Tools",fg="Steel blue",bg="white smoke")
        #Place Top Logo
        lblInfo.pack(fill=BOTH, expand=1)
        #lblInfo.grid(row=1, column=0)
        #Set attributes of Bottom Logo
        blInfo=Label(Bots,text="By Ruslan Shakirov. rshak002@gmail.com")
        blInfo.pack(fill=BOTH, expand=1)
        #Place Bottom Logo
        blInfo.grid(row=15,column=0)
        tblInfo = Label(root, font=('arial', 15, 'bold'),fg="Steel Blue",bg="white smoke",height=1)
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
        #Add 'file' to the menu.
        menu.add_cascade(label='File', menu=file)
        #Add buttons to first bar of the menu.
        file.add_command(label='Save', command='')
        file.add_command(label='Exit', command=root.destroy)

        #Second bar of the menu.
        edit=Menu(menu)
        edit.add_command(label='Undo', command='')
        #Add 'edit' to the menu.
        menu.add_cascade(label='Edit',menu=edit)

        #Third bar of the menu.
        about=Menu(menu)
        menu.add_cascade(label='About',menu=about)

    def tab_buttons(self):
         """This function creates tab1,tab2,tab3 inside main Window Frame.
            With the following attributes in paranthesis.
         """
         tab1 = Frame(note, bg="white smoke")
         tab2 = Frame(note, bg="white smoke")
         tab3 = Frame(note,bg="white smoke")
         tab4 = Frame(note,bg="white smoke")
         tab5 = Frame(note,bg="white smoke")
         tab1.configure(width=800, height=650)
         tab2.configure(width=800, height=650)
         tab3.configure(width=800, height=650)
         tab4.configure(width=800, height=650)
         note.add(tab3, text = " Win Commands ")
         note.add(tab1, text = "  OS Tools  ")
         note.add(tab2, text = " Virus/Malware ")
         note.add(tab4,text=" End-User Software")
         note.add(tab5, text=" Info ")
         note.pack()

         #First Column of tab1.
         #Each button has two variables with a link and a name of software.
         #Gets passed to btn1Click function of file Link.py
         Crystaldisk="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUm5JdXRic1FMN00"
         CrystaldiskFile="CrystalDisk.exe"
         btn1=Button(tab1,padx=41,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Crystal Disk",bg="light cyan",command=lambda: links.L.btnClick(Crystaldisk,CrystaldiskFile))
         btn1.place(x=8,y=10)

         Hddguardian="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkRml4VzVEUjlzWDA"
         HddguardianFile="Hddguardian.exe"
         btn2=Button(tab1,padx=32,bd=2,fg="steel blue",font=('arial',10,'bold'),text="HDD Guardian",bg="light cyan",command=lambda: links.L.btnClick(Hddguardian,HddguardianFile))
         btn2.place(x=8,y=50)

         Victoriahdd="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkZHVmQVJJQ0lCZG8"
         VictoriahddFile="Victoriahdd.exe"
         btn3=Button(tab1,padx=37,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Victoria HDD",bg="light cyan",command=lambda: links.L.btnClick(Victoriahdd,VictoriahddFile))
         btn3.place(x=8, y=90)

         Smartdegraf="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkWHpLdG9OZzE0ZEU"
         SmartdegrafFile="Autoruns.exe"
         btn4=Button(tab1,padx=35,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Smart Degraf",bg="light cyan",command=lambda: links.L.btnClick(Smartdegraf,Smartdegraf))
         btn4.place(x=8, y=130)

         Autoruns="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkWHpLdG9OZzE0ZEU"
         AutorunsFile="Autoruns.exe"
         btn5=Button(tab1,padx=49,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Autoruns",bg="light cyan",command=lambda: links.L.btnClick(Autoruns,AutorunsFile))
         btn5.place(x=8, y=170)

         Siw=""
         SiwFile=""
         btn6=Button(tab1,padx=64,bd=2,fg="steel blue",font=('arial',10,'bold'),text="SIW",bg="light cyan",command=lambda: links.L.btnClick(Siw,SiwFile))
         btn6.place(x=8,y=210)
         
         Ccleaner="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkaENpYnhKQlVSeG8"
         CcleanerFile="Ccleaner"
         btn7=Button(tab1,padx=46,bd=2,fg="steel blue",font=('arial',10,'bold'),text="CCleaner",bg="light cyan",command=lambda: links.L.btnClick(Ccleaner,CcleanerFile))
         btn7.place(x=9,y=250)

         Cpuz="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUm5JdXRic1FMN00"
         CpuzFile="Cpuz.exe"
         btn8=Button(tab1,padx=57,bd=2,fg="steel blue",font=('arial',10,'bold'),text="CPU-Z",bg="light cyan",command=lambda: links.L.btnClick(Cpuz,CpuzFile))
         btn8.place(x=8,y=290)

         Wisedatarecovery="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcW96YXBaRVJpUnc"
         WisedatarecoveryFile="Wisedatarecovery.exe"
         btn9=Button(tab1,padx=13,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Wise Data Recovery",bg="light cyan",command=lambda: links.L.btnClick(Wisedatarecovery,WisedatarecoveryFile))
         btn9.place(x=8, y=330)

         Angryipscanner="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUm5JdXRic1FMN00"
         AngryipscannerFile="Angryipscanner.exe"
         btn10=Button(tab1,padx=21,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Angry IP Scanner",bg="light cyan",command=lambda: links.L.btnClick(Angryipscanner,AngryipscannerFile))
         btn10.place(x=8, y=370)

         Pcdecrapifier="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkQWZIbWwzNVRiWE0"
         PcdecrapifierFile="Pcdecrapifier.exe"
         btn11=Button(tab1,padx=30,bd=2,fg="steel blue",font=('arial',10,'bold'),text="PC Decrapifier",bg="light cyan",command=lambda: links.L.btnClick(Ipdecrapifier,IpdecrapifierFile))
         btn11.place(x=8, y=410)
         
         Restoration="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkZW5yMzJJUERiWDA"
         RestorationFile="Restoration.exe"
         btn12=Button(tab1,padx=40,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Restoration",bg="light cyan",command=lambda: links.L.btnClick(Restoration,RestorationFile))
         btn12.place(x=8,y=450)
         
         #Second Column of tab1.
         Windirstat="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkaEEtTGNJeU1Ldnc"
         WindirstatFile="Windirstat.exe"
         btn13=Button(tab1,padx=41,bd=2,fg="steel blue",font=('arial',10,'bold'),text="WinDirStat",bg="light cyan",command=lambda: links.L.btnClick(Windirstat,WindirstatFile))
         btn13.place(x=230,y=10)
         
         Consoleportable="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkbXBZVVFMMHN6bGs"
         ConsoleportableFile="Consoleportable.exe"
         btn14=Button(tab1,padx=20,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Console Portable",bg="light cyan",command=lambda: links.L.btnClick(Consoleportable,ConsoleportableFile))
         btn14.place(x=230,y=50)

         Processexplorer="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkVXp5YVh5MW03UWM"
         ProcessexloprerFile="Processexplorer.exe"
         btn15=Button(tab1,padx=21,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Process Explorer",bg="light cyan",command=lambda: links.L.btnClick(Processexplorer,ProcessexplorerFile))
         btn15.place(x=230, y=90)

         Winaudit="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkQWtveVZBWlhLUHc"
         WindauditFile="Winaudit.exe"
         btn16=Button(tab1,padx=45,bd=2,fg="steel blue",font=('arial',10,'bold'),text="WinAudit",bg="light cyan",command=lambda: links.L.btnClick(Winaudit,WinauditFile))
         btn16.place(x=230, y=130)

         Patchmypc="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkeGVBcXpHSXkxWjA"
         PatchmypcFile="Patchmypc.exe"
         btn17=Button(tab1,padx=34,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Patch My PC",bg="light cyan",command=lambda: links.L.btnClick(Patchmypc,PatchmypcFile))
         btn17.place(x=230, y=170)

         Sysrestoremanager="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkaEJsdlBpci1rRHM"
         SysrestoremanagerFile="Sysrestoremanager.exe"
         btn18=Button(tab1,padx=7,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Sys Restore Manager",bg="light cyan",command=lambda: links.L.btnClick(Sysrestoremanager,SysrestoremanagerFile))
         btn18.place(x=230,y=210)

         Gpushark="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkQWMyQlNXRmtZNVE"
         GpusharkFile="Gpushark.exe"
         btn19=Button(tab1,padx=40,bd=2,fg="steel blue",font=('arial',10,'bold'),text="GPU Shark",bg="light cyan",command=lambda: links.L.btnClick(Gpushark,GpusharkFile))
         btn19.place(x=230,y=250)

         Geekuninstaller="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUGFzZG5nQUZTeDA"
         GeekuninstallerFile="Geekuninstaller.exe"
         btn20=Button(tab1,padx=24,bd=2,fg="steel blue",font=('arial',10,'bold'),text="GeekUninstaller",bg="light cyan",command=lambda: links.L.btnClick(Geekuninstaller,GeekuninstallerFile))
         btn20.place(x=230,y=290)

         Recuva="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkMmNicC1SMkZsOW8"
         RecuvaFile="Recuva.exe"
         btn21=Button(tab1,padx=51,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Recuva",bg="light cyan",command=lambda: links.L.btnClick(Recuva,RecuvaFile))
         btn21.place(x=230, y=330)

         Winutilities="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUm5JdXRic1FMN00"
         WinutilitiesFile="Winutilities.exe"
         btn22=Button(tab1,padx=25,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Win Utilites Pro",bg="light cyan",command=lambda: links.L.btnClick(Winutilities,WinutilitiesFile))
         btn22.place(x=230, y=370)

         Winprepair="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkSFJnTG1xZGZVNDg"
         WinrepairFile="Winrepair.exe"
         btn23=Button(tab1,padx=5,bd=2,fg="steel blue",font=('arial',10,'bold'),text="Win Repair All-in-One",bg="light cyan",command=lambda: links.L.btnClick(Winrepair,WinrepairFile))
         btn23.place(x=230, y=410)

         Truecrypt="https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkWno1QTBpQzJwbEU"
         TruecryptFile="Truecrypt.exe"
         btn24=Button(tab1,padx=43,bd=2,fg="SkyBlue4",font=('arial',10,'bold'),text="TrueCrypt",bg="light cyan",command=lambda: links.L.btnClick(Truecrypt,TruecryptFile))
         btn24.place(x=230,y=450)

        
         #Place buttons in first column of tab2.
         btn25=Button(tab2,padx=60,bd=2,fg="black",font=('arial',10,'bold'),text="Ninite",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn25.place(x=8,y=10)

         btn26=Button(tab2,padx=28,bd=2,fg="black",font=('arial',10,'bold'),text="Google Chrome",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn26.place(x=8,y=50)

         btn27=Button(tab2,padx=8,bd=2,fg="black",font=('arial',10,'bold'),text="Chrome Cleanup Tool",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn27.place(x=8, y=90)

         btn27=Button(tab2,padx=31,bd=2,fg="black",font=('arial',10,'bold'),text="Mozilla Firefox",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn27.place(x=8, y=130)

         btn28=Button(tab2,padx=58,bd=2,fg="black",font=('arial',10,'bold'),text="Opera",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn28.place(x=8, y=170)

         btn29=Button(tab2,padx=63,bd=2,fg="black",font=('arial',10,'bold'),text="7-Zip",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn29.place(x=8,y=210)

         btn30=Button(tab2,padx=53,bd=2,fg="black",font=('arial',10,'bold'),text="WinRaR",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn30.place(x=8,y=250)
         
         btn31=Button(tab2,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="Skype",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn31.place(x=8,y=290)

         btn32=Button(tab2,padx=40,bd=2,fg="black",font=('arial',10,'bold'),text="Thunderbird",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn32.place(x=8, y=330)

         btn33=Button(tab2,padx=52,bd=2,fg="black",font=('arial',10,'bold'),text="Dropbox",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn33.place(x=8, y=370)

         btn34=Button(tab2,padx=38,bd=2,fg="black",font=('arial',10,'bold'),text="Google Drive",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn34.place(x=8, y=410)

         btn35=Button(tab2,padx=50,bd=2,fg="black",font=('arial',10,'bold'),text="OneDrive",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn35.place(x=8,y=450)
         
         #Place buttons in second column of tab1.
         
         btn36=Button(tab2,padx=53 ,bd=2,fg="black",font=('arial',10,'bold'),text="ITunes",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn36.place(x=230,y=10)

         btn37=Button(tab2,padx=61,bd=2,fg="black",font=('arial',10,'bold'),text="VLC",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn37.place(x=230,y=50)

         btn38=Button(tab2,padx=57,bd=2,fg="black",font=('arial',10,'bold'),text="AIMP",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn38.place(x=230, y=90)

         btn39=Button(tab2,padx=48,bd=2,fg="black",font=('arial',10,'bold'),text="Winamp",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn39.place(x=230, y=130)

         btn40=Button(tab2,padx=31,bd=2,fg="black",font=('arial',10,'bold'),text="K-Lite Codecs",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn40.place(x=230, y=170)

         btn41=Button(tab2,padx=59,bd=2,fg="black",font=('arial',10,'bold'),text="GOM",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn41.place(x=230,y=210)

         btn42=Button(tab2,padx=52,bd=2,fg="black",font=('arial',10,'bold'),text="Spotify",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn42.place(x=230,y=250)
         
         btn43=Button(tab2,padx=54,bd=2,fg="black",font=('arial',10,'bold'),text="Java 8",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn43.place(x=230,y=290)

         btn44=Button(tab2,padx=39,bd=2,fg="black",font=('arial',10,'bold'),text="NotePad++",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn44.place(x=230, y=330)

         btn45=Button(tab2,padx=48,bd=2,fg="black",font=('arial',10,'bold'),text="WinSCP",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn45.place(x=230, y=370)

         btn46=Button(tab2,padx=58,bd=2,fg="black",font=('arial',10,'bold'),text="Putty",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn46.place(x=230, y=410)

         btn47=Button(tab2,padx=49,bd=2,fg="black",font=('arial',10,'bold'),text="FileZilla",bg="light cyan",command=lambda: links.L.btnClick(CrystalDisk,CrystalDiskFile))
         btn47.place(x=230,y=450)

   


if __name__ == '__main__':
    root = Tk()
    #Title of Window Frame.
    root.title("RusBase 0.0.7")
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
