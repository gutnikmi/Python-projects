from rps_int_re import rps_intg
from tkinter import *
from PIL import ImageTk, Image
import warnings
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)


class ChooseFig:
    def __init__(self):
        self.a = 1
        self.res = 'idk'

    def match_img(self, arg):
        match arg:
            case 1:
                self.img1 = Image.open('Rock.png')
                self.img1 = self.img1.resize((150, 150), Image.LANCZOS)
                self.img1 = ImageTk.PhotoImage(self.img1)

            case 2:
                self.img1 = Image.open('Paper.png')
                self.img1 = self.img1.resize((150, 150), Image.LANCZOS)
                self.img1 = ImageTk.PhotoImage(self.img1)

            case 3:
                self.img1 = Image.open('Scissors.png')
                self.img1 = self.img1.resize((150, 150), Image.LANCZOS)
                self.img1 = ImageTk.PhotoImage(self.img1)

            case _:
                print('You fucked up')

    def change_p(self):
        self.match_img(self.a)
        if self.a < 3:
            self.a += 1
        else:
            self.a = 1
        btn = Button(image=self.img1, padx="5", pady="0", font="16", command=self.change_p)
        btn.grid(row=1, column=1, padx=8, pady=0)


class CompChoice:
    def comp_turn(self):
        self.a = chs.a - 1
        self.res, self.c_c = rps_intg(self.a)
        match self.res:
            case "w":
                self.res = "  You win!    "
            case "d":
                self.res = "It's a draw!  "
            case "l":
                self.res = " You loose   "
        match self.c_c:
            case 1:
                self.img2 = Image.open('Rock.png')
                self.img2 = self.img2.resize((150, 150), Image.LANCZOS)
                self.img2 = ImageTk.PhotoImage(self.img2)
            case 2:
                self.img2 = Image.open('Paper.png')
                self.img2 = self.img2.resize((150, 150), Image.LANCZOS)
                self.img2 = ImageTk.PhotoImage(self.img2)
            case 3:
                self.img2 = Image.open('Scissors.png')
                self.img2 = self.img2.resize((150, 150), Image.LANCZOS)
                self.img2 = ImageTk.PhotoImage(self.img2)
            case _:
                print('You fucked up')
        btn = Button(text=self.res, padx="10", pady="0", font="16", command=self.comp_turn)
        btn.grid(row=2, column=1, padx=8, pady=0)
        # lbl = Label(text=res, padx="80", pady="10", font="1")
        # lbl.grid(row=2, column=1, padx=8, pady=0)
        lbl = Label(image=self.img2, padx="80", pady="10", font="1")
        lbl.grid(row=3, column=1, padx=8, pady=0)



root = Tk()
root.title("Rock Paper Scissors")
root.geometry("550x500")
chs = ChooseFig()
cchs = CompChoice()
chs.change_p()
cchs.comp_turn()

label = Label(text=" ", padx="70", pady="10", font="1")
label.grid(row=0, column=0, padx=8, pady=0)
root.mainloop()

# def choose_pic():
#     global a
#     global c
#     global img, img2
#     global res
#     global c_c
#     match a:
#         case 1:
#             img = Image.open('Rock.png')
#             img = img.resize((150, 150), Image.LANCZOS)
#             img = ImageTk.PhotoImage(img)
#             c = "r"
#         case 2:
#             img = Image.open('Paper.png')
#             img = img.resize((150, 150), Image.LANCZOS)
#             img = ImageTk.PhotoImage(img)
#             c = "p"
#         case 3:
#             img = Image.open('Scissors.png')
#             img = img.resize((150, 150), Image.LANCZOS)
#             img = ImageTk.PhotoImage(img)
#             c = "s"
#         case _:
#             print('You fucked up')
#     if a < 3:
#         a += 1
#     else:
#         a = 1
#     res, c_c = rps_intg(c)
#     match res:
#         case "w":
#             res = "You win!"
#         case "d":
#             res = "It's a draw!"
#         case "l":
#             res = "You loose"
#
#     btn = Button(image=img, padx="5", pady="0", font="16", command=choose_pic)
#     btn.grid(row=1, column=1, padx=8, pady=0)
#     match c_c:
#         case "r":
#             img2 = Image.open('Rock.png')
#             img2 = img2.resize((150, 150), Image.LANCZOS)
#             img2 = ImageTk.PhotoImage(img2)
#         case "p":
#             img2 = Image.open('Paper.png')
#             img2 = img2.resize((150, 150), Image.LANCZOS)
#             img2 = ImageTk.PhotoImage(img2)
#         case "s":
#             img2 = Image.open('Scissors.png')
#             img2 = img2.resize((150, 150), Image.LANCZOS)
#             img2 = ImageTk.PhotoImage(img2)
#         case _:
#             print('You fucked up')
#
#     lbl = Label(text=res, padx="80", pady="10", font="1")
#     lbl.grid(row=2, column=1, padx=8, pady=0)
#     lbl = Label(image=img2, padx="80", pady="10", font="1")
#     lbl.grid(row=3, column=1, padx=8, pady=0)
