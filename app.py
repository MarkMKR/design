import os
import time
from asyncio import Future
from tkinter import *
import asyncio
from PIL import ImageTk, Image
import cv2
from pynput.keyboard import Key, Controller
import serial
import pyautogui

class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()

class WD_Images(Tk):
    def __init__(self, root):
        self.root = root

        self.manual = ImageTk.PhotoImage(Image.open("img/manual.png").resize((222, 46)))
        self.scenary = ImageTk.PhotoImage(Image.open("img/scenary.png").resize((222, 46)))

        self.door = ImageTk.PhotoImage(Image.open("img/door.png").resize((50, 50)))
        self.door_active = ImageTk.PhotoImage(Image.open("img/door-active.png").resize((50, 50)))

        self.cam = ImageTk.PhotoImage(Image.open("img/cam.png").resize((50, 50)))
        self.cam_active = ImageTk.PhotoImage(Image.open("img/cam-active.png").resize((50, 50)))

        self.led = ImageTk.PhotoImage(Image.open("img/led.png").resize((50, 50)))
        self.led_active = ImageTk.PhotoImage(Image.open("img/led-active.png").resize((50, 50)))

        self.light = ImageTk.PhotoImage(Image.open("img/light.png").resize((50, 50)))
        self.light_active = ImageTk.PhotoImage(Image.open("img/light-active.png").resize((50, 50)))

        self.smoke = ImageTk.PhotoImage(Image.open("img/smoke.png").resize((50, 50)))
        self.smoke_active = ImageTk.PhotoImage(Image.open("img/smoke-active.png").resize((50, 50)))

        self.fire = ImageTk.PhotoImage(Image.open("img/fire.png").resize((50, 50)))
        self.fire_active = ImageTk.PhotoImage(Image.open("img/fire-active.png").resize((50, 50)))

        self.alarm = ImageTk.PhotoImage(Image.open("img/alarm.png").resize((50, 50)))
        self.alarm_active = ImageTk.PhotoImage(Image.open("img/alarm-active.png").resize((50, 50)))

        self.hair_dryer = ImageTk.PhotoImage(Image.open("img/hair-dryer.png").resize((50, 50)))
        self.hair_dryer_active = ImageTk.PhotoImage(Image.open("img/hair-dryer-active.png").resize((50, 50)))

        self.hair_dryer = ImageTk.PhotoImage(Image.open("img/hair-dryer.png").resize((50, 50)))
        self.hair_dryer_active = ImageTk.PhotoImage(Image.open("img/hair-dryer-active.png").resize((50, 50)))

        self.panel = ImageTk.PhotoImage(Image.open("img/panel.png").resize((50, 50)))
        self.panel_active = ImageTk.PhotoImage(Image.open("img/panel-active.png").resize((50, 50)))

        self.tree = ImageTk.PhotoImage(Image.open("img/tree.png").resize((50, 50)))
        self.tree_active = ImageTk.PhotoImage(Image.open("img/tree-active.png").resize((50, 50)))

        self.fireplace = ImageTk.PhotoImage(Image.open("img/fireplace.png").resize((50, 50)))
        self.fireplace_active = ImageTk.PhotoImage(Image.open("img/fireplace-active.png").resize((50, 50)))

        self.volumeUp = ImageTk.PhotoImage(Image.open("img/sound-increase.png").resize((50, 50)))
        self.volumeDown = ImageTk.PhotoImage(Image.open("img/sound-decrease.png").resize((50, 50)))

class WD_Button(Tk):
    def __init__(self, root):
        self.root = root

    def btn(self, img, command):
        btn = Button(self.root, text="", image=img, borderwidth=0, activebackground='#ffffff', background='#ffffff',
               relief=SUNKEN, command=command)
        btn.status = 0;
        return btn;

class Window(Tk):

    def __init__(self, loop):
        self.volume = 50;
        self.keyboard = Controller()
        self.arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=57600)
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

        self.btnDoor5 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(5, self.btnDoor5)))
        self.btnDoor2 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(2, self.btnDoor2)))
        self.btnDoor0 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(0, self.btnDoor0)))
        self.btnDoor4 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(4, self.btnDoor4)))
        self.btnDoor3 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(3, self.btnDoor3)))
        self.btnDoor1 = self.btn_father.btn(self.img_father.door, lambda: self.loop.create_task( self.door(1, self.btnDoor1)))

        self.btnLed0 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(21, self.btnLed0)))
        self.btnLed1 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(9, self.btnLed1)))
        self.btnLed2 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(1, self.btnLed2)))
        self.btnLed3 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(10, self.btnLed3)))
        self.btnLed4 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(15, self.btnLed4)))
        self.btnLed5 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(14, self.btnLed5)))
        self.btnLed6 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(5, self.btnLed6)))
        self.btnLed7 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(3, self.btnLed7)))
        self.btnLed8 = self.btn_father.btn(self.img_father.led, lambda: self.loop.create_task( self.led(2, self.btnLed8)))

        self.btnLight0 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(12, self.btnLight0)))
        self.btnLight1 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(8, self.btnLight1)))
        self.btnLight2 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(0, self.btnLight2)))
        self.btnLight3 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(44, self.btnLight3)))
        self.btnLight4 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(45, self.btnLight4)))
        self.btnLight5 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(13, self.btnLight5)))
        self.btnLight6 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(4, self.btnLight6)))
        self.btnLight7 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(47, self.btnLight7)))
        self.btnLight8 = self.btn_father.btn(self.img_father.light, lambda: self.loop.create_task( self.light(46, self.btnLight8)))

        self.btnSmoke0 = self.btn_father.btn(self.img_father.smoke, lambda: self.loop.create_task( self.smoke(6, self.btnSmoke0)))
        self.btnSmoke1 = self.btn_father.btn(self.img_father.smoke, lambda: self.loop.create_task( self.smoke(7, self.btnSmoke1)))
        self.btnSmoke2 = self.btn_father.btn(self.img_father.smoke, lambda: self.loop.create_task( self.smoke(8, self.btnSmoke2)))
        self.btnSmoke3 = self.btn_father.btn(self.img_father.smoke, lambda: self.loop.create_task( self.smoke(9, self.btnSmoke3)))
        self.btnSmoke4 = self.btn_father.btn(self.img_father.smoke, lambda: self.loop.create_task( self.smoke(10, self.btnSmoke4)))
        self.btnSmoke5 = self.btn_father.btn(self.img_father.smoke, lambda: self.loop.create_task( self.smoke(11, self.btnSmoke5)))

        self.btnCam1 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(0, self.btnCam1)))
        self.btnCam2 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(1, self.btnCam2)))
        self.btnCam3 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(2, self.btnCam3)))
        self.btnCam4 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(3, self.btnCam4)))
        self.btnCam5 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(4, self.btnCam5)))
        self.btnCam6 = self.btn_father.btn(self.img_father.cam, lambda: self.loop.create_task(self.camEnable(5, self.btnCam6)))

        self.btnFire1 = self.btn_father.btn(self.img_father.fire, lambda: self.loop.create_task(self.fire(16,31, self.btnFire1)))
        self.btnFire2 = self.btn_father.btn(self.img_father.fire, lambda: self.loop.create_task(self.fire(1,1, self.btnFire2)))
        self.btnFire3 = self.btn_father.btn(self.img_father.fire, lambda: self.loop.create_task(self.fire(35,37, self.btnFire3)))
        self.btnFire4 = self.btn_father.btn(self.img_father.fire, lambda: self.loop.create_task(self.fire(3,1, self.btnFire4)))
        self.btnFire6 = self.btn_father.btn(self.img_father.fire, lambda: self.loop.create_task(self.fire(5,1, self.btnFire6)))

        self.btnAlarm1 = self.btn_father.btn(self.img_father.alarm, lambda: self.loop.create_task(self.alarm(26, self.btnAlarm1)))
        self.btnAlarm2 = self.btn_father.btn(self.img_father.alarm, lambda: self.loop.create_task(self.alarm(24, self.btnAlarm2)))
        self.btnAlarm3 = self.btn_father.btn(self.img_father.alarm, lambda: self.loop.create_task(self.alarm(36, self.btnAlarm3)))
        self.btnAlarm4 = self.btn_father.btn(self.img_father.alarm, lambda: self.loop.create_task(self.alarm(29, self.btnAlarm4)))
        self.btnAlarm5 = self.btn_father.btn(self.img_father.alarm, lambda: self.loop.create_task(self.alarm(27, self.btnAlarm5)))
        self.btnAlarm6 = self.btn_father.btn(self.img_father.alarm, lambda: self.loop.create_task(self.alarm(20, self.btnAlarm6)))

        self.btnHair5 = self.btn_father.btn(self.img_father.hair_dryer, lambda: self.loop.create_task(self.hair(34, self.btnHair5)))
        self.btnHair6 = self.btn_father.btn(self.img_father.hair_dryer, lambda: self.loop.create_task(self.hair(33, self.btnHair6)))

        self.btnVolumeUp = self.btn_father.btn(self.img_father.volumeUp, lambda: self.loop.create_task(self.volumeUp()))
        self.btnVolumeDown = self.btn_father.btn(self.img_father.volumeDown, lambda: self.loop.create_task(self.volumeDown()))

        self.btnFirepalce = self.btn_father.btn(self.img_father.fireplace, lambda: self.loop.create_task(self.fireplace(0, self.btnFirepalce)))
        self.btnTree = self.btn_father.btn(self.img_father.tree, lambda: self.loop.create_task(self.tree(0, self.btnTree)))

        self.btnPanel3 = self.btn_father.btn(self.img_father.panel, lambda: self.loop.create_task(self.panel(23, self.btnPanel3)))
        self.btnPanel4 = self.btn_father.btn(self.img_father.panel, lambda: self.loop.create_task(self.panel(23, self.btnPanel4)))
        self.btnPanel5 = self.btn_father.btn(self.img_father.panel, lambda: self.loop.create_task(self.panel(28, self.btnPanel5)))
        self.btnPanel6 = self.btn_father.btn(self.img_father.panel, lambda: self.loop.create_task(self.panel(17, self.btnPanel6)))
        self.btnPanel7 = self.btn_father.btn(self.img_father.panel, lambda: self.loop.create_task(self.panel(0, self.btnPanel7)))


        self.btnManual.place(x=20, y=20)

        self.btnDoor5.place(x=185, y=220)#floor 3 l
        self.btnDoor2.place(x=697, y=220)#floor 3 r
        self.btnDoor0.place(x=185, y=365)#floor 2 l
        self.btnDoor4.place(x=697, y=365)#floor 2 r
        self.btnDoor3.place(x=185, y=520)#floor 1 l
        self.btnDoor1.place(x=697, y=520)#floor 1 r

        self.btnLed0.place(x=240, y=220)#floor 3 l
        self.btnLed1.place(x=750, y=220)#floor 3 l
        self.btnLed2.place(x=240, y=365)#floor 3 l
        self.btnLed5.place(x=750, y=365)#floor 3 l
        self.btnLed6.place(x=240, y=520)#floor 3 l
        self.btnLed8.place(x=750, y=520)#floor 3 l
        self.btnLed8.place(x=750, y=520)#floor 3 l
        self.btnLed3.place(x=470, y=220)#floor 3 l
        self.btnLed4.place(x=470, y=365)#floor 3 l
        self.btnLed7.place(x=470, y=520)#floor 3 l

        self.btnLight0.place(x=295, y=220)#floor 3 l
        self.btnLight1.place(x=805, y=220)#floor 3 l
        self.btnLight2.place(x=295, y=365)#floor 3 l
        self.btnLight5.place(x=805, y=365)#floor 3 l
        self.btnLight6.place(x=295, y=520)#floor 3 l
        self.btnLight8.place(x=805, y=520)#floor 3 l
        self.btnLight8.place(x=805, y=520)#floor 3 l
        self.btnLight3.place(x=470, y=170)#floor 3 l
        self.btnLight4.place(x=470, y=315)#floor 3 l
        self.btnLight7.place(x=470, y=470)#floor 3 l

        self.btnTree.place(x=915, y=365)#floor 3 l
        self.btnFirepalce.place(x=915, y=305)#floor 3 l

        self.btnSmoke0.place(x=350, y=220)#floor 3 l
        self.btnSmoke1.place(x=860, y=220)#floor 3 l
        self.btnSmoke2.place(x=350, y=365)#floor 3 l
        self.btnSmoke3.place(x=860, y=365)#floor 3 l
        self.btnSmoke4.place(x=350, y=520)#floor 3 l
        self.btnSmoke5.place(x=860, y=520)#floor 3 l

        self.btnCam1.place(x=185, y=160)
        self.btnCam2.place(x=697, y=160)
        self.btnCam3.place(x=185, y=305)
        self.btnCam4.place(x=697, y=305)
        self.btnCam5.place(x=185, y=460)
        self.btnCam6.place(x=697, y=460)

        self.btnFire1.place(x=240, y=160)
        self.btnFire2.place(x=750, y=160)
        self.btnFire3.place(x=240, y=460)
        self.btnFire4.place(x=750, y=305)
        self.btnFire6.place(x=750, y=460)

        self.btnAlarm1.place(x=295, y=160)
        self.btnAlarm2.place(x=805, y=160)
        self.btnAlarm3.place(x=295, y=460)
        self.btnAlarm4.place(x=240, y=305)
        self.btnAlarm5.place(x=805, y=305)
        self.btnAlarm6.place(x=805, y=460)

        self.btnHair5.place(x=350, y=160)
        self.btnHair6.place(x=295, y=305)

        self.btnPanel4.place(x=860, y=460)
        self.btnPanel5.place(x=860, y=305)
        self.btnPanel6.place(x=350, y=305)
        self.btnPanel7.place(x=350, y=460)

        self.btnVolumeUp.place(x=30, y=125)
        self.btnVolumeDown.place(x=100, y=125)

        self.cams = [self.btnCam1, self.btnCam2]
    def ledSerial(self,method, param1, param2):
        string = "<LEDWRITE" + "\0" + str(param1) + "\0" + str(param2) + ">"
        self.arduino.write(bytes(string, 'utf-8'))
        time.sleep(.5)
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

    def fireSerial(self, param1, param2):
        string = "<LEDFIREA" + "\0" + str(param1) + "\0" + str(param2) + ">"
        self.arduino.write(bytes(string, 'utf-8'))
        time.sleep(.5)
        data = self.arduino.read_all()
        print(data.decode())

    def servo(self,method, param1):
        string = "<"+ method + "\0" + str(param1)+">"
        self.arduino.write(bytes(string, 'utf-8'))
        time.sleep(.1)
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

    def smokeSerial(self, param1):
        string = "<SMOKE" + "\0" + str(param1)+">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        time.sleep(.1)
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))


    def blink(self,param1, param2, param3):
        string = "<LEDBLINK" + "\0" + str(param1)+ "\0" + str(param2)+ "\0" + str(param3) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        time.sleep(.1)
        data = self.arduino.read_all()
        print(data.decode())

    def blackout(self):
        string = "<BLACKOUT>"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        time.sleep(.1)
        data = self.arduino.read_all()
        print(data.decode())
    def default(self):
        string = "<DEFAULT>"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        time.sleep(.1)
        data = self.arduino.read_all()
        print(data.decode())
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
        try:
            self.switchCam(cam)
            vid = cv2.VideoCapture(camName, cv2.CAP_DSHOW)
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
            self.status = not self.status
            self.loop.create_task(self.camEnable(camName, cam))
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

    async def fireplace(self, index, fpalce):
        self.change_img(fpalce, self.img_father.fireplace, self.img_father.fireplace_active)

    async def tree(self, index, tree):
        self.change_img(tree, self.img_father.tree, self.img_father.tree_active)

    async def door(self, index, door):
        self.change_img(door, self.img_father.door, self.img_father.door_active)
        door.status = not door.status
        comand = 'SERVOOPEN' if door.status == 1 else 'SERVOCLOSE'
        self.servo(comand, index)

    async def led(self, index, led):
        self.change_img(led, self.img_father.led, self.img_father.led_active)
        self.ledSerial("LEDWRITE", index, 255)

    async def light(self, index, light):
        self.change_img(light, self.img_father.light, self.img_father.light_active)
        self.ledSerial("LEDWRITE", index, 0)
    async def smoke(self, index, smoke):
        self.change_img(smoke, self.img_father.smoke, self.img_father.smoke_active)
        self.smokeSerial(index)
        print('smoke' + str(index))

    async def fire(self, index1, index2, fire):
        self.change_img(fire, self.img_father.fire, self.img_father.fire_active)
        self.fireSerial(index1, index2)
        print('fire1' + str(index1)+ ' ===== fire2' + str(index2))

    async def alarm(self, index, alarm):
        self.change_img(alarm, self.img_father.alarm, self.img_father.alarm_active)
        self.blink(index, 100, 300)
        print('alarm' + str(index))

    async def hair(self, index, hair):
        self.change_img(hair, self.img_father.hair_dryer, self.img_father.hair_dryer_active)
        self.blink(index, 100, 300)
        print('hair' + str(index))

    async def panel(self, index, panel):
        self.change_img(panel, self.img_father.panel, self.img_father.panel_active)
        self.blink(index, 100, 300)
        print('panel' + str(index))

    async def volumeDown(self):
        self.volume -= 10
        if self.volume <= 9:
            self.volume = 0;
        os.system(f'amixer set Master {str(self.volume)}%')

    async def volumeUp(self):
        self.volume += 10
        if self.volume >= 91:
            self.volume = 100;
        os.system(f'amixer set Master {str(self.volume)}%')
    def switch_light(self, lampIndx):
        pass #switch light

    def switch_door(self, index):
        pass #switch door

def main():
    asyncio.run(App().exec())

if __name__ == '__main__':
    main()