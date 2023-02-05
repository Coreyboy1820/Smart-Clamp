# Rotary Menu
# Kevin McAleer
# May 2021

from machine import Pin, I2C
from os import listdir
from ssd1306 import SSD1306_I2C
from time import sleep
from button import Button

class RotaryDisplay:

    def __init__(self, oled, menu, upButton, downButton, selectButton, backButton):
        self.oled = oled
        self.upButton = upButton
        self.downButton = downButton
        self.selectButton = selectButton
        self.backButton = backButton
        self.menu = menu
        self.list_length = len(self.menu)
        self.item = 1
        self.line = 1
        self.line_height = 10
        self.screen_offset = 2
        self.total_lines = 6
        self.shift = 0
        self.highlight = 1
        self.width = 128
        self.height = 64

    def launch(self):
        """ Launch the Python script <filename> """
        # clear the screen
        self.oled.fill_rect(0,0,self.width,self.height,0)
        self.oled.text("Launching", 1, 60)
        self.oled.show()

    def displayMenu(self):
        """ Shows the menu on the screen"""

        # clear the display
        self.oled.fill_rect(0,0,self.width,self.height,0)

        # Shift the list of files so that it shows on the display
        short_list = self.menu[self.shift : self.shift + self.total_lines]

        for item in short_list:
            if self.highlight == self.line:
                self.oled.fill_rect(0,(self.line-1)*self.line_height+self.screen_offset, self.width,self.line_height,1)
                self.oled.text(">",0, (self.line-1)*self.line_height,0)
                self.oled.text(item, 10, (self.line-1)*self.line_height+self.screen_offset,0)
                self.oled.show()
            else:
                self.oled.text(item, 10, (self.line-1)*self.line_height+self.screen_offset,1)
                self.oled.show()
            self.line += 1 
        self.oled.show()

    def handleCursor(self):
        # move up
        if self.upButton.read():
            if self.highlight > 1:
                self.highlight -=1
            else:
                if self.shift > 0:
                    self.shift -= 1
        if self.downButton.read():
            if self.highlight < self.total_lines:
                self.highlight += 1
            else: 
                if self.shift+self.total_lines < self.list_length:
                    self.shift += 1
        


#while True:
        
    # Check for button pressed
    #if button_pin.value() == False and not button_down:
    #    button_down = True

   #     print("Launching", menu[highlight-1+shift]) 

        # execute script
        # launch(menu[(highlight-1) + shift])
        
  #      print("Returned from launch")

    # Decbounce button
 #   if button_pin.value() == True and button_down:
#        button_down = False