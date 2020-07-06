# trying 2
class You:
    J = 'called from class'

    @classmethod
    def __init__(cls, nums=1):
        print(cls.J)
        cls.J += ' plus one'

You()
You()
You()
You()


lst = [1,2,3,'a', 'km']

print(lst.index(3))

class LedPrint:
    def __init__(self, dimensions=8):
        self.dimensions = dimensions
        from time import sleep
        self.sleep = sleep

    def makeParts(self, snakemouth=tuple, snakebody=list):
        lastPoint = snakemouth
        bodyparts = [[]]
        partNumber = 0
        if snakebody[1][0] == lastPoint[0]:
            axis = 'X'
        elif snakebody[1][1] == lastPoint[1]:
            axis = 'Y'
        for point in snakebody:
            if point[0] == lastPoint[0] and axis == 'X':
                bodyparts[partNumber].append(point)
            elif point[1] == lastPoint[1] and axis == 'Y':
                bodyparts[partNumber].append(point)
            else:
                partNumber += 1
                bodyparts.append([])
                bodyparts[partNumber].append(point)
                if axis == 'Y': axis = 'X'
                elif axis == 'X': axis = 'Y'
            lastPoint = point
        return bodyparts

mouth = (4,8)
body = [
    (4,8),
    (4,9),
    (4,10),
    (4,11),
    (5,11),
    (6,11),
    (6,10),
    (6,9),
    (6,8),
    (5,8)
]
io = LedPrint()
print(io.makeParts(mouth, body))