from imu import MPU6050
import time

class Workouts:
    def __init__(self, i2c):
        self.i2c = i2c
        self.imu = MPU6050(self.i2c)
        self.weight_state = 'down'
        self.reps = 0
        
    def Update(self):
        ax=round(self.imu.accel.x,4)
        ay=round(self.imu.accel.y,4)
        az=round(self.imu.accel.z,4)
        time.sleep(0.2)
        return ax, ay, az
        
    def BicepCurls(self):
        accel = self.Update()
        if (accel[2] < 0.5 and accel[0] > -0.7 and self.weight_state != 'up'):
            self.weight_state = 'up'
        elif(accel[2] > 0.7 and accel[0] < 0.5 and self.weight_state == 'up'):
            self.weight_state = 'down'
            self.reps+=1
        return self.reps
    
    def BenchPress(self):
        accel = self.Update()
        if (accel[2] < 0.5 and accel[0] > -0.7 and self.weight_state != 'up'):
            self.weight_state = 'up'
        elif(accel[2] > 0.7 and accel[0] < 0.5 and self.weight_state == 'up'):
            self.weight_state = 'down'
            self.reps+=1
        return self.reps
    
    def BentOverRows(self):
        accel = self.Update()
        if (accel[2] < 0.7 and accel[0] > -0.5 and self.weight_state != 'up'):
            self.weight_state = 'up'
        elif(accel[2] > 0.95 and accel[0] < 0.2 and self.weight_state == 'up'):
            self.weight_state = 'down'
            self.reps+=1
        return self.reps
    
    def Squats(self):
        accel = self.Update()
        if (accel[2] < 0.65 and self.weight_state != 'up'):
            self.weight_state = 'up'
        elif(accel[2] < 0.65 and self.weight_state == 'up'):
            self.weight_state = 'down'
            self.reps+=1
        return self.reps
    
    def BenchPress(self):
        accel = self.Update()
        if (accel[2] < 0.65 and self.weight_state != 'up'):
            self.weight_state = 'up'
        elif(accel[2] > 0.65 and self.weight_state == 'up'):
            self.weight_state = 'down'
            self.reps+=1
        return self.reps