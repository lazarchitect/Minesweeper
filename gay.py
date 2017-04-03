import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()


flagPic = ImageTk.PhotoImage(Image.open("flag.bmp"))
tkinter.Button(root, image = flagPic).pack()

root.mainloop()