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
        key_dic = {
            Key.right: 0,
            Key.up: 1,
            Key.left: 2,
            Key.down: 3
        }
        if key in key_dic:
            if (self.direction + key_dic[key]) % 4 != 0:
                self.direction = key_dic[key]
            # print(self.direction)

    def setDirerctionListener(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()