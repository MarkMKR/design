from PIL import ImageTk, Image

app_backround = ImageTk.PhotoImage(Image.open("img/back.png"))
lock = ImageTk.PhotoImage(Image.open("img/door.png").resize((60, 60)))
lock_active = ImageTk.PhotoImage(Image.open("img/door-active.png").resize((60, 60)))