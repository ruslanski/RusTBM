from tkinter import *
import tkinter as tk
from tkinter import ttk
import time


"""https://stackoverflow.com/questions/38883022/python-progress-bar-gui"""

class progress_bar(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(fill=BOTH,expand=1)
        self.val = 0
        self.maxval = 1
        self.progress["maximum"] = 1

    def updating(self, val):
        self.val = val
        self.progress["value"] = self.val
        app.title("Loading "+str(int(self.val*100))+"%")
        if self.val == self.maxval:
            self.destroy()

def test(i=0):
    app.updating(i/50)
    if i < 100:
        app.after(50, test, i+1)

app = progress_bar()
app.after(1, test)
app.geometry("250x20+650+350")
app.mainloop()
"""
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import time

MAX = 30

root = Tk()
root.geometry('{}x{}'.format(400, 100))
progress_var = DoubleVar() #here you have ints but when calc. %'s usually floats
theLabel = Label(root, text="Sample text to show")
theLabel.pack()
progressbar = ttk.Progressbar(root, variable=progress_var, maximum=MAX)
progressbar.pack(fill=X, expand=1)


def loop_function():

    k = 0
    while k <= MAX:
    ### some work to be done
        progress_var.set(k)
        k += 1
        time.sleep(0.02)
        root.update_idletasks()
    root.after(100, loop_function)


root.mainloop()


import sys
from tkinter import *
from tkinter import ttk
mGui = Tk()

mGui.geometry('450x450')
mGui.title('Hanix Downloader')

mpb = ttk.Progressbar(mGui,orient ="horizontal",length = 200, mode ="determinate")
mpb.pack()
mpb["maximum"] = 100
mpb["value"] = 50

mGui.mainloop()
"""
