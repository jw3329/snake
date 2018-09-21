import random

from project.Snake.Snake import Snake


class Grid:
    def __init__(self):
        self.SIZE = 15
        self.grid = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.snake = Snake()
        # choose random grid to put the head and the direction to go
        self.snake.loc_list.append(self.generateRandomLocation())
        self.snake.direction = self.generateRandomDirection()
        # mark snake on the grid
        self.setSnake()


    def generateRandomScore(self):
        x = random.randint(0,self.SIZE-1)
        y = random.randint(0,self.SIZE-1)
        return (x,y)

    def generateRandomLocation(self):
        (x,y) = self.generateRandomScore()
        divider = self.SIZE - 10
        return (x % divider + 5, y % divider + 5)

    def generateRandomDirection(self):
        direction = random.randint(0,3)
        return direction

    def setSnake(self):
        # get body length and mark it into grid
        print('hi')
        x = [0,1,0,-1]
        y = [-1,0,1,0]
        head = self.snake.loc_list[0]
        self.grid[head[0]][head[1]] = 1     #head
        cur_x,cur_y = head[0],head[1]
        direct = self.snake.direction
        for i in range(self.snake.body_length):
            cur_x += x[direct]
            cur_y += y[direct]
            self.snake.loc_list.append((cur_x,cur_y))
            self.grid[cur_x][cur_y] = 1
        self.printGrid()
        print(direct)

    def printGrid(self):
        n = len(self.grid)
        for i in range(n):
            print(self.grid[i])

    def move(self):
        x = [0,-1,0,1]
        y = [1,0,-1,0]
        snake = self.snake
        grid = self.grid
        head = snake.loc_list[0]
        trial_x = head[0] + x[snake.direction]
        trial_y = head[1] + y[snake.direction]
        grid[trial_x][trial_y] = 1
        snake.loc_list.insert(0,(trial_x,trial_y))
        last = snake.loc_list.pop()
        grid[last[0]][last[1]] = 0
        self.printGrid()
        print(snake.direction)
g = Grid()
print('')
g.move()
