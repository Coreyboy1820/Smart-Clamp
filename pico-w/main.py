from rotary_display import RotaryDisplay
from Timers import Timer
from WifiConnection import WiFiConnection
import Workouts
from time import sleep
from button import Button
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


imu_i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
oled_i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
json = {"username": "user1","exercise": "deadlift","reps": 0,"weight": 0,"duration": 0}

# Screen Variables
width = 128
height = 64

# create the display
oled = SSD1306_I2C(width=width, height=height, i2c=oled_i2c)
oled.init_display()

# Setup the Rotary Encoder
upButton = Button(26)
downButton = Button(28)
selectButton  = Button(2)

display = RotaryDisplay(oled, upButton, downButton, selectButton)
workout = Workouts.Workouts(10, 10, imu_i2c)
connection = WiFiConnection('Turbo', 'sfcastro')

while True:
    display.handleSelect()
    display.displayMenu()
    display.handleCursor()
    sleep(.1)
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
        sleep(.1)
    
    if (display.startSet == False):
        workout.reps = 0
        display.reps = 0
        json['weight'] = display.lastWeight
        json['reps'] = display.lastReps
        json['exercise'] = current_exercise
        json['duration'] = display.lastTime
        connection.post(json)