import tkinter as tk
from tkSimpleStatusbar import *

master = tk.Tk()
master.geometry('326x65')
master.title("Membuat Status Bar")

status = StatusBar(master)
status.pack(side=BOTTOM, fill=X)
status.set("selamat datang...")
def new():
    status.set("sedeng new")
def detect():
    status.set("sedang detect")
def training():
    status.set("sedang training")
def openfile():
    status.set("sedang buka file")



img_detect = PhotoImage(file="img/face_detec.png").subsample(15,15)
img_new = PhotoImage(file="img/add_data.png").subsample(15,15)
img_train = PhotoImage(file="img/training.png").subsample(15,15)
img_openfile = PhotoImage(file="img/files.png").subsample(15,15)

btn_detect = Button(master,image = img_detect,compound=LEFT,command=new, text="Detect").pack(side=LEFT)
btn_new = Button(master,image=img_new,compound=LEFT,command=detect,text="New").pack(side=LEFT)
btn_train = Button(master,image=img_train,compound=LEFT,command=training,text="Training").pack(side=LEFT)
btn_openfile = Button(master,image=img_openfile,compound=LEFT,command=openfile,text="Open file").pack(side=LEFT)

master.mainloop()