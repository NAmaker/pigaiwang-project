from tkinter import *


class Gui_input:
    x = None
    txt = None

    def __init__(self, titl):
        window = Tk()
        self.window = window
        self.window.title(titl)
        self.window.geometry("780x600")
        txt = Text(self.window, width=100)
        txt.grid(column=1, row=0)
        self.txt=txt

        btn = Button(self.window, text="点击确定", command=self.clicked,bg='red')
        btn.grid(column=4, row=4)
        self.window.mainloop()

    def clicked(self, ):
        self.x = self.txt.get('0.0','end')
        self.window.destroy()


