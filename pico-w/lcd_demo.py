from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from button import Button
from rotary_display import RotaryDisplay

id = 0
sda = Pin(0)
scl = Pin(1)
i2c = I2C(id=id, scl=scl, sda=sda)

# Screen Variables
width = 128
height = 64

# create the display
oled = SSD1306_I2C(width=width, height=height, i2c=i2c)
oled.init_display()

# Setup the Rotary Encoder
upButton = Button(3)
downButton = Button(2)
selectButton  = Button(4)
backButton = Button(5)
menu = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test10"]

display = RotaryDisplay(oled, menu, upButton, downButton, selectButton, backButton)
while True:
    display.displayMenu()
    display.handleCursor()
    sleep(.5)
