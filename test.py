from tkinter import *
import time
root = Tk()
clock = Label(root, font=('times', 20, 'bold'))
clock.pack(fill=BOTH, expand=1)
def tick():
# get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
# if time string has changed, update it
    clock.config(text=time2)
# calls itself every 200 milliseconds
# to update the time display as needed
# could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
root.mainloop( )
