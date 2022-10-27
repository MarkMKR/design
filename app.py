from tkinter import *
import asyncio
from PIL import ImageTk, Image
import cv2

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
                          relief=SUNKEN, command=lambda: await self.cam())
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
        self.btnDoor1 = self.change_img(self.btnDoor1, self.door, self.door_active)
        print('d');
        vid = cv2.VideoCapture(0)
        while (True):
            # Capture the video frame
            # by frame
            ret, frame = vid.read()

            # Display the resulting frame
            name = 'frame'
            cv2.namedWindow(name, cv2.WND_PROP_FULLSCREEN)
            cv2.moveWindow(name, 1920, 0)
            cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow(name, frame)
            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            cv2.waitKey(1)

asyncio.run(App().exec())