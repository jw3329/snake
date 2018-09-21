import random
import time

from project.Snake.Snake import Snake

NOTHING = 0
BODY = 1
WALL = 2
FOOD = 3
HEAD = 4

class State:
    def __init__(self):
        self.SIZE = 20
        self.grid = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]

        for i in range(self.SIZE):
            self.grid[0][i] = WALL
            self.grid[i][0] = WALL
            self.grid[self.SIZE-1][i] = WALL
            self.grid[i][self.SIZE-1] = WALL
            
        self.snake = Snake()
        # choose random grid to put the head and the direction to go
        self.snake.loc_list.append(self.generateRandomLocation())
        self.snake.direction = self.generateRandomDirection()
        # mark snake on the grid
        self.setSnake()
        self.gameLoop()

    def generateRandomLocation(self):
        fourth = self.SIZE//4
        x = random.randint(fourth, fourth*3)
        y = random.randint(fourth, fourth*3)
        return (x,y)

    def generateRandomDirection(self):
        direction = random.randint(0,3)
        return direction

    def generateFruitLocation(self):
        while True:
            x = random.randint(0,self.SIZE-1)
            y = random.randint(0,self.SIZE-1)
            if self.grid[y][x] not in [BODY,WALL]:
                return (x,y)

    def setSnake(self):
        # get body length and mark it into grid
        x = [1,0,-1,0]
        y = [0,-1,0,1]
        head_x, head_y = self.snake.loc_list[0]
        self.grid[head_y][head_x] = HEAD     #head
        cur_x,cur_y = head_x, head_y
        direct = self.snake.direction
        for i in range(self.snake.body_length):
            cur_x -= x[direct]
            cur_y -= y[direct]
            self.snake.loc_list.append((cur_x,cur_y))
            self.grid[cur_y][cur_x] = BODY

    def printState(self):
        n = len(self.grid)
        for i in range(n):
            print(self.grid[i])

    def nextState(self):
        x = [1,0,-1,0]
        y = [0,-1,0,1]
        head = self.snake.loc_list[0]
        self.grid[head[1]][head[0]] = BODY
        trial_x = head[0] + x[self.snake.direction]
        trial_y = head[1] + y[self.snake.direction]
        new_head_loc = self.grid[trial_y][trial_x]
        if new_head_loc != WALL and new_head_loc != BODY:
            self.grid[trial_y][trial_x] = HEAD
            self.snake.loc_list.insert(0,(trial_x,trial_y))
            if new_head_loc == FOOD:
                self.snake.body_length += 1
                self.snake.score += 1
            else:
                last_x, last_y = self.snake.loc_list.pop()
                self.grid[last_y][last_x] = NOTHING

    def addTail(self):
        last = self.snake.loc_list[-1]
        self.nextState()
        self.snake.loc_list.append(last)
        self.grid[last[1]][last[0]] = BODY
        self.snake.body_length += 1

    def gameLoop(self):
        fruit_loc = self.generateFruitLocation()
        self.grid[fruit_loc[1]][fruit_loc[0]] = FOOD
        while True:
            head_loc = self.snake.loc_list[0]
            # print(head_loc)
            if self.grid[head_loc[1]][head_loc[0]] in [BODY, WALL]: break
            if fruit_loc == head_loc:
                fruit_loc = self.generateFruitLocation()
                self.grid[fruit_loc[1]][fruit_loc[0]] = FOOD
                self.snake.score += 1
                self.addTail()
            else:
                self.nextState()
            self.printState()
            print('')
            time.sleep(1)
        print('game over')


State()