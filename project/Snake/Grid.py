import random
from project.Snake.Snake import Snake


class Grid:
    def __init__(self):
        self.SIZE = 100
        self.grid = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.snake = Snake()

    def generateRandomScore(self):
        x = random.randint(0,self.SIZE-1)
        y = random.randint(0,self.SIZE-1)
        return (x,y)

    def generateRandomLocation(self):
        (x,y) = self.generateRandomScore()
        divider = self.SIZE - 10
        return (x % divider + 5, y % divider + 5)
Grid()