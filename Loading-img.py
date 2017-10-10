from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

class ImageLabel(tk.Label):
    """Class below displays a gif loading image with transaparent background.
       When end-user click on a button, class ImageLabel displays image for
       three seconds and closes.
    """

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)
window=tk.Tk()
"""
Below code makes background of image transparent.
OS-Dependent,but works in Windows.
User: dln385. https://stackoverflow.com/questions/19080499/
transparent-background-in-a-tkinter-window
"""
window.overrideredirect(True)
window.geometry("+700+350")
window.lift()
window.wm_attributes("-topmost", True)
window.wm_attributes("-disabled", True)
window.wm_attributes("-transparentcolor", "white")
lbl=ImageLabel(window, bg='white')
#Transaparent Background Ends#
lbl.load("files\loading.gif")
lbl.pack(fill=BOTH, expand = True)
window.mainloop()

