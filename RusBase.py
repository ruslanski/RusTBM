#!usr/bin/env python3
#RusBase PC
#Version 0.0.4
#Author: Ruslan Shakirov
#https://github.com/ruslanski/RusBase
#Start Date: 08/21/2017

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random
import time
import subprocess
import urllib
import os


class Application(Frame):
    """GUI application with twelve buttons"""

    def __init__(self,master):
        self.master = master
        self.logo()
        self.menu_bar()
        self.tab_buttons()

    def logo(self):
        #Set frame size and style for Top Logo 
        Tops=Frame(root)
        Tops.pack(side=TOP)
        #Set frame size and style for Bottom Logo
        Bots=Frame(root)
        Bots.pack(side=BOTTOM)
        #Set attributes of Top Logo
        lblInfo=Label(Tops, font=('arial',20,'bold'), text="RusBase PC",fg="Steel Blue",anchor="w")
        #Place Top Logo
        lblInfo.grid(row=1, column=0)
        #Set attributes of Bottom Logo
        blInfo=Label(Bots,text="By Ruslan Shakirov. rshak02@gmail.com")
        #Place Bottom Logo
        blInfo.grid(row=15,column=0)

        localtime=time.asctime(time.localtime(time.time()))

        #Set attributes of Time 
        lblInfo=Label(Tops, font=('arial',8,'bold'), text=localtime,anchor="w")
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

         btn2=Button(tab1,padx=32,bd=2,fg="black",font=('arial',10,'bold'),text="HDD Guardian",command=self.btn2Click)
         btn2.place(x=8,y=50)

         btn3=Button(tab1,padx=37,bd=2,fg="black",font=('arial',10,'bold'),text="Victoria HDD",command=self.btn3Click)
         btn3.place(x=8, y=90)

         btn4=Button(tab1,padx=49,bd=2,fg="black",font=('arial',10,'bold'),text="Autoruns",command=self.btn4Click)
         btn4.place(x=8, y=130)

         btn5=Button(tab1,padx=46,bd=2,fg="black",font=('arial',10,'bold'),text="MSConfig",command=self.btn5Click)
         btn5.place(x=8, y=170)

         btn6=Button(tab1,padx=18,bd=2,fg="black",font=('arial',10,'bold'),text="Check LAN+WLAN",command=self.btn6Click)
         btn6.place(x=8,y=210)

         btn7=Button(tab1,padx=47,bd=2,fg="black",font=('arial',10,'bold'),text="CCleaner",command=self.btn7Click)
         btn7.place(x=8,y=250)
         
         btn8=Button(tab1,padx=62,bd=2,fg="black",font=('arial',10,'bold'),text="RKill",command=self.btn8Click)
         btn8.place(x=8,y=290)

         btn9=Button(tab1,padx=39,bd=2,fg="black",font=('arial',10,'bold'),text="RogueKiller",command=self.btn9Click)
         btn9.place(x=8, y=330)

         btn10=Button(tab1,padx=33,bd=2,fg="black",font=('arial',10,'bold'),text="Malwarebytes",command=self.btn10Click)
         btn10.place(x=8, y=370)

         btn11=Button(tab1,padx=36,bd=2,fg="black",font=('arial',10,'bold'),text="Adw Cleaner",command=self.btn11Click)
         btn11.place(x=8, y=410)

         btn12=Button(tab1,padx=61,bd=2,fg="black",font=('arial',10,'bold'),text="Revo",command=self.btn12Click)
         btn12.place(x=8,y=450)
         
         #Place buttons in second column of tab1.
         
         btn13=Button(tab1,padx=41,bd=2,fg="black",font=('arial',10,'bold'),text="WinDirStat",command=self.btn13Click)
         btn13.place(x=230,y=10)

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
    
    def btn1Click(btn):
        """Function downloads a file from link, launches file and deletes after closing."""
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUm5JdXRic1FMN00', 'CrystalDisk.exe')
        file=("CrystalDisk.exe")
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)

    def btn2Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkakdSZkRSeXljWEk', 'HDDGuardian.exe')
        file="HDDGuardian.exe"
        
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
            
    def btn3Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkVEdWaUVEY09BcFU', 'VictoriaHDD.exe')
        file="VictoriaHDD.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
        
    def btn4Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn5Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn6Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn7Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkd3NDU3QxTjhFUFE', 'Ccleaner.exe')
        file="Ccleaner.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn8Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib.request import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkaHVVUlpocVRSakE', 'rkill.exe')
        file="rkill.exe"
        file2="rkill64.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
            os.remove(file2)
    def btn9Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkc2lzZTdFTjNYTVU', 'RogueKiller.exe')
        file="RogueKiller.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn10Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkWjcwalRObi1iOU0', 'Malwarebytes.exe')
        file="Malwarebytes.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn11Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkM2thTl9GeEJZdTg', 'AdwCleaner.exe')
        file="AdwCleaner.exe"
        
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn12Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkbmdqMWsyaHludnM', 'Revo.exe')
        file="Revo.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn13Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkaEEtTGNJeU1Ldnc', 'Windirstat.exe')
        file="Windirstat.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn14Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkeEVrcUFscWEyUlk', 'ConsolePortable.exe')
        file="ConsolePortable.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn15Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkN3A0OTY0MEV1dnM', 'ProcessExplorer.exe')
        file="ProcessExplorer.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn16Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkQWtveVZBWlhLUHc', 'WinAudit.exe')
        file="WinAudit.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn17Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkeGVBcXpHSXkxWjA', 'PatchMyPC.exe')
        file="PatchMyPC.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn18Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkaEJsdlBpci1rRHM', 'SystemRestoreManager.exe')
        file="SystemRestoreManager.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn19Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkQktwNW5tWlBuWUE', 'GPUShark.exe')
        file="GPUShark.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn20Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkUGFzZG5nQUZTeDA', 'GeekUninstaller.exe')
        file="GeekUninstaller.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn21Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn22Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Recuva.exe')
        file="Recuva.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn23Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com /uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'CompleteWinRepair.exe')
        file="CompleteWinRepair.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn24Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'WinSystemControl.exe')
        file="WinSystemControl.exe"
        
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
    def btn25Click(btn):
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
            for x in range(0,1):
                try:
                    btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=8)
                except:
                    pass
        finally:
            os.remove(file)
            
    #Tab2
    def btn26Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn27Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn28Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)

    def btn29Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn30Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn31Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn32Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn33Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn34Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn35Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn36Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn37Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn38Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn39Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn40Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn41Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        img=ImageLabel()
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn42Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn43Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn44Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn45Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn46Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn47Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn48Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)


    #Size of Window Frame and its Title.
root = Tk()
root.title("RusBase PC 0.0.4")
root.geometry("400x600+0+0")
note = ttk.Notebook(root)

app = Application(root)
root.mainloop()
if __name__ == '__main__':
    main()
