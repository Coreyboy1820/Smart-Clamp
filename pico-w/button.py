from machine import Pin

class Button:
    def __init__(self, pinNum):
        self.pin = Pin(pinNum, Pin.IN, Pin.PULL_UP)
    
    def read(self):
        return self.pin.value()
