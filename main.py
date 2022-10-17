from tkinter import *
from PIL import ImageTk, Image

def change_img(btn, img1, img2):
    if(btn.cget('image') == str(img1)):
        btn.config(image=img2)
    else:
        btn.config(image=img1)
    return btn
def door1():
    global btnDoor1
    btnDoor1 = change_img(btnDoor1, door, door_active)

root = Tk()

root.geometry("1020x600")

app_backround = ImageTk.PhotoImage(Image.open("img/back.png").resize((1024, 600)))
door = ImageTk.PhotoImage(Image.open("img/door.png").resize((60, 60)))
door_active = ImageTk.PhotoImage(Image.open("img/door-active.png").resize((60, 60)))

label1 = Label(root, image=app_backround)
label1.place(x=0, y=0)

btnDoor1 = Button(root, text="", image=door, borderwidth=0, activebackground='#ffffff', background='#ffffff', relief=SUNKEN, command=door1)
btnDoor1.place(x=90, y=120)

root.mainloop()