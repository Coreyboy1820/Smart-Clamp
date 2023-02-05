from machine import Pin

class pot:
    def __init__(self, adc):
        self.adc = adc

    def read(self):
        self.adc.value()