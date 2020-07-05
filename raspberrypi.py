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
        self.ledMtx = [["[ ]" for i in range(self.dimensions)] for j in range(self.dimensions)]
        #for simulator
        # this is the decoder for the rpi representation of the code
        class GPIO:
            def __init__(self, pos_pin, neg_pin, ledMtx):
                self.pos_pin = RPiSimulator.pos_pin
                self.neg_pin = RPiSimulator.neg_pin
                self.ledMtx = ledMtx

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
                
                
                for row in self.ledMtx:
                    for led in row:
                        print(f"{led}", end='')
                    print()
                print('\n\n')

        self.GPIO = GPIO(self.pos_pin, self.neg_pin, self.ledMtx)

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

IO = RPiSimulator()
position = (1,2)

for i in range(5):
    IO.setLed(position, 'ON')
    sleep(1)
    IO.setLed(position, 'OFF')
    sleep(1)

# IO.finishLeds()
