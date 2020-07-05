# class PinsArray:
#     import RPi.GPIO as GPIO
#     pos_pin = [24, 22, 18, 16, 23, 21, 19, 15]
#     neg_pin = [40, 38, 36, 32, 37, 35, 33, 31]

#     def __init__(self, dimensions=8, GPIO=GPIO, pos_pin=pos_pin, neg_pin=neg_pin):
#         self.pos_pin = pos_pin
#         self.neg_pin = neg_pin
#         self.GPIO = GPIO
#         self.dimensions = dimensions
#         GPIO.setmode(GPIO.BOARD)

#         for pin in pos_pin:
#             GPIO.setup(pin, GPIO.OUT)
#         for pin in neg_pin:
#             GPIO.setup(pin, GPIO.OUT)

#         for pos in range(self.dimensions):
#             GPIO.output(pos_pin[pos], False)
#             GPIO.output(neg_pin[pos], True)


#     def setLed(self, coordinates=tuple, state=str):
#         xpos, yneg = coordinates
#         if state == 'ON':
#             self.GPIO.output(self.pos_pin[xpos], True)
#             self.GPIO.output(self.neg_pin[yneg], False)
#         elif state == 'OFF':
#             self.GPIO.output(self.pos_pin[xpos], False)
#             self.GPIO.output(self.neg_pin[yneg], True)

#     def finishLeds(self):
#         for pos in range(self.dimensions):
#             self.GPIO.output(self.pos_pin[pos], False)
#             self.GPIO.output(self.neg_pin[pos], False)
from time import sleep

class RPiSimulator:
    pos_pin = [24, 22, 18, 16, 23, 21, 19, 15]
    neg_pin = [40, 38, 36, 32, 37, 35, 33, 31]


    def __init__(self, dimensions=8):
        self.pos_pin = RPiSimulator.pos_pin
        self.neg_pin = RPiSimulator.neg_pin
        self.dimensions = dimensions
        
        # this is the decoder for the rpi representation of the code
        class GPIO:
            def __init__(self, pos_pin=list, neg_pin=list, dim=self.dimensions):
                self.pos_pin = RPiSimulator.pos_pin
                self.neg_pin = RPiSimulator.neg_pin
                self.ledMtx = [["[ ]" for i in range(dim)] for j in range(dim)]
                self.energized = [["[ ]" for i in range(dim)] for j in range(dim)]

            def output(self, outputNumber=int, state=bool):
                if outputNumber in self.pos_pin: # x axis
                    currentPin = self.pos_pin.index(outputNumber)
                    action = 'OneColPos'
                elif outputNumber in self.neg_pin: # y axis
                    currentPin = self.neg_pin.index(outputNumber)
                    action = 'OneRowNeg'

                if action == 'OneRowNeg':
                    for i in range(len(self.ledMtx)):
                        if state == False:
                            self.ledMtx[currentPin][i] = "[O]"
                        elif state == True:
                            self.ledMtx[currentPin][i] = "[ ]"
                if action == 'OneColPos':
                    for i in range(len(self.ledMtx)):
                        if state == True:
                            self.ledMtx[i][currentPin] = "[O]"
                        elif state == False:
                            self.ledMtx[i][currentPin] = "[ ]"
                self.display()
            
            def display(self):
                xon, yon = [], []
                xoff, yoff = [], []
                dim = len(self.ledMtx)
                counton, countoff = 0, 0
                # Search for index where you have the row on
                for y in range(dim):
                    if self.ledMtx[y].count("[O]") == dim:
                        yon.append(y)
                    elif self.ledMtx[y].count("[ ]") == dim:
                        yoff.append(y)
                    # search in cols
                    for x in range(dim):
                        if self.ledMtx[x][y] == "[O]":
                            counton += 1
                        elif self.ledMtx[x][y] == "[ ]":
                            countoff += 1
                    if counton == dim:
                        xon.append(y)
                    elif countoff == dim:
                        xoff.append(y)
                    countoff = 0
                    counton = 0

                for row in yon:
                    for col in xon:
                        self.energized[row][col] = "[O]"
                for row in yoff:
                    for col in xoff:
                        self.energized[row][col] = "[ ]"

                for row in reversed(self.energized):
                    for led in row:
                        print(f"{led}", end='')
                    print()
                print('\n\n')

        self.GPIO = GPIO(self.pos_pin, self.neg_pin)
        
# esto se debe descomentar cuando estes en la rpi
        # for pos in range(self.dimensions):
        #     self.GPIO.output(self.pos_pin[pos], False)
        #     self.GPIO.output(self.neg_pin[pos], True)

    def setLed(self, coordinates=tuple, state=str):
        xpos, yneg = coordinates
        if state == 'ON':
            self.GPIO.output(self.pos_pin[xpos], True)
            self.GPIO.output(self.neg_pin[yneg], False)
        elif state == 'OFF':
            self.GPIO.output(self.pos_pin[xpos], False)
            self.GPIO.output(self.neg_pin[yneg], True)

    def finishLeds(self):
        for pos in range(self.dimensions):
            self.GPIO.output(self.pos_pin[pos], False)
            self.GPIO.output(self.neg_pin[pos], False)

IO = RPiSimulator() #funciona perfecto
pos1 = (1,2)
pos2 = (3,5)

for i in range(5):
    IO.setLed(pos1, 'ON')
    IO.setLed(pos2, 'ON')
    sleep(1)
    IO.setLed(pos1, 'OFF')
    IO.setLed(pos2, 'OFF')
    sleep(1)

#descomentar
# IO.finishLeds()
