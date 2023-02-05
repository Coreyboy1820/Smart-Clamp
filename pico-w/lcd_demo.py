from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from button import Button
from rotary_display import RotaryDisplay

id = 0
sda = Pin(8)
scl = Pin(9)
i2c = I2C(id=id, scl=scl, sda=sda)

# Screen Variables
width = 128
height = 64

# create the display
oled = SSD1306_I2C(width=width, height=height, i2c=i2c)
oled.init_display()

# Setup the Rotary Encoder
upButton = Button(26)
downButton = Button(28)
selectButton  = Button(2)

display = RotaryDisplay(oled, upButton, downButton, selectButton)
while True:
    
    display.handleSelect()
    display.displayMenu()
    display.handleCursor()
    sleep(.1)
