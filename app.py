from asyncio import Future
from tkinter import *
import asyncio
from PIL import ImageTk, Image
import cv2
from pynput.keyboard import Key, Controller

class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()

class WD_Images(Tk):
    def __init__(self, root):
        self.root = root

        self.manual = ImageTk.PhotoImage(Image.open("img/manual.png").resize((222, 46)))
        self.scenary = ImageTk.PhotoImage(Image.open("img/scenary.png").resize((222, 46)))

        self.door = ImageTk.PhotoImage(Image.open("img/door.png").resize((30, 30)))
        self.door_active = ImageTk.PhotoImage(Image.open("img/door-active.png").resize((30, 30)))

        self.cam = ImageTk.PhotoImage(Image.open("img/cam.png").resize((30, 30)))
        self.cam_active = ImageTk.PhotoImage(Image.open("img/cam-active.png").resize((30, 30)))

class WD_Button(Tk):
    def __init__(self, root):
        self.root = root

    def btn(self, img, command):
        return Button(self.root, text="", image=img, borderwidth=0, activebackground='#ffffff', background='#ffffff',
               relief=SUNKEN, command=command)

class Window(Tk):

    def __init__(self, loop):
        self.keyboard = Controller()
        self.loop = loop
        self.name = 'frame'
        self.status = False
        self.root = Tk()
        self.root.geometry("1020x600")
        self.root.config(background='#ffffff')

        self.app_backround = ImageTk.PhotoImage(Image.open("img/back.png").resize((1024, 600)))
        self.label1 = Label(self.root, image=self.app_backround, background='#ffffff')
        self.label1.place(x=0, y=0)

        self.img_father = WD_Images(self.root)
        self.btn_father = WD_Button(self.root)

        self.btnManual = self.btn_father.btn(self.img_father.manual, lambda: self.loop.create_task(self.new()))

        self.btnDoor1 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(0)))
        self.btnDoor2 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(1)))
        self.btnDoor3 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(2)))
        self.btnDoor4 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(3)))
        self.btnDoor5 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(4)))
        self.btnDoor6 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(5)))

        self.btnCam1 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(0, self.btnCam1)))
        self.btnCam2 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(1, self.btnCam2)))
        self.btnCam3 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(2, self.btnCam3)))
        self.btnCam4 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(3, self.btnCam4)))
        self.btnCam5 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(4, self.btnCam5)))
        self.btnCam6 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(5, self.btnCam6)))

        self.btnManual.place(x=20, y=20)

        self.btnDoor1.place(x=330, y=238)#floor 3 l
        self.btnDoor2.place(x=750, y=238)#floor 3 r
        self.btnDoor3.place(x=330, y=380)#floor 2 l
        self.btnDoor4.place(x=750, y=380)#floor 2 r
        self.btnDoor5.place(x=330, y=535)#floor 1 l
        self.btnDoor6.place(x=750, y=535)#floor 1 r

        self.btnCam1.place(x=90, y=120)
        self.btnCam2.place(x=130, y=120)
        self.btnCam3.place(x=170, y=120)
        self.btnCam4.place(x=210, y=120)
        self.btnCam5.place(x=250, y=120)
        self.btnCam6.place(x=290, y=120)

        self.cams = [self.btnCam1, self.btnCam2]
        self.doors = [self.btnDoor1, self.btnDoor2, self.btnDoor3, self.btnDoor4, self.btnDoor5, self.btnDoor6]

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

    def switchCam(self, camInstance):
        for camVal in self.cams:
            camVal.config(image=self.img_father.cam)
        self.change_img(camInstance, self.img_father.cam, self.img_father.cam_active)

    async def camEnable(self, camName, cam):
        self.switchCam(cam)
        vid = cv2.VideoCapture(camName, cv2.CAP_DSHOW)
        self.status = not self.status
        try:
            if self.status != False:
                while (True):
                    if self.status == False:
                        break
                    ret, frame = vid.read()
                    cv2.namedWindow(self.name, cv2.WND_PROP_FULLSCREEN)
                    cv2.moveWindow(self.name, 1920, 0)
                    cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow(self.name, frame)
                    await asyncio.sleep(0.01)
            else:
                while (True):
                    if self.status == True:
                        break
                    ret, frame = vid.read()
                    cv2.namedWindow(self.name, cv2.WND_PROP_FULLSCREEN)
                    cv2.moveWindow(self.name, 1920, 0)
                    cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow(self.name, frame)
                    await asyncio.sleep(0.01)
        except:
            await self.camEnable(camName, cam)

    async def new(self):
        self.scenary = Toplevel()
        self.scenary.geometry("1020x600")
        self.scenary.attributes("-fullscreen", True)
        self.scenary.config(background='#ffffff')

        self.btn_father_sc = WD_Button(self.scenary)

        self.btnScenary = self.btn_father_sc.btn(self.img_father.scenary, lambda: self.loop.create_task(self.scenary_close()))
        self.btnScenary.place(x=20, y=20)

    async def scenary_close(self):
        self.scenary.destroy()

    async def door(self, doorIndx):
        self.doors[doorIndx] = self.change_img(self.doors[doorIndx], self.img_father.door, self.img_father.door_active)
        print('door' + str(doorIndx))

    def switch_light(self, lampIndx):
        pass #switch light

    def switch_door(self, doorIndx):
        pass #switch door

def main():
    asyncio.run(App().exec())

if __name__ == '__main__':
    main()