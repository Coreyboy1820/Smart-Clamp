from rotary_display import RotaryDisplay
from Timers import Timer
from WifiConnection import WiFiConnection
import Workouts
from time import sleep
from button import Button
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


imu_i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
oled_i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
# switch to oled_I2c = 0 sda = 8 scl = 9 when using breadboard | I2c = 1 sda = 18 scl = 19 when using protoboard
json = {"username": "user1","exercise": "deadlift","reps": 0,"weight": 0,"duration": 0}

# Screen Variables
width = 128
height = 64
post = False

# create the display
oled = SSD1306_I2C(width=width, height=height, i2c=oled_i2c)
oled.init_display()

# Setup the Rotary Encoder
upButton = Button(26)
downButton = Button(28)
selectButton  = Button(22)

display = RotaryDisplay(oled, upButton, downButton, selectButton)
workout = Workouts.Workouts(imu_i2c)
connection = WiFiConnection('SJSU Robotics 2.4GHz', 'R0Bot1cs3250')
connection.connect()

while True:
    display.handleSelect()
    display.displayMenu()
    display.handleCursor()
    sleep(.01)
    current_exercise = display.exerciseList[display.exerciseIndex]
    
    while (display.startSet):
        if (current_exercise == "Bicep curls"):
            display.reps = workout.BicepCurls()
        elif (current_exercise == "Overhead press"):
            display.reps = workout.OverheadPress()
        elif (current_exercise == "Bent over rows"):
            display.reps = workout.BentOverRows()
        elif (current_exercise == "Squats"):
            display.reps = workout.Squats()
        elif (current_exercise == "Bench Press"):
            display.reps = workout.BenchPress()
        
        display.handleSelect()
        display.displayMenu()
        display.handleCursor()
        post = True
        sleep(.01)
    
    if (post):
        workout.reps = 0
        display.reps = 0
        json['weight'] = display.lastWeight
        json['reps'] = display.lastReps
        json['exercise'] = current_exercise
        json['duration'] = display.lastTime
        connection.post('http://13.56.207.97:5000/workouts', json)
        post = False