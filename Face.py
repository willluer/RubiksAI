import numpy as np
class Face:
    def __init__(self,symbol):
        self.state = self.initFace(symbol)

    def printFace(self):
        print(self.state)
        # for row in self.state:
        #     for col in row:
        #         print(col)


    def initFace(self,symbol):
        i = 0
        if symbol != ' ':
            face = [[symbol+'-1',symbol+'-2',symbol+'-3'],
                    [symbol+'-4',symbol+'-5',symbol+'-6'],
                    [symbol+'-7',symbol+'-8',symbol+'-9']]
            return np.array(face)
        else:
            return np.array([['   ' for i in range(3)] for j in range(3)])
