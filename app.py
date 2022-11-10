import os
import time
from asyncio import Future
from tkinter import *
import asyncio
from PIL import ImageTk, Image
from pygame import mixer
import cv2
from pynput.keyboard import Key, Controller
import serial
import pyautogui
from random import randrange
from video_capture import VideoCaptureAsync
mixer.init()

class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()


class WD_Images(Tk):
    def __init__(self, root):
        self.root = root

        self.manual = "img/manual.png"
        self.scenary_btn = "img/scenary.png"

        self.scenary_1 = "img/scenary-1.png"
        self.scenary_active_1 = "img/scenary-active-1.png"

        self.door = "img/door.png"
        self.door_active = "img/door-active.png"

        self.cam = "img/cam.png"
        self.cam_active = "img/cam-active.png"

        self.led = "img/led.png"
        self.led_active = "img/led-active.png"

        self.light = "img/light.png"
        self.light_active = "img/light-active.png"

        self.smoke = "img/smoke.png"
        self.smoke_active = "img/smoke-active.png"

        self.fire = "img/fire.png"
        self.fire_active = "img/fire-active.png"

        self.alarm = "img/alarm.png"
        self.alarm_active = "img/alarm-active.png"

        self.hair_dryer = "img/hair-dryer.png"
        self.hair_dryer_active = "img/hair-dryer-active.png"

        self.panel = "img/panel.png"
        self.panel_active = "img/panel-active.png"

        self.tree = "img/tree.png"
        self.tree_active = "img/tree-active.png"

        self.fireplace = "img/fireplace.png"
        self.fireplace_active = "img/fireplace-active.png"

        self.volumeUp = "img/sound-increase.png"
        self.volumeDown = "img/sound-decrease.png"

        self.kotel = "img/gaz.png"
        self.kotel_active = "img/gaz-active.png"

        self.torch = "img/torch.png"
        self.torch_active = "img/torch-active.png"

        self.vent = "img/vent.png"
        self.vent_active = "img/vent-active.png"

        self.balon = "img/balon.png"
        self.balon_active = "img/balon-active.png"

        self.wilka = "img/wilka.png"
        self.wilka_active = "img/wilka-active.png"
class WD_Button(Tk):
    count = 0
    def __init__(self, root):
        self.root = root


    def btn(self, pasive, active, command, status, x=50, y=50):
        self.active = ImageTk.PhotoImage(Image.open(active).resize((x, y)))
        self.pasive = ImageTk.PhotoImage(Image.open(pasive).resize((x, y)))
        ret = 'pasive'
        if status == 1:
            ret = 'active'
        btn = Button(self.root, text="", image=getattr(self, ret), borderwidth=0, activebackground='#ffffff', background='#ffffff',
                     relief=SUNKEN, command=command)
        btn.status = status
        btn.active = self.active
        btn.pasive = self.pasive
        return btn



class Window(Tk):

    def __init__(self, loop):
        self.alarmStatus = 0
        self.volume = 50;
        self.arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=57600)
        self.keyboard = Controller()
        self.loop = loop
        self.name = 'frame'
        self.status = False
        self.root = Tk()
        self.root.geometry("1020x600")
        self.root.config(background='#ffffff')

        self.app_backround = ImageTk.PhotoImage(Image.open("img/back.png").resize((1024, 585)))
        self.label1 = Label(self.root, image=self.app_backround, background='#ffffff', padx=50, pady=50)
        self.label1.place(x=0, y=0)

        self.img_father = WD_Images(self.root)
        self.btn_father = WD_Button(self.root)

        self.btnManual = self.btn_father.btn(self.img_father.manual, self.img_father.manual,
                                             lambda: self.loop.create_task(self.new()), 0, 222,46)

        self.btnDoor5 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(5, self.btnDoor5)), 0)
        self.btnDoor2 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(2, self.btnDoor2)), 0)
        self.btnDoor0 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(0, self.btnDoor0)), 0)
        self.btnDoor4 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(4, self.btnDoor4)), 0)
        self.btnDoor3 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(3, self.btnDoor3)), 0)
        self.btnDoor1 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(1, self.btnDoor1)), 0)

        self.btnLed0 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(11, self.btnLed0)), 1) #child
        self.btnLed1 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(9, self.btnLed1)), 1)  #sleep
        self.btnLed2 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(1, self.btnLed2)), 1) #batroom
        self.btnLed3 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(10, self.btnLed3)), 1) #middle3
        self.btnLed4 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(15, self.btnLed4)), 1)
        self.btnLed5 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(14, self.btnLed5)), 1)
        self.btnLed6 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(5, self.btnLed6)), 1)  #kitchen
        self.btnLed7 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(3, self.btnLed7)), 1) #middle1
        self.btnLed8 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(self.led(2, self.btnLed8)), 1) #kotel

        self.btnLight0 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(12, self.btnLight0)), 1)
        self.btnLight1 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(8, self.btnLight1)), 1) #sleep
        self.btnLight2 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(0, self.btnLight2)), 1)
        self.btnLight3 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(44, self.btnLight3)), 1)
        self.btnLight4 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(45, self.btnLight4)), 1)
        self.btnLight5 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(13, self.btnLight5)), 1)
        self.btnLight6 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(4, self.btnLight6)), 1)  #kitchen
        self.btnLight7 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(47, self.btnLight7)), 1)
        self.btnLight8 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(self.light(46, self.btnLight8)), 1)

        self.btnSmoke0 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(self.smoke(6, self.btnSmoke0)), 0)
        self.btnSmoke1 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(self.smoke(7, self.btnSmoke1)), 0)
        self.btnSmoke2 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(self.smoke(8, self.btnSmoke2)), 0)
        self.btnSmoke3 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(self.smoke(9, self.btnSmoke3)), 0)
        self.btnSmoke4 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(self.smoke(10, self.btnSmoke4)), 0)
        self.btnSmoke5 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(self.smoke(11, self.btnSmoke5)), 0)

        self.btnCam1 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(self.camEnable(0, self.btnCam1)), 0)
        self.btnCam2 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(self.camEnable(1, self.btnCam2)), 0)
        self.btnCam3 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(self.camEnable(4, self.btnCam3)), 0)
        self.btnCam4 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(self.camEnable(0, self.btnCam4)), 0)
        self.btnCam5 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(self.camEnable(1, self.btnCam5)), 0)
        self.btnCam6 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(self.camEnable(4, self.btnCam6)), 0)

        self.btnFire1 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(self.fire(16, 31, self.btnFire1)), 0)
        self.btnFire2 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(self.fireSingle(41, self.btnFire2)), 0)
        self.btnFire3 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(self.fire(35, 53, self.btnFire3)), 0)
        self.btnFire4 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(self.fireSingle(22, self.btnFire4)), 0)
        self.btnFire6 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(self.fire(38, 42, self.btnFire6)), 0)

        self.btnAlarm1 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(self.alarm(26, self.btnAlarm1)), self.loop.create_task(self.sound())], 0)
        self.btnAlarm2 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(self.alarm(24, self.btnAlarm2)), self.loop.create_task(self.sound())], 0)
        self.btnAlarm3 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(self.alarm(36, self.btnAlarm3)), self.loop.create_task(self.sound())], 0)
        self.btnAlarm4 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(self.alarm(29, self.btnAlarm4)), self.loop.create_task(self.sound())], 0)
        self.btnAlarm5 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(self.alarm(27, self.btnAlarm5)), self.loop.create_task(self.sound())], 0)
        self.btnAlarm6 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(self.alarm(20, self.btnAlarm6)), self.loop.create_task(self.sound())], 0)

        self.btnHair5 = self.btn_father.btn(self.img_father.wilka, self.img_father.wilka_active,
                                            lambda: self.loop.create_task(self.fireSingle(34, self.btnHair5)), 1)
        self.btnHair6 = self.btn_father.btn(self.img_father.hair_dryer, self.img_father.hair_dryer_active,
                                            lambda: self.loop.create_task(self.fireSingle(33, self.btnHair6)), 1)

        self.btnVolumeUp = self.btn_father.btn(self.img_father.volumeUp, self.img_father.volumeUp,
                                               lambda: self.loop.create_task(self.volumeUp()), 0)
        self.btnVolumeDown = self.btn_father.btn(self.img_father.volumeDown, self.img_father.volumeDown,
                                                 lambda: self.loop.create_task(self.volumeDown()), 0)

        self.btnFirepalce = self.btn_father.btn(self.img_father.fireplace, self.img_father.fireplace_active,
                                                lambda: self.loop.create_task(self.fire(18, 43, self.btnFirepalce)), 1)
        self.btnTree = self.btn_father.btn(self.img_father.tree, self.img_father.tree_active,
                                           lambda: self.loop.create_task(self.tree(54, self.btnTree)), 1)

        self.btnPanel3 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(self.panel(23, self.btnPanel3)), 0)
        self.btnPanel4 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(self.panel(23, self.btnPanel4)), 0)
        self.btnPanel5 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(self.panel(28, self.btnPanel5)), 0)
        self.btnPanel6 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(self.panel(30, self.btnPanel6)), 0)
        self.btnPanel7 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(self.fireSingle(37, self.btnPanel7)), 1)

        self.btnTorch = self.btn_father.btn(self.img_father.torch, self.img_father.torch_active, lambda: self.loop.create_task(self.light(40, self.btnTorch)), 1)
        self.btnFan = self.btn_father.btn(self.img_father.vent, self.img_father.vent_active, lambda: self.loop.create_task(self.fan(self.btnFan)), 0)
        self.btnBalon = self.btn_father.btn(self.img_father.balon, self.img_father.balon_active, lambda: self.loop.create_task(self.light(21, self.btnBalon)), 0)
        self.btnKotel = self.btn_father.btn(self.img_father.kotel, self.img_father.kotel_active, lambda: self.loop.create_task(self.fireSingle(17, self.btnKotel)), 1)
        self.btnHot = self.btn_father.btn(self.img_father.kotel, self.img_father.kotel_active, lambda: self.loop.create_task(self.fireSingle(39, self.btnHot)), 1)



        self.btnTorch.place(x=915, y=212)  # floor 3 l
        self.btnFan.place(x=550, y=505)  # floor 3 l
        self.btnBalon.place(x=915, y=505)  # floor 3 l
        self.btnHot.place(x=915, y=450)  # floor 3 l
        self.btnKotel.place(x=405, y=353)  # floor 3 l


        self.btnManual.place(x=20, y=20)

        self.btnDoor5.place(x=185, y=212)  # floor 3 l
        self.btnDoor2.place(x=697, y=212)  # floor 3 r
        self.btnDoor0.place(x=185, y=353)  # floor 2 l
        self.btnDoor4.place(x=697, y=353)  # floor 2 r
        self.btnDoor3.place(x=185, y=505)  # floor 1 l
        self.btnDoor1.place(x=697, y=505)  # floor 1 r

        self.btnLed0.place(x=240, y=212)  # floor 3 l
        self.btnLed1.place(x=750, y=212)  # floor 3 l
        self.btnLed2.place(x=240, y=353)  # floor 3 l
        self.btnLed5.place(x=750, y=353)  # floor 3 l
        self.btnLed6.place(x=240, y=505)  # floor 3 l
        self.btnLed8.place(x=750, y=505)  # floor 3 l
        self.btnLed8.place(x=750, y=505)  # floor 3 l
        self.btnLed3.place(x=470, y=212)  # floor 3 l
        self.btnLed4.place(x=470, y=353)  # floor 3 l
        self.btnLed7.place(x=470, y=505)  # floor 3 l

        self.btnLight0.place(x=295, y=212)  # floor 3 l
        self.btnLight1.place(x=805, y=212)  # floor 3 l
        self.btnLight2.place(x=295, y=353)  # floor 3 l
        self.btnLight5.place(x=805, y=353)  # floor 3 l
        self.btnLight6.place(x=295, y=505)  # floor 3 l
        self.btnLight8.place(x=805, y=505)  # floor 3 l
        self.btnLight8.place(x=805, y=505)  # floor 3 l
        self.btnLight3.place(x=470, y=155)  # floor 3 l
        self.btnLight4.place(x=470, y=300)  # floor 3 l
        self.btnLight7.place(x=470, y=455)  # floor 3 l

        self.btnTree.place(x=915, y=353)  # floor 3 l
        self.btnFirepalce.place(x=915, y=299)  # floor 3 l

        self.btnSmoke0.place(x=350, y=212)  # floor 3 l
        self.btnSmoke1.place(x=860, y=212)  # floor 3 l
        self.btnSmoke2.place(x=350, y=353)  # floor 3 l
        self.btnSmoke3.place(x=860, y=353)  # floor 3 l
        self.btnSmoke4.place(x=350, y=505)  # floor 3 l
        self.btnSmoke5.place(x=860, y=505)  # floor 3 l

        self.btnCam1.place(x=185, y=158)
        self.btnCam2.place(x=697, y=158)
        self.btnCam3.place(x=185, y=299)
        self.btnCam4.place(x=697, y=299)
        self.btnCam5.place(x=185, y=450)
        self.btnCam6.place(x=697, y=450)

        self.btnFire1.place(x=240, y=158)
        self.btnFire2.place(x=750, y=158)
        self.btnFire3.place(x=240, y=450)
        self.btnFire4.place(x=750, y=299)
        self.btnFire6.place(x=750, y=450)

        self.btnAlarm1.place(x=295, y=158)
        self.btnAlarm2.place(x=805, y=158)
        self.btnAlarm3.place(x=295, y=450)
        self.btnAlarm4.place(x=240, y=299)
        self.btnAlarm5.place(x=805, y=299)
        self.btnAlarm6.place(x=805, y=450)

        self.btnHair5.place(x=350, y=158)
        self.btnHair6.place(x=295, y=299)

        self.btnPanel4.place(x=860, y=450)
        self.btnPanel5.place(x=860, y=299)
        self.btnPanel6.place(x=350, y=299)
        self.btnPanel7.place(x=350, y=450)

        self.btnVolumeUp.place(x=30, y=125)
        self.btnVolumeDown.place(x=100, y=125)

        self.cams = [self.btnCam6,self.btnCam5, self.btnCam4, self.btnCam3, self.btnCam2, self.btnCam1]
        self.smokes = [self.btnSmoke5, self.btnSmoke4, self.btnSmoke3, self.btnSmoke2, self.btnSmoke0, self.btnSmoke1]

    def ledSerial(self, method, param1, param2):
        string = "<LEDWRITE" + "\0" + str(param1) + "\0" + str(param2) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

    def fireSerial(self, param1, param2):
        string = "<LEDFIREA" + "\0" + str(param1) + "\0" + str(param2) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def fireSerialSingle(self, param1):
        string = "<LEDFIREB" + "\0" + str(param1)  + "\0" + str(63) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())


    def servo(self, method, param1):
        string = "<" + method + "\0" + str(param1) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

    def smokeSerial(self, param1):
        string = "<SMOKE" + "\0" + str(param1) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

    def blink(self, param1, param2, param3):
        string = "<LEDBLINK" + "\0" + str(param1) + "\0" + str(param2) + "\0" + str(param3) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def serialFan(self, comand):
        string = f"<{comand}>"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def blackout(self):
        string = "<BLACKOUT>"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def default(self):
        string = "<DEFAULT>"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(.1)

    def change_img(self, btn):
        btn.status = not btn.status
        if (btn.status  == 1):
            print('active')
            btn.config(image=btn.active)
        else:
            print('disabled')
            btn.config(image=btn.pasive)
        return btn

    def switchCam(self, camInstance):
        for camVal in self.cams:
            camVal.config(image=camInstance.pasive)
            camVal["state"] = "active"
        self.change_img(camInstance)
        camInstance["state"] = "disable"

    async def camEnable(self, camName, cam):
        print(camName)
        try:
            self.switchCam(cam)
            cam = cv2.VideoCapture(camName)
            self.status = not self.status
            if self.status != False:
                while (True):
                    if self.status == False:
                        cam.release()
                        cv2.destroyAllWindows()
                        break
                    ret, image = cam.read()
                    cv2.imshow(self.name, image)
                    cv2.waitKey(1)
                    await asyncio.sleep(0.01)
            else:
                while (True):
                    if self.status == True:
                        cam.release()
                        cv2.destroyAllWindows()
                        break
                    ret, image = cam.read()
                    cv2.imshow(self.name, image)
                    cv2.waitKey(1)
                    await asyncio.sleep(0.01)
        except:
            await asyncio.sleep(.1)
            await self.camEnable(camName, cam)
            await asyncio.sleep(.1)


    async def scenary_action_1(self, btn):
        self.change_img(btn)
        self.blackout()
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(5)
        self.ledSerial('LEDWRITE', 12, 255)
        await asyncio.sleep(5)
        self.fireSerial(34, 63)
        await asyncio.sleep(5)
        self.smokeSerial(6)
        await asyncio.sleep(.3)
        self.ledSerial('LEDWRITE', 12, 0)
        await asyncio.sleep(.3)
        self.ledSerial('LEDWRITE', 34, 0)
        await asyncio.sleep(3)
        self.blink(26, 200, 200)
        await self.sound()
        await asyncio.sleep(1)
        self.fireSerial(16,31)
        await asyncio.sleep(10)
        self.servo('SERVOOPEN', 5)
        await asyncio.sleep(1)
        self.serialFan('FANON')
        await asyncio.sleep(5)
        await self.sound()
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 12, 150)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 16, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 31, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 26, 0)
        await asyncio.sleep(.2)
        self.servo('SERVOCLOSE', 5)
        await asyncio.sleep(.2)
        self.serialFan('FANOFF')
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()

    async def scenary_action_2(self, btn):
        self.change_img(btn)
        self.blackout()
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(5)
        self.ledSerial('LEDWRITE', 46, 255)
        self.fireSerialSingle(39)
        await asyncio.sleep(5)
        self.smokeSerial(8)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 46, 0)
        await asyncio.sleep(3)
        self.fireSerial(38,42)
        await asyncio.sleep(.3)
        self.blink(20, 200, 200)
        await self.sound()
        await asyncio.sleep(3)
        self.ledSerial('LEDWRITE', 21, 255)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', 21, 0)
        await asyncio.sleep(10)
        self.servo('SERVOOPEN', 1)
        await asyncio.sleep(1)
        self.serialFan('FANON')
        await asyncio.sleep(5)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 38, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 42, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 20, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 39, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 21, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 46, 150)
        await asyncio.sleep(.2)
        await self.sound()
        await asyncio.sleep(10)
        self.serialFan('FANOFF')
        await asyncio.sleep(.5)
        self.servo('SERVOCLOSE', 1)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.default()


    async def scenary_action_3(self, btn):
        self.change_img(btn)
        self.blackout()
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(5)
        self.ledSerial('LEDWRITE', 8, 255)
        await asyncio.sleep(5)
        self.fireSerial(41,40)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 8, 0)
        await asyncio.sleep(.3)
        self.blink(24, 200, 200)
        await self.sound()
        await asyncio.sleep(10)
        self.servo('SERVOOPEN', 2)
        await asyncio.sleep(1)
        self.serialFan('FANON')
        await asyncio.sleep(5)
        await self.sound()
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 8, 150)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 41, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 40, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 24, 0)
        await asyncio.sleep(5)
        self.serialFan('FANOFF')
        await asyncio.sleep(1)
        self.servo('SERVOCLOSE', 2)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()

    async def sound(self):
        self.alarmStatus = not self.alarmStatus
        if self.alarmStatus == 1:
            mixer.music.load('siren.mp3')  # Loading Music File
            mixer.music.play()
            await asyncio.sleep(.1)
        else:
            mixer.music.stop()

    async def scenary_action_4(self, btn):
        self.change_img(btn)
        self.blackout()
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(5)
        self.ledSerial('LEDWRITE', 13, 255)
        await asyncio.sleep(1)
        self.fireSerial(18,43)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 54, 255)
        await asyncio.sleep(5)
        self.smokeSerial(9)
        await asyncio.sleep(3)
        self.ledSerial('LEDWRITE', 13, 0)
        self.blink(27, 200, 200)
        await self.sound()
        await asyncio.sleep(1)
        self.fireSerialSingle(22)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', 54, 0)
        await asyncio.sleep(10)
        self.servo('SERVOOPEN', 4)
        await asyncio.sleep(1)
        self.serialFan('FANON')
        await asyncio.sleep(5)
        await self.sound()
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 13, 150)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 22, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 27, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 54, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 18, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 43, 0)
        await asyncio.sleep(5)
        self.serialFan('FANOFF')
        await asyncio.sleep(1)
        self.servo('SERVOCLOSE', 4)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()

    async def scenary_action_5(self, btn):
        self.change_img(btn)
        self.blackout()
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(5)
        self.ledSerial('LEDWRITE', 4, 255)
        await asyncio.sleep(1)
        self.fireSerialSingle(37)
        await asyncio.sleep(6)
        self.smokeSerial(9)
        await asyncio.sleep(3)
        self.ledSerial('LEDWRITE', 4, 0)
        self.blink(36, 200, 200)
        await self.sound()
        await asyncio.sleep(1)
        self.fireSerial(35,53)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', 37, 0)
        await asyncio.sleep(10)
        self.servo('SERVOOPEN', 3)
        await asyncio.sleep(1)
        self.serialFan('FANON')
        await asyncio.sleep(5)
        await self.sound()
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 4, 150)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 36, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 35, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 53, 0)
        await asyncio.sleep(5)
        self.serialFan('FANOFF')
        await asyncio.sleep(1)
        self.servo('SERVOCLOSE', 3)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()

    async def new(self):
        self.scenary = Toplevel()
        self.scenary.geometry("1020x600")
        self.scenary.config(background='#ffffff')



        self.btn_father_sc = WD_Button(self.scenary)

        self.scenary1 = self.btn_father_sc.btn(self.img_father.scenary_1, self.img_father.scenary_active_1,
                                            lambda: self.loop.create_task(self.scenary_action_1(self.scenary1)), 0, 400, 50)
        self.scenary1.place(x=300, y=100)  # floor 3 l

        self.scenary2 = self.btn_father_sc.btn(self.img_father.scenary_1, self.img_father.scenary_active_1,
                                            lambda: self.loop.create_task(self.scenary_action_2(self.scenary2)), 0, 400, 50)
        self.scenary2.place(x=300, y=170)  # floor 3 l

        self.scenary3 = self.btn_father_sc.btn(self.img_father.scenary_1, self.img_father.scenary_active_1,
                                            lambda: self.loop.create_task(self.scenary_action_3(self.scenary3)), 0, 400, 50)
        self.scenary3.place(x=300, y=240)  # floor 3 l

        self.scenary4 = self.btn_father_sc.btn(self.img_father.scenary_1, self.img_father.scenary_active_1,
                                            lambda: self.loop.create_task(self.scenary_action_4(self.scenary4)), 0, 400, 50)
        self.scenary4.place(x=300, y=310)  # floor 3 l

        self.scenary5 = self.btn_father_sc.btn(self.img_father.scenary_1, self.img_father.scenary_active_1,
                                            lambda: self.loop.create_task(self.scenary_action_5(self.scenary5)), 0, 400, 50)
        self.scenary5.place(x=300, y=380)  # floor 3 l

        self.scenaries = [self.scenary1, self.scenary2, self.scenary3, self.scenary4, self.scenary5]

        self.btnScenary = self.btn_father_sc.btn(self.img_father.scenary_btn,self.img_father.scenary_btn,
                                                 lambda: self.loop.create_task(self.scenary_close()), 0, 222, 46)
        self.btnScenary.place(x=20, y=20)

    async def scenary_close(self):
        self.scenary.destroy()

    async def fireplace(self, index, fpalce):
        self.change_img(fpalce)

    async def tree(self, index, tree):
        self.change_img(tree)
        status = 0 if tree.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)

    async def door(self, index, door):
        self.change_img(door)
        comand = 'SERVOOPEN' if door.status == 1 else 'SERVOCLOSE'
        self.servo(comand, index)

    async def led(self, index, led):
        self.change_img(led)
        status = 0 if led.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)

    async def light(self, index, light):
        self.change_img(light)
        status = 0 if light.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)

    async def fan(self, fan):
        self.change_img(fan)
        comand = 'FANOFF' if fan.status == 0 else 'FANON'
        self.serialFan(comand)

    async def smoke(self, index, smoke):
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"]="disabled"
        self.smokeSerial(index)
        await asyncio.sleep(5)
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"]="active"

    async def fire(self, index1, index2, fire):
        self.change_img(fire)
        status = 0 if fire.status == 0 else 255
        if status == 0:
            self.ledSerial("LEDWRITE", index1, 0)
            self.ledSerial("LEDWRITE", index2, 0)
        else:
            self.fireSerial(index1, index2)

    async def fireSingle(self, index1, fire):
        self.change_img(fire)
        status = 0 if fire.status == 0 else 255
        if status == 0:
            self.ledSerial("LEDWRITE", index1, 0)  
        else:
            self.fireSerialSingle(index1)

    async def alarm(self, index, alarm):
        self.change_img(alarm)
        status = 0 if alarm.status == 0 else 255
        if status == 0:
            self.ledSerial('LEDWRITE',index, 0)
        else:
            self.blink(index, 200, 200)
        print('alarm' + str(index))

    async def hair(self, index, hair):
        self.change_img(hair)
        status = 0 if hair.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)
        print('hair' + str(index))

    async def panel(self, index, panel):
        self.change_img(panel)
        status = 0 if panel.status == 0 else 255
        if status == 0:
            self.ledSerial('LEDWRITE',index, 0)
        else:
            self.blink(index, 200, 200)
        print('alarm' + str(index))                        
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

def main():
    asyncio.run(App().exec())


if __name__ == '__main__':
    main()
