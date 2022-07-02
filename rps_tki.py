from rps import rps_intg
from tkinter import *
from PIL import ImageTk, Image
import warnings
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)
a = 1
res = "idk"


def choose_pic():
    global a
    global c
    global img, img2
    global res
    global c_c
    match a:
        case 1:
            img = Image.open('Rock.png')
            img = img.resize((150, 150), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            c = "r"
        case 2:
            img = Image.open('Paper.png')
            img = img.resize((150, 150), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            c = "p"
        case 3:
            img = Image.open('Scissors.png')
            img = img.resize((150, 150), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            c = "s"
        case _:
            print('You fucked up')
    if a < 3:
        a += 1
    else:
        a = 1
    res, c_c = rps_intg(c)
    match res:
        case "w":
            res = "You win!"
        case "d":
            res = "It's a draw!"
        case "L":
            res = "You loose"
    # if res == "w":
    #     res = "You win!"
    # elif res == "d":
    #     res = "It's a draw"
    # else:
    #     res == "You loose"
    btn = Button(image=img, padx="5", pady="0", font="16", command=choose_pic)
    btn.grid(row=1, column=1, padx=8, pady=0)
    match c_c:
        case "r":
            img2 = Image.open('Rock.png')
            img2 = img2.resize((150, 150), Image.LANCZOS)
            img2 = ImageTk.PhotoImage(img2)
        case "p":
            img2 = Image.open('Paper.png')
            img2 = img2.resize((150, 150), Image.LANCZOS)
            img2 = ImageTk.PhotoImage(img2)
        case "s":
            img2 = Image.open('Scissors.png')
            img2 = img2.resize((150, 150), Image.LANCZOS)
            img2 = ImageTk.PhotoImage(img2)
        case _:
            print('You fucked up')

    lbl = Label(text=res, padx="80", pady="10", font="1")
    lbl.grid(row=2, column=1, padx=8, pady=0)
    lbl = Label(image=img2, padx="80", pady="10", font="1")
    lbl.grid(row=3, column=1, padx=8, pady=0)




root = Tk()
root.title("Rock Paper Scissors")
root.geometry("550x500")
choose_pic()



label = Label(text=" ", padx="70", pady="10", font="1")
label.grid(row=0, column=0, padx=8, pady=0)
root.mainloop()
