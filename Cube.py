from Face import Face
import numpy as np
import random
import pygame
import time
class Cube:
    #Cube state will be an array of [Top Face, Left Face, Front, Right, Down, Back]
    def __init__(self):
            self.top,self.left,self.front,self.right,self.down,self.back = self.initCube()
            pygame.init()
            self.myDisplay=pygame.display.set_mode((451,601))


    def isGoalState(self):
        count=0
        for i in self.top.state.flatten():
            count += 1
            if i[0] != 'Y' and i[2] != str(count):
                return False
        count=0
        for i in self.front.state.flatten():
            count += 1
            if i[0] != 'B' and i[2] != str(count):
                return False
        count=0
        for i in self.left.state.flatten():
            count += 1
            if i[0] != 'O' and i[2] != str(count):
                return False
        count=0
        for i in self.right.state.flatten():
            count += 1
            if i[0] != 'R' and i[2] != str(count):
                return False
        count=0
        for i in self.down.state.flatten():
            count += 1
            if i[0] != 'W' and i[2] != str(count):
                return False
        count=0
        for i in self.back.state.flatten():
            count += 1
            if i[0] != 'G' and i[2] != str(count):
                return False
        return True

    def moveF(self,direction='cw'): # Move front face default clockwise
        leftToMove = np.copy(self.left.state[:,2])
        topToMove = np.copy(self.top.state[2,:])
        rightToMove = np.copy(self.right.state[:,0])
        downToMove = np.copy(self.down.state[0,:])

        if direction == 'cw':
            #rotate front face array
            # print("Front CW")
            self.front.state = np.array(list(zip(*self.front.state[::-1])))
            self.left.state[:,2] = downToMove
            self.top.state[2,:] = leftToMove
            self.right.state[:,0] = topToMove
            self.down.state[0,:] = rightToMove

        elif direction == 'ccw':
            # print("Front CCW")
            rotated = list(zip(*self.front.state[::-1]))
            rotated = list(zip(*rotated[::-1]))
            self.front.state = np.array(list(zip(*rotated[::-1])))
            self.left.state[:,2] = topToMove
            self.top.state[2,:] = rightToMove
            self.right.state[:,0] = downToMove
            self.down.state[0,:] = leftToMove

    def moveL(self,direction='cw'): # Move left face
        topToMove = np.copy(self.top.state[:,0])
        backToMove = np.copy(self.back.state[:,0])
        frontToMove = np.copy(self.front.state[:,0])
        downToMove = np.copy(self.down.state[:,0])

        if direction == 'cw':
            #rotate front face array
            # print("Left CW")
            self.left.state = np.array(list(zip(*self.left.state[::-1])))
            self.top.state[:,0] = np.flip(backToMove,0)
            self.back.state[:,0] = downToMove
            self.front.state[:,0] = topToMove
            self.down.state[:,0] = frontToMove

        elif direction == 'ccw':
            # print("Left CCW")
            rotated = list(zip(*self.left.state[::-1]))
            rotated = list(zip(*rotated[::-1]))
            self.left.state = np.array(list(zip(*rotated[::-1])))
            self.top.state[:,0] = frontToMove
            self.back.state[:,0] = np.flip(topToMove,0)
            self.front.state[:,0] = downToMove
            self.down.state[:,0] = backToMove

    def moveR(self,direction='cw'): # Move right face
        topToMove = np.copy(self.top.state[:,2])
        backToMove = np.copy(self.back.state[:,2])
        frontToMove = np.copy(self.front.state[:,2])
        downToMove = np.copy(self.down.state[:,2])

        if direction == 'cw':
            #rotate front face array
            # print("Right CW")
            self.right.state = np.array(list(zip(*self.right.state[::-1])))
            self.top.state[:,2] = frontToMove
            self.back.state[:,2] = topToMove
            self.front.state[:,2] = downToMove
            self.down.state[:,2] = backToMove

        elif direction == 'ccw':
            # print("Right CCW")
            rotated = list(zip(*self.right.state[::-1]))
            rotated = list(zip(*rotated[::-1]))
            self.right.state = np.array(list(zip(*rotated[::-1])))
            self.top.state[:,2] = backToMove
            self.back.state[:,2] = downToMove
            self.front.state[:,2] = topToMove
            self.down.state[:,2] = frontToMove


    def moveB(self,direction='cw'): # Move back face

        leftToMove = np.copy(self.left.state[:,0])
        topToMove = np.copy(self.top.state[0,:])
        rightToMove = np.copy(self.right.state[:,2])
        downToMove = np.copy(self.down.state[:,2])

        if direction == 'cw':
            #rotate front face array
            # print("Back CW")
            self.back.state = np.array(list(zip(*self.back.state[::-1])))
            self.left.state[:,0] = topToMove
            self.top.state[0,:] = rightToMove
            self.right.state[:,2] = downToMove
            self.down.state[:,2] = leftToMove

        elif direction == 'ccw':
            # print("Back CCW")
            rotated = list(zip(*self.back.state[::-1]))
            rotated = list(zip(*rotated[::-1]))
            self.back.state = np.array(list(zip(*rotated[::-1])))
            self.left.state[:,0] = downToMove
            self.top.state[0,:] = leftToMove
            self.right.state[:,2] = topToMove
            self.down.state[:,2] = rightToMove


    def moveU(self,direction='cw'): # Move top face
        leftToMove = np.copy(self.left.state[0,:])
        backToMove = np.copy(self.back.state[2,:])
        frontToMove = np.copy(self.front.state[0,:])
        rightToMove = np.copy(self.right.state[0,:])

        if direction == 'cw':
            #rotate front face array
            # print("Top CW")
            self.top.state = np.array(list(zip(*self.top.state[::-1])))
            self.left.state[0,:] = frontToMove
            self.back.state[2,:] = np.flip(leftToMove,0)
            self.front.state[0,:] = rightToMove
            self.right.state[0,:] = np.flip(backToMove,0)

        elif direction == 'ccw':
            # print("Top CCW")
            rotated = list(zip(*self.top.state[::-1]))
            rotated = list(zip(*rotated[::-1]))
            self.top.state = np.array(list(zip(*rotated[::-1])))
            self.left.state[0,:] = np.flip(backToMove,0)
            self.back.state[2,:] = np.flip(rightToMove,0)
            self.front.state[0,:] = leftToMove
            self.right.state[0,:] = frontToMove

    def moveD(self,direction='cw'): # Move bottom face
        leftToMove = np.copy(self.left.state[2,:])
        backToMove = np.copy(self.back.state[0,:])
        frontToMove = np.copy(self.front.state[2,:])
        rightToMove = np.copy(self.right.state[2,:])

        if direction == 'cw':
            #rotate front face array
            # print("Down CW")
            self.down.state = np.array(list(zip(*self.down.state[::-1])))
            self.left.state[2,:] = np.flip(backToMove,0)
            self.back.state[0,:] = np.flip(rightToMove,0)
            self.front.state[2,:] = leftToMove
            self.right.state[2,:] = frontToMove

        elif direction == 'ccw':
            # print("Down CCW")
            rotated = list(zip(*self.down.state[::-1]))
            rotated = list(zip(*rotated[::-1]))
            self.down.state = np.array(list(zip(*rotated[::-1])))
            self.left.state[2,:] = frontToMove
            self.back.state[0,:] = np.flip(leftToMove,0)
            self.front.state[2,:] = rightToMove
            self.right.state[2,:] = np.flip(backToMove,0)
    def shuffle(self,n,show=False): # Shuffle
        choices = 'RULDBFruldbf'
        choices = [letter for letter in choices]
        moves = ""
        for i in range(n):
            moves += random.choice(choices)
        self.move(moves,show)
        return moves
    # def solve(self): # Solve the cube
    def move(self,moves,show=False): # Take in array of moves to make: e.g. [l,f,b,u,d,d,d,l,]
        for move in moves:
            print(move,end="")
            if show:
                self.drawCube()
            # self.printCube()
            if move == 'R':
                self.moveR()
            elif move == 'r':
                self.moveR('ccw')

            elif move == 'U':
                self.moveU()
            elif move == 'u':
                self.moveU('ccw')

            elif move == 'L':
                self.moveL()
            elif move == 'l':
                self.moveL('ccw')

            elif move == 'B':
                self.moveB()
            elif move == 'b':
                self.moveB('ccw')

            elif move == 'D':
                self.moveD()
            elif move == 'd':
                self.moveD('ccw')

            elif move == 'F':
                self.moveF()
            elif move == 'f':
                self.moveF('ccw')

    def stack(self):
        emptyFace= Face(' ')
        row1 = np.hstack((emptyFace.state,self.top.state,emptyFace.state))
        row2 = np.hstack((self.left.state,self.front.state,self.right.state))
        row3 = np.hstack((emptyFace.state,self.down.state,emptyFace.state))
        row4 = np.hstack((emptyFace.state,self.back.state,emptyFace.state))
        joinedCube = np.vstack((row1,row2,row3,row4))
        return joinedCube

    def drawCube(self):
        joinedCube = self.stack()
        pygame.init()
        pygame.display.set_caption("Rubiks Cube")
        W=(255,255,255)
        B=(0,0,255)
        R=(255,0,0)
        O=(255,140,0)
        Y=(255,255,128)
        G=(0,255,0)
        black=(0,0,0)
        colorDict = {'W':(255,255,255),'B':(0,0,255),'R':(255,0,0),'O':(255,140,0),
                     'O':(255,140,0),'Y':(255,255,128),'G':(0,255,0)}
        # myDisplay.fill(WHITE)
        rows,cols = np.shape(joinedCube)

        startTime = time.time()
        showTime = 3.0 if self.isGoalState() else 0.005

        while time.time() < startTime+showTime:
            for event in pygame.event.get():
                if event.type==pygame.quit:
                    pygame.quit()
                    sys.exit()

            for i in range(rows):
                for j in range(cols):
                    color = joinedCube[i,j]
                    color = color[0]
                    if color != " ":
                        pygame.draw.rect(self.myDisplay,colorDict[color],(j*50,i*50,50,50))
            for xCoord in np.linspace(0,400,9):
                pygame.draw.line(self.myDisplay,black,(xCoord,0),(xCoord,600),2)
            for yCoord in np.linspace(0,600,13):
                pygame.draw.line(self.myDisplay,black,(0,yCoord),(450,yCoord),2)


            pygame.display.update()
        # pygame.time.delay(5000)

    def printCube(self):
        joinedCube = self.stack()
        for row in joinedCube:
            print(row)
            # for col in row:
            #     print(col,end="")
            # print('\n')
        # print(joinedCube)

    def initCube(self):
        return Face('Y'),Face('O'),Face('B'),Face('R'),Face('W'),Face('G')
