from imu import MPU6050
import time
from machine import Pin, I2C

class Workouts:
    def __init__(self, timer, max_reps):
        self.i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
        self.imu = MPU6050(self.i2c)
        self.timer = timer
        self.weight_state = 'down'
        self.reps = 0
        self.max_reps = max_reps
        self.rep_distance = []
        
    def RepType(self, rep_type):
        if (rep_type == 'FULL'):
            self.rep_distance = [0.5, -0.7, 0.7, 0.5]
        elif(rep_type == 'HALF')
            self.rep_distance = [0.25, -0.35, 0.35, 0.25]
        
    def Update(self):
        ax=round(self.imu.accel.x,4)
        ay=round(self.imu.accel.y,4)
        az=round(self.imu.accel.z,4)
        time.sleep(0.2)
        return ax, ay, az
        
    def BicepCurls(self):
        accel = self.Update()
        if (accel[2] < self.rep_distance[0] and accel[0] > self.rep_distance[1] and self.weight_state != 'up'):
            self.weight_state = 'up'
        elif(accel[2] > self.rep_distance[2] and accel[0] < self.rep_distance[3] and self.weight_state == 'up'):
            self.weight_state = 'down'
            self.reps+=1
        return self.reps