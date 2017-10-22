from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import subprocess
import urllib
import os

class L:
    
    def btnClick(url,file):
        """This function downloads a software from a link, launches it,
           and deletes after closing.
        #    try:
        #        ld=subprocess.check_call([sys.executable,'img.py'],timeout=2)
        #    except:
        #        pass
        """
        
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve(url,file)
        ld=subprocess.check_call([sys.executable,'bar.py'])
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
