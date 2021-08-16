import os
import sys
import glob
import re
import shutil
from tkinter import filedialog
import tkinter
from functools import partial
from tkinter import messagebox
from PIL import Image, ImageTk

global img
global ret
ret = 0
global flag
flag = True

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def modosu():
    if ret == 0:
      if not flag == True:
        messagebox.showerror("エラー","まずはフォルダを選択してください")
      return 0
    oyapath = ret
    kopaths = []
    kopaths.append(oyapath + "/omote")
    kopaths.append(oyapath + "/ura")
    kopaths.append(oyapath + "/yamaneko")

    for ko in kopaths:
        files = glob.glob(ko + "/*")
        for f in files:
            print(f)
            shutil.move(f, oyapath)

    for ko in kopaths:
      files = os.listdir(ko)
      if files:
        print(ko + "__の中にファイルがあるので、削除しせんでした。")
        print(files)
      else:
        print(ko + "__は空なので、削除します。")
        shutil.rmtree(ko)
      


def furiwake():
    if ret == 0:
      if not flag == True:
        messagebox.showerror("エラー","まずはフォルダを選択してください")
      return 0
    dirpath = ret
    print(dirpath)
    os.makedirs(dirpath + "/omote", exist_ok=True)
    os.makedirs(dirpath + "/ura", exist_ok=True)
    os.makedirs(dirpath + "/yamaneko", exist_ok=True)

    if not os.path.isdir(dirpath):
        print("フォルダが存在しません。作業をやめます。")
        sys.exit()

    files = os.listdir(dirpath)
    files_file = [f for f in files if os.path.isfile(os.path.join(dirpath, f))]
    files_file.sort()

    for f in files_file:
        f = dirpath + "/" + f
        print(f)
        num = re.findall(r"\d+", f)
        if len(num) == 0:
            shutil.move(f, dirpath + "/yamaneko")
        elif int(num[-1]) % 2 == 1:
            shutil.move(f, dirpath + "/omote")
        else:
            shutil.move(f, dirpath + "/ura")




class Application(tkinter.Frame):
    global ret
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('ウラオモテヤマネコ')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        global img
        # pyinstallerの時には、specに以下の行を追加
        # a.datas += [("top.png" , "./appfigs/top.png" , "DATA")]
        img = Image.open(resource_path('top.png'))
        img = ImageTk.PhotoImage(img)
 
        self.canvas = tkinter.Canvas(bg="white", width=300, height=300)
        self.canvas.pack(anchor=tkinter.NW)
        self.canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

        self.dialog_button = tkinter.Button(self, text='画像が入っているフォルダを選択...', command=file_open, width=30,height=3)
        self.dialog_button.pack(anchor=tkinter.NW)

        self.text_1 = tkinter.StringVar()
        self.type_label = tkinter.Label(self, textvariable=self.text_1 , height= 4 ,wraplength=300)
        self.type_label.pack(anchor=tkinter.W)
        self.text_2 = tkinter.StringVar()
        self.content_label = tkinter.Label(self, textvariable=self.text_2)
        self.content_label.pack(anchor=tkinter.W)

        self.furiwake_button = tkinter.Button(self, text='フォルダ内の画像を分ける', command=furiwake, width=30,height=3).pack(anchor=tkinter.NW)
        self.modosu_button = tkinter.Button(self, text='振り分けた画像を戻す', command=modosu, width=30,height=3).pack(anchor=tkinter.NW)
        global flag
        flag = False
def file_open():
    global ret
    global flag
    ini_dir = './'
    ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='画像の入ったフォルダを選択してください', mustexist = True)

    if not len(ret) == 0:    
      app.text_1.set("フォルダ名:" + str(ret))
      app.text_2.set("処理の種類を選択してニャ")

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()

