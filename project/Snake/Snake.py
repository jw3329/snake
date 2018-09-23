from threading import Thread
from pynput.keyboard import Key, Listener

class Snake:
    def __init__(self):
        self.body_length = 1
        self.score = 0
        self.direction = 0      # right = 0, up = 1, left = 2, down = 3
        self.loc_list = []

        directionThread = Thread(target=self.setDirerctionListener,args=())
        directionThread.start()

    def on_press(self, key):
        x = [1,0,-1,0]
        y = [0,-1,0,1]
        key_dic = {
            Key.right: 0,
            Key.up: 1,
            Key.left: 2,
            Key.down: 3
        }
        head = self.loc_list[0]
        body = self.loc_list[1]
        if key in key_dic:
            if (head[0] + x[key_dic[key]], head[1] + y[key_dic[key]]) != body:
                self.direction = key_dic[key]
            # print(self.direction)

    def setDirerctionListener(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()