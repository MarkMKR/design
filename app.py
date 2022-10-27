from tkinter import *
import asyncio
from PIL import ImageTk, Image


class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()


class Window(Tk):
    def __init__(self, loop):
        self.loop = loop
        self.root = Tk()
        self.root.geometry("1020x600")

        self.app_backround = ImageTk.PhotoImage(Image.open("back.png").resize((1024, 600)))
        self.door = ImageTk.PhotoImage(Image.open("img/door.png").resize((60, 60)))
        self.door_active = ImageTk.PhotoImage(Image.open("img/door-active.png").resize((60, 60)))

        label1 = Label(self.root, image=self.app_backround)
        label1.place(x=0, y=0)

        self.btnDoor1 = Button(self.root, text="", image=self.door, borderwidth=0, activebackground='#ffffff', background='#ffffff',
                          relief=SUNKEN, command=lambda: self.loop.create_task(self.cam()))
        self.btnDoor1.place(x=90, y=120)

    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(.1)

    def change_img(self, btn, img1, img2):
        if (btn.cget('image') == str(img1)):
            btn.config(image=img2)
        else:
            btn.config(image=img1)
        return btn

    async def door1(self):
        self.btnDoor1 = self.change_img(self.btnDoor1, self.door, self.door_active)

    async def cam(self):
        pass

asyncio.run(App().exec())