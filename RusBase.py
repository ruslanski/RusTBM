from tkinter import *
import random
import time;
import subprocess

root=Tk()
root.geometry("800x600+0+0")
root.title("RusBase PC")

text_Input=StringVar()

Tops=Frame(root, width=800, height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=600, height=700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=200, height=700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

#TIME
localtime=time.asctime(time.localtime(time.time()))

