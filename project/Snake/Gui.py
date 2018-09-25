from tkinter import *

from project.Snake.State import State

WINDOW_SIZE = 700


class Gui(State):

    def _center_window(self,root,w, h):
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def __init__(self):
        self.root = Tk()
        self._center_window(self.root,WINDOW_SIZE,WINDOW_SIZE)
        self.root.resizable(width=False,height=False)
        self.root.title('Snake')
        super().__init__()
        grid_size = WINDOW_SIZE // self.SIZE
        print(grid_size)
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if i + j % 2 == 0:
                    label = Label(self.root,bg='red')
                else:
                    label = Label(self.root,bg='blue')
                label.grid(row=i*grid_size,column=j*grid_size,rowspan = grid_size, columnspan = grid_size)
        # self.frame = Frame(self.root,width = 600, height = 600)
        # self.frame.pack()
        self.root.mainloop()


Gui()





