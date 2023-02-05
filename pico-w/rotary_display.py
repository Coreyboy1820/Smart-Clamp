# Rotary Menu
# Kevin McAleer
# May 2021

from machine import Pin, I2C
from os import listdir
from ssd1306 import SSD1306_I2C
from time import sleep
from button import Button
from Timers import Timer

class RotaryDisplay:

    def __init__(self, oled, upButton, downButton, selectButton, backButton):
        self.oled = oled
        self.upButton = upButton
        self.downButton = downButton
        self.selectButton = selectButton
        self.backButton = backButton
        self.exerciseList = ["Bicep curls", "Tricep extensions", "Overhead press", "Bent over rows", "lateral raises"]
        self.exerciesIndex = 0
        self.weight = 0
        self.line_height = 10
        self.screen_offset = 2
        self.total_lines = 3
        self.shift = 0
        self.highlight = 1
        self.width = 128
        self.height = 64
        self.startSet = False
        self.startRest = False
        self.timer = Timer(0)
        self.reps = 0

    def launch(self):
        """ Launch the Python script <filename> """
        # clear the screen
        self.oled.fill_rect(0,0,self.width,self.height,0)
        self.oled.text("Launching", 1, 10)
        self.oled.show()

    def displayMenu(self):
        if self.startRest:
            self.highlight = 3
            self.handleStartSet()
        elif self.startSet:
            self.highlight = 3
            self.handleStartRest()
        else:
            self.handleMainMenu()

    def handleMainMenu(self):
        item = 1
        # clear the display
        self.oled.fill_rect(0,0,self.width,self.height,0)

        # the second parameter in the handleHighlight function is the order of which they are placed in the device
        self.handleHighlight(self.exerciseList[self.exerciesIndex], 1)
        self.handleHighlight(self.weight, 2)
        self.handleHighlight("Start Rest", 3)
        self.handleHighlight("Start Set", 4)
    
    def handleStartRest(self):
        self.timer.startTimer()
        # clear the screen
        self.oled.fill_rect(0,0,self.width,self.height,0)
        self.handleHighlight(self.timer.getTimeElapsed(), 1)
        self.handleHighlight(self.reps, 2)
        self.handleHighlight("stop", 3)

    def handleStartSet(self):
        self.timer.startTimer()
        self.oled.fill_rect(0,0,self.width,self.height,0)
        

    def handleHighlight(self, item, number):
        if self.highlight == number:
            self.oled.fill_rect(0,(number-1)*self.line_height+self.screen_offset, self.width,self.line_height,1)
            self.oled.text(">",0, (number-1)*self.line_height+self.screen_offset,0)
            self.oled.text(item, 10, (number-1)*self.line_height+self.screen_offset,0)
        else:
            self.oled.text(item, 10, (number-1)*self.line_height+self.screen_offset,1)
        self.oled.show()

    def handleCursor(self):
        # move up
        if not self.upButton.read():
            if self.highlight > 1:
                self.highlight -=1
            else:
                if self.shift > 0:
                    self.shift -= 1
            self.displayMenu()
        print(self.highlight)
        # move down
        if self.downButton.read():
            if self.highlight < self.total_lines:
                self.highlight += 1
            else: 
                if self.shift+self.total_lines < len(self.selectionMenu):
                    self.shift += 1
            self.displayMenu()
        
    def handleSelect(self):
        if self.startRest:
            # handle the rest selection category
            self.backButton
        elif self.startSet:
            # handles the set selection category
            self.backButton
        else:
            # this should only happen if you are on the home screen.
            self.backButton