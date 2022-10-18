from tkinter import *
from PIL import ImageTk, Image
import os

def change_img(btn, img1, img2):
    if(btn.cget('image') == str(img1)):
        btn.config(image=img2)
    else:
        btn.config(image=img1)
    return btn

def disable_img(btn, img1, img2):
    btn.config(image=img1)

def door1():
    global btnDoor1
    btnDoor1 = change_img(btnDoor1, door, door_active)


root = Tk()

root.geometry("1020x600")

app_backround = ImageTk.PhotoImage(Image.open("img/back.png").resize((1024, 600)))
door = ImageTk.PhotoImage(Image.open("img/door.png").resize((60, 60)))
door_active = ImageTk.PhotoImage(Image.open("img/door-active.png").resize((60, 60)))
cam = ImageTk.PhotoImage(Image.open("img/lock.png").resize((60, 60)))
cam_active = ImageTk.PhotoImage(Image.open("img/lock-active.png").resize((60, 60)))

label1 = Label(root, image=app_backround)
label1.place(x=0, y=0)

btnDoor1 = Button(root, text="", image=door, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=door1)
btnDoor1.place(x=90, y=120)

btnCam1 = Button(root, text="", image=cam, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=lambda: switchCam('cam1', btnCam1))
btnCam1.place(x=160, y=520)
btnCam2 = Button(root, text="", image=cam, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=lambda: switchCam('cam2', btnCam2))
btnCam2.place(x=230, y=520)
btnCam3 = Button(root, text="", image=cam, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=lambda: switchCam('cam3', btnCam3))
btnCam3.place(x=300, y=520)
btnCam4 = Button(root, text="", image=cam, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=lambda: switchCam('cam4', btnCam4))
btnCam4.place(x=370, y=520)
btnCam5 = Button(root, text="", image=cam, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=lambda: switchCam('cam5', btnCam5))
btnCam5.place(x=440, y=520)
btnCam6 = Button(root, text="", image=cam, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=lambda: switchCam('cam6', btnCam6))
btnCam6.place(x=510, y=520)

cams = [btnCam1, btnCam2, btnCam3, btnCam4, btnCam5, btnCam6]

def switchCam(camName, camInstance):
    for camVal in cams:
        camVal = disable_img(camVal, cam, cam_active)
    camInstance = change_img(camInstance, cam, cam_active)

root.mainloop()