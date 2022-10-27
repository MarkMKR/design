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
        self.name = 'frame'
        self.status = False
        self.root = Tk()
        self.root.geometry("1020x600")

        self.app_backround = ImageTk.PhotoImage(Image.open("img/img.png").resize((1024, 600)))
        self.door = ImageTk.PhotoImage(Image.open("img/door.png").resize((30, 30)))
        self.door_active = ImageTk.PhotoImage(Image.open("img/door-active.png").resize((30, 30)))

        self.cam = ImageTk.PhotoImage(Image.open("img/lock.png").resize((30, 30)))
        self.cam_active = ImageTk.PhotoImage(Image.open("img/lock-active.png").resize((30, 30)))

        label1 = Label(self.root, image=self.app_backround)
        label1.place(x=0, y=0)

        self.btnCam1 = Button(self.root, text="", image=self.door, borderwidth=0, activebackground='#ffffff', background='#ffffff',
                          relief=SUNKEN, command=lambda: self.loop.create_task(self.camEnable(0, self.btnCam1)))
        self.btnCam1.place(x=90, y=120)
        self.btnCam2 = Button(self.root, text="", image=self.door, borderwidth=0, activebackground='#ffffff', background='#ffffff',
                          relief=SUNKEN, command=lambda: self.loop.create_task(self.camEnable(2, self.btnCam2)))
        self.btnCam2.place(x=160, y=120)
        self.cams = [self.btnCam1, self.btnCam2]
    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(.1)

    def disable_img(self, btn, img1, img2):
        btn.config(image=img1)

    def change_img(self, btn, img1, img2):
        if (btn.cget('image') == str(img1)):
            btn.config(image=img2)
        else:
            btn.config(image=img1)
        return btn

    async def door1(self):
        self.btnDoor1 = self.change_img(self.btnDoor1, self.door, self.door_active)

    def switchCam(self, camName, camInstance):
        for camVal in self.cams:
            self.disable_img(camVal, self.cam, self.cam_active)
        self.change_img(camInstance, self.cam, self.cam_active)
    async def camEnable(self, camName, cam):
        self.switchCam(camName, cam)
        vid = cv2.VideoCapture(camName)
        self.status = not self.status
        if self.status != False:
            while (True):
                if self.status == False:
                    break
                ret, frame = vid.read()
                cv2.namedWindow(self.name, cv2.WND_PROP_FULLSCREEN)
                cv2.moveWindow(self.name, 1920, 0)
                cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow(self.name, frame)

                cv2.waitKey(1)
                await asyncio.sleep(.1)
        else:
            while (True):
                if self.status == True:
                    break
                ret, frame = vid.read()
                cv2.namedWindow(self.name, cv2.WND_PROP_FULLSCREEN)
                cv2.moveWindow(self.name, 1920, 0)
                cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow(self.name, frame)
                cv2.waitKey(1)
                await asyncio.sleep(.1)

asyncio.run(App().exec())