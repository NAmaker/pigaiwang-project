from tkinter import *

class Gui_txt:

    x = None
    txt = None
    def __init__(self, titl):
        window = Tk()
        self.window = window
        self.window.title(titl)
        self.window.geometry("700x500")
        txt = Entry(self.window, width=60)
        txt.grid(column=1, row=0)
        self.txt = txt
        btn = Button(self.window, text="请点击确定", command=self.clicked,bg='red')
        btn.grid(column=4, row=4)
        self.window.mainloop()


    def clicked(self,):
        self.x = self.txt.get()
        self.window.destroy()


name = Gui_txt("输入你的账号")
name = name.x

