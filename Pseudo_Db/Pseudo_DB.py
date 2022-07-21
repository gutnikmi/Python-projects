from tkinter import *

exe = 0
lst = []
lns = [0]

class Entr:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        pass

    def call(self):
        print(self.name)

    def labl(self, text):
        self.label = Label(text=text, padx="5", pady="0", font="16")
        self.label.grid(row=2 + exe, column=1, padx=10, pady=0)
        self.label = Label(text=exe, padx="5", pady="0", font="16")
        self.label.grid(row=2 + exe, column=0, padx=0, pady=0)


def add_button():
    global exe
    e = ent.get()
    if int(opt.get()) == (len(lns)-1):
        lst.append(Entr(f"Line{exe}"))
        lst[exe].labl(e)
        exe += 1
        lns.append(exe)
        opt.set(exe)
    else:
        texe = exe
        exe = int(opt.get())
        e = ent.get()
        lst[int(opt.get())].labl(e)
        exe = texe
    option = OptionMenu(root, opt, *lns)
    option.config(background="#555", foreground="#ccc")
    option.grid(row=1, column=4, padx=10, pady=0)
    ent.delete(0, END)



def rem_button():
    global exe
    texe = exe
    exe = int(opt.get())
    f = "                           "
    lst[int(opt.get())].labl(f)
    exe = texe


root = Tk()
root.title("Pseudo DB")
root.geometry("550x500")
lbl = Label()

opt = StringVar()

label = Label(text=" ", padx="5", pady="0", font="1")
label.grid(row=0, column=0, padx=8, pady=0)

bta = Button(text="Add text", background="#555", foreground="#ccc",
             padx="0", pady="0", font="10", command=add_button,
             )
bta.grid(row=1, column=2, padx=10, pady=10)

btr = Button(text="Drop text", background="#555", foreground="#ccc",
             padx="0", pady="0", font="10", command=rem_button,
             )
btr.grid(row=1, column=3, padx=10, pady=10)

ent = Entry(font="16")
ent.grid(row=1, column=1, padx=10, pady=30)

option = OptionMenu(root, opt, "0")
opt.set(0)
option.config(background="#555", foreground="#ccc")
option.grid(row=1, column=4, padx=10, pady=0)

root.mainloop()
