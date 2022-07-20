# my ass is very big.
import subprocess
import io
import os
import time
import re
import uuid
import sys

try:
    import requests
    print('ok')
except Exception as e:
    print(f'EXCEPTION: {e}')
    print('now installing requests')
    acmd = 'pip3 install requests'
    res = subprocess.getoutput(acmd)
    time.sleep(1)
    import requests

try:
    from tkinter import *
    print('okkkkkkkkkkkk')
except Exception as e:
    print(f'EXCEPTION: {e}')
    print('now installing tkinter')
    acmd = 'pip3 install tkinter'
    res = subprocess.getoutput(acmd)
    time.sleep(1)
    from tkinter import *

# создание окна
root = Tk()
root.geometry('500x300')
root.title('youtube downloader')
Label(root, text = "downloader YT", font = 'arial 20 bold').pack()

# поле для ссылки
link = StringVar()
Label(root, text = 'please here:', font = 'arial 15 bold').place(x = 160, y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)


def download_url():

    opendir()
    try:
        import yt_dlp
        print('ok')
    except Exception as e:
        print(f'EXCEPTION: {e}')
        print('now installing')
        acmd = 'pip3 install yt_dlp'
        res = subprocess.getoutput(acmd)
        time.sleep(1)
        import yt_dlp


    url = str(link.get())
    Label(root, text = 'Downloaded', font = 'arial 15').place(x = 180, y = 210)


    ydl_opts = {
        'ignoreerrors': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
        print(error_code)

    filename = ''
    return filename
    

def opendir():
    filename = os.path.basename(__file__)
    currdir = os.path.abspath(__file__).replace(filename, '')
    if sys.platform.startswith('win'):
        filename = os.path.basename(__file__)
        currdir = os.path.abspath(__file__).replace(filename, '')
        norm_path = os.path.normpath(currdir)
        os.system('start "" "' + norm_path + '"')

    else:
        os.system('xdg-open "%s"' % currdir)
    return 

Button(root, text = 'Download', font = 'arial 15 bold', bg = 'pale violet red', padx = 2,command = download_url).place(x = 80, y = 150)
Button(root, text = 'Open dir', font = 'arial 15 bold', bg = 'pale violet red', padx = 2,command = opendir).place(x = 290, y = 150)
root.mainloop()
