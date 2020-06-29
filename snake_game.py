from random import randint
from time import sleep
import keyboard
import curses

# import tkinter as tk  # Para el futuro debo hacerlo fuera de la consola


class Snake:
    def __init__(self, limits=tuple):
        self.xf, self.yf = limits
        self.mouth = randint(0, self.xf), randint(0, self.yf)
        self.body = [self.mouth]
        self.direction = None
        self.step = None
        self.life = True

    def move(self, mvDir=str, foodposition=tuple):
        if mvDir == 'up' and self.direction != 'down':
            self.step = 0, 1
            self.direction = mvDir
        elif mvDir == 'down' and self.direction != 'up':
            self.step = 0, -1
            self.direction = mvDir
        elif mvDir == 'left' and self.direction != 'right':
            self.step = -1, 0
            self.direction = mvDir
        elif mvDir == 'right' and self.direction != 'left':
            self.step = 1, 0
            self.direction = mvDir
        
        self.mouth = self.mouth[0]+self.step[0], self.mouth[1]+self.step[1]
        self.body.insert(0, self.mouth)
        if not self.eat(foodposition):
            self.body.pop()

    def eat(self, foodPosition=tuple):
        if foodPosition == self.mouth:
            return True
        else:
            return False

    def stillAlive(self):
        x, y = self.mouth
        if x < 0 or x > self.xf or y < 0 or y > self.yf:
            self.life = False
        for points in self.body[1:]:
            if self.mouth == points:
                self.life = False


class Board:
    def __init__(self, xlim=int, ylim=int):
        self.xlimit = xlim - 1
        self.ylimit = ylim - 1
    
    def printPanel(self, snakebody = list, food = tuple, move = 'up'):  # cambiar a curses en el futuro
        p = [[' ' for i in range(self.xlimit+1)] for i in range(self.ylimit+1)]
        
        fx, fy = food
        p[self.ylimit-fy][fx] = '*'
        
        mouth = ''
        if move == 'up': mouth = 'v'
        elif move == 'down': mouth = '^'
        elif move == 'left': mouth = '>'
        elif move == 'right': mouth = '<'
        fx, fy = snakebody[0]
        p[self.ylimit-fy][fx] = mouth
        
        for points in snakebody[1:]:
            x,y = points
            p[self.ylimit-y][x] = 'O'
        print('  .'*(self.xlimit+2))
        for rows in p:
            print('  .', end='')
            for cols in rows:
                print(cols, end=' .')
            print()
        print('\n\n')
    
    def getMove(self):
        key = None
        curses.wrapper()
        screen = curses.initscr()  # inicia la instancia de la nueva pantalla
        curses.noecho()  # no devolver a la pantalla el valor que fue ingresado, ya que 
        curses.cbreak()  # romper la ejecucion solo con un caracter, sin necesitar enter
        screen.keypad(True)

        curses.halfdelay(10)
        key = screen.getch()

        curses.nocbreak()
        screen.keypad(False)

        curses.echo()
        curses.endwin()
    
    def endGame(self):
        print('\t\tthe end\t\t')


class Food:
    def __init__(self, limits=tuple):
        self.__limits = limits
        self.position = None

    def newFood(self, snakeBody=list):
        xf, yf = self.__limits
        self.position = (randint(0, xf), randint(0, yf))
        while(True):
            if self.position in snakeBody:
                self.position = (randint(0, xf), randint(0, yf))
            else:
                break


# object wall
dim = int(input('Inserta la cantidad de filas y columnas: '))
screen = Board(dim, dim)
limits = screen.xlimit, screen.ylimit

# object snake
snake = Snake(limits)

# object food
food = Food(limits)
food.newFood(snake.body)

# define first move (choose the largest distance)
spaceToMove = {}
spaceToMove['right'] = limits[0] - snake.mouth[0]
spaceToMove['left'] = snake.mouth[0]
spaceToMove['up'] = limits[1] - snake.mouth[1]
spaceToMove['down'] = snake.mouth[1]
spaceToMove = sorted(spaceToMove.items(), key=lambda sp: sp[1], reverse=True)
snake.direction = spaceToMove[0][0]
del spaceToMove

# moving snake
while snake.life:
    #imprime la pantalla
    screen.printPanel(snake.body, food.position, snake.direction)
    userKey = ''
    
    keyboard.start_recording()
    sleep(0.5)
    listOfKeys = keyboard.stop_recording()
    
    if len(listOfKeys) > 0:
        userKey = str(listOfKeys[0])[14:][:-6]
    del listOfKeys
    if userKey == 'up' or userKey == 'down' or userKey == 'left' or userKey == 'right':
        snake.move(userKey, food.position)
    else:
        snake.move(snake.direction, food.position)

    if snake.eat(food.position) == True:
        food.newFood(snake.body)
    
    snake.stillAlive()
else:
    print("""
          THE END. SAMUEL IBARRA
          """)

