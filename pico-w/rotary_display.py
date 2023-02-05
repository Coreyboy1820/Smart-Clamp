from machine import Pin, I2C
from os import listdir
from ssd1306 import SSD1306_I2C
from time import sleep
from button import Button
from Timers import Timer

class RotaryDisplay:

    def __init__(self, oled, upButton, downButton, selectButton):
        self.oled = oled
        self.upButton = upButton
        self.downButton = downButton
        self.selectButton = selectButton
        self.exerciseList = ["Bicep curls", "Bent over rows", "Squats", "Bench Press"]
        self.exerciseIndex = 0
        self.weight = 0
        self.line_height = 10
        self.screen_offset = 6
        self.total_lines = 4
        self.shift = 0
        self.highlight = 1
        self.lastHighlight = 1
        self.width = 128
        self.height = 64
        self.startSet = False
        self.startRest = False
        self.timer = Timer(0)
        self.reps = 0
        self.selectPressed = False
        self.lastReps = 0
        self.lastTime = 0.0
        self.lastWeight = 0.0

    def launch(self):
        """ Launch the Python script <filename> """
        # clear the screen
        self.oled.fill_rect(0,0,self.width,self.height,0)
        self.oled.text("Launching", 1, 10)
        self.oled.show()

    def displayMenu(self):
        if self.startRest:
            self.highlight = 3
            self.handleStartRest()
        elif self.startSet:
            self.highlight = 3
            self.handleStartSet()
        else:
            self.handleMainMenu()

    def handleMainMenu(self):
        item = 1
        # clear the display
        self.oled.fill_rect(0,0,self.width,self.height,0)

        # the second parameter in the handleHighlight function is the order of which they are placed in the device
        self.handleHighlight(self.exerciseList[self.exerciseIndex], 1)
        self.handleHighlight(f"Weight: {self.weight}", 2)
        self.handleHighlight("Start Rest", 3)
        self.handleHighlight("Start Set", 4)
    
    def handleStartRest(self):
        if not self.timer.isRunning():
            self.timer.startTimer()
        # clear the screen
        self.oled.fill_rect(0,0,self.width,self.height,0)
        self.handleHighlight(f"      {self.timer.getTimeElapsed()}", 1)
        self.handleHighlight(f"Reps: {self.lastReps}", 2)
        self.handleHighlight("stop", 3)

    def handleStartSet(self):
        if not self.timer.isRunning():
            self.timer.startTimer()
        self.oled.fill_rect(0,0,self.width,self.height,0)
        self.handleHighlight(f"      {self.timer.getTimeElapsed()}", 1)
        self.handleHighlight(f"Reps: {self.reps}", 2)
        self.handleHighlight("Stop", 3)

        

    def handleHighlight(self, item, number):
        if self.highlight == number:
            self.oled.fill_rect(0,(number-1)*self.line_height+self.screen_offset, self.width,self.line_height,1)
            self.oled.text(">",0, (number-1)*self.line_height+self.screen_offset,0)
            self.oled.text(item, 10, (number-1)*self.line_height+self.screen_offset,0)
        else:
            self.oled.text(item, 10, (number-1)*self.line_height+self.screen_offset,1)
        self.oled.show()

    def handleCursor(self):
        if self.selectPressed:
            # the only time selectpressed is high is when 
            if self.highlight == 1:
                if self.upButton.read():
                    self.exerciseIndex = (self.exerciseIndex + 1) % 4
                if self.downButton.read():
                    if self.exerciseIndex > 0:
                        self.exerciseIndex -= 1
                    else:
                        self.exerciseIndex = 3
            elif self.highlight == 2:
                if self.upButton.read():
                    self.weight += 2.5
                if self.downButton.read():
                    if self.weight == 0:
                        self.weight = 0
                    else:
                        self.weight -= 2.5

        else:
            # move up
            if self.upButton.read():
                if self.highlight > 1:
                    self.lastHightLight = self.highlight
                    self.highlight -=1
                else:
                    self.lastHighlight = self.highlight
                    self.highlight = 4
                self.displayMenu()
            # move down
            if self.downButton.read():
                if self.highlight < self.total_lines:
                    self.lastHighlight = self.highlight
                    self.highlight += 1
                else:
                    self.lastHighlight = self.highlight
                    self.highlight = 1
                self.displayMenu()
        
    def handleSelect(self):
        if self.selectButton.read():
            if self.startRest:
                # handle the rest selection category
                self.startRest = False
                self.timer.stopTimer()
            elif self.startSet:
                # handles the set selection category
                self.lastTime = self.timer.getTimeElapsed()
                self.lastWeight = self.weight
                self.weight = 0
                self.lastReps = self.reps
                self.timer.stopTimer()
                self.startSet = False
            else:
                # this should only happen if you are on the home screen.
                if (self.highlight == 1 or self.highlight == 2) and not self.selectPressed:
                    self.selectPressed = True
                elif (self.highlight == 1 or self.highlight==2) and self.selectPressed:
                    self.selectPressed = False
                elif self.highlight == 3:
                    self.startRest = True
                elif self.highlight == 4:
                    self.startSet = True