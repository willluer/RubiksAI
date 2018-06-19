from Cube import Cube
import numpy as np
from util import reverse
import pygame

cube = Cube()
print()
# cube.back.state = np.array([['A','C','D'],['E','F','K'],['H','I','J']])
# cube.printCube()
# cube.drawCube()
print(cube.isGoalState())
# movesMade = cube.shuffle(100,show=True)
# cube.drawCube()

# cube.move('RUru'*6)
# cube.drawCube()

# reversedMoves = reverse(movesMade)
#
cube.move("urfuRURdDbURLDDRblrbFLDfRDlbFUDldr")
print()
print(cube.isGoalState())
cube.move("URuufDLrFlDDuDlbUrBbRFBdUfBruFruuRLUfrRDLUUFuffFbuDfBlFLFUfDlFUdbUuBDufLdFuflfLbFdUBfFFUfuuldrRFulrUURfURbFuDbfrBbRuBLdUddLfRldFUUruRDLdufBLdrFdlfBRLBrddlruBdDrurUFRU",show=True)
print()
print(cube.isGoalState())
cube.drawCube()
print()
# cube.drawCube()

# cube.printCube()
# print("Goal State: ",cube.isGoalState())
# cube.move("UllLLu")
# cube.printCube()

# RRLUR
# rulrr
# cube.move('D')
# cube.printCube()

# print()
# cube.move('u')
# cube.printCube()
# print()
# cube.move('r')
# cube.printCube()
# print()
# cube.move('u')
# cube.printCube()
# print()
# cube.move('u')
# cube.printCube()
# print()
