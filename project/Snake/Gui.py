import time
from threading import Thread
from tkinter import *

from project.Snake.State import State

WINDOW_SIZE = 700
PADDING = 20

NOTHING = 0
BODY = 1
WALL = 2
FOOD = 3
HEAD = 4

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
        # self.root.geometry('%dx%d' % (WINDOW_SIZE,WINDOW_SIZE))
        self.frame = Frame(self.root,width = WINDOW_SIZE, height=WINDOW_SIZE)
        self.frame.pack(padx=PADDING,pady=PADDING)
        self._center_window(self.root,WINDOW_SIZE,WINDOW_SIZE)
        self.root.resizable(width=False,height=False)
        self.root.title('Snake')
        super().__init__()
        self.root.update()
        self.grid_size = self.frame.winfo_width() // self.SIZE
        self.frame_list = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                # print(i, j)
                if i in [0,self.SIZE-1] or j in [0,self.SIZE-1]:
                    label = Frame(self.frame,bg='gray40',width=self.grid_size,height=self.grid_size)
                elif (i + j) % 2 == 0:
                    # print('even',i,j)
                    label = Frame(self.frame,bg='dark green',width=self.grid_size,height=self.grid_size)
                else:
                    # print('odd',i,j)
                    label = Frame(self.frame,bg='lime green',width=self.grid_size,height=self.grid_size)
                self.frame_list[i][j] = label
                label.grid(row=i,column=j)
        self.restore = []
        self.gameLoop()
        self.root.mainloop()

    def gameLoop(self):
        fruit_loc = self.generateFruitLocation()
        self.grid[fruit_loc[1]][fruit_loc[0]] = FOOD
        head_loc = self.snake.loc_list[0]
        while True:
            # print(head_loc)
            if fruit_loc == head_loc:
                fruit_loc = self.generateFruitLocation()
                self.grid[fruit_loc[1]][fruit_loc[0]] = FOOD
                # self.snake.score += 1
                # self.addTail()
            self.nextState()
            head_loc = self.snake.loc_list[0]
            if self.grid[head_loc[1]][head_loc[0]] in [BODY, WALL]: break
            # self.printState()
            # print('')
            # fruit = Frame(self.frame, bg='red', width=self.grid_size, height=self.grid_size)
            # gui_thread = Thread(target=self.updateGUI, args=(fruit_loc,))
            # gui_thread.start()
            # gui_thread.join()
            self.updateGUI(fruit_loc)
            time.sleep(0.1)
        print('game over')

    def updateGUI(self,fruit_loc):
        for rest in self.restore:
            i,j = rest[1],rest[0]
            if i in [0, self.SIZE - 1] or j in [0, self.SIZE - 1]:
                self.frame_list[i][j].config(bg='gray40')
            elif (i + j) % 2 == 0:
                # print('even',i,j)
                self.frame_list[i][j].config(bg='dark green')
            else:
                # print('odd',i,j)
                self.frame_list[i][j].config(bg='lime green')
        size = self.grid_size
        self.frame_list[fruit_loc[1]][fruit_loc[0]].config(bg='red')
        snake_loc = self.snake.loc_list
        head = snake_loc[0]
        self.frame_list[head[1]][head[0]].config(bg='yellow')
        for body in snake_loc[1:]:
            self.frame_list[body[1]][body[0]].config(bg='white')
        self.frame.update()
        self.restore = [fruit_loc] + snake_loc
Gui()





