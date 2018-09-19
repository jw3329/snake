from pynput.keyboard import Key, Listener

class Snake:
    def __init__(self):
        self.body_length = 1
        self.score = 0
        self.direction = 0      # right = 0, up = 1, left = 2, down = 3
        self.speed = 1
        self.head = (0,0)

        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self,key):
        key_dic = {
            Key.right: 0,
            Key.up: 1,
            Key.left: 2,
            Key.down: 3
        }
        if key in key_dic:
            self.direction = key_dic[key]
            #print(self.direction)



Snake()