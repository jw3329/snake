import random

from Snake import Snake

NOTHING = 0
BODY = 1
WALL = 2
FOOD = 3

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

    def generateRandomLocation(self):
        fourth = self.SIZE//4
        x = random.randint(fourth, fourth*3)
        y = random.randint(fourth, fourth*3)
        return (x,y)

    def generateRandomDirection(self):
        direction = random.randint(0,3)
        return direction

    def setSnake(self):
        # get body length and mark it into grid
        x = [1,0,-1,0]
        y = [0,-1,0,1]
        head_x, head_y = self.snake.loc_list[0]
        self.grid[head_y][head_x] = BODY     #head
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
        trial_x = head[0] + x[self.snake.direction]
        trial_y = head[1] + y[self.snake.direction]
        newHeadLoc = self.grid[trial_y][trial_x]
        if newHeadLoc != WALL and newHeadLoc != BODY:
            self.grid[trial_y][trial_x] = BODY
            self.snake.loc_list.insert(0,(trial_x,trial_y))
            if newHeadLoc == FOOD:
                self.snake.body_length += 1
                self.snake.score += 1
            else:
                last_x, last_y = self.snake.loc_list.pop()
                self.grid[last_y][last_x] = NOTHING


g = State()
g.printState()
print(g.snake.direction)

print('')

g.nextState()
g.printState()
print(g.snake.direction)