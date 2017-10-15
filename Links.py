import subprocess
import urllib
import os

class L:
    def btn1Click(url,file):
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
                btn1=subprocess.check_call([sys.executable,'img.py'],timeout=2)
            except:
                pass
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
        return None
    """
    def btn2Click(btn):

        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkakdSZkRSeXljWEk', 'HDDGuardian.exe')
        pass
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
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
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkVEdWaUVEY09BcFU', 'VictoriaHDD.exe')
        pass
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
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
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        pass
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn5Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        pass
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn6Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkcnZkX3FSMUdCaEk', 'Autoruns.exe')
        pass
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="Autoruns.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn7Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkd3NDU3QxTjhFUFE', 'Ccleaner.exe')
        pass
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="Ccleaner.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn8Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib.request import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkaHVVUlpocVRSakE', 'rkill.exe')
        pass
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="rkill.exe"
        file2="rkill64.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
            os.remove(file2)
    def btn9Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkc2lzZTdFTjNYTVU', 'RogueKiller.exe')
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="RogueKiller.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn10Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkWjcwalRObi1iOU0', 'Malwarebytes.exe')
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="Malwarebytes.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn11Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkM2thTl9GeEJZdTg', 'AdwCleaner.exe')
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="AdwCleaner.exe"
        try:
            btn=subprocess.call([file], shell=True)
        finally:
            os.remove(file)
    def btn12Click(btn):
        try:
            from urllib.request import urlretrieve
        except ImportError:
            from urllib import urlretrieve
        urlretrieve('https://drive.google.com/uc?export=download&id=0B06Qp2heoHZkbmdqMWsyaHludnM', 'Revo.exe')
        for x in range(0,1):
            try:
                btn1=subprocess.check_call([sys.executable,'Loading-img.py'],timeout=2)
            except:
                pass
        file="Revo.exe"
        try:
            btn=subprocess.call([file], shell=True)
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
    """
