import time
class Timer:
    def __init__(self, maxTime):
        self.startTime = 0
        self.maxTime = maxTime
        
    # if called it will restart timer
    def startTimer(self):
        self.startTime = time.time()
        
    def stopTimer(self):
        self.startTime = 0
        
    def getTimeElapsed(self):
        timeElapsed = round((time.time()-self.startTime), 2)
        return timeElapsed
        
    def isRunning(self):
        if self.startTime == 0:
            return False
        return True

    def setMaxTime(self, maxTime):
        self.maxTime = maxTime

    def maxTimeReached(self):
        if int(self.getTimeElapsed()) == self.maxTime:
            self.stopTimer()
            return True
        return False
        
# def main():
#     timer = Timer(10)
#     while(True):
#         time.sleep(.01)
#         if not timer.isRunning():
#             print("we have started the timer")
#             timer.startTimer()
        
        
#         #logic
#         print(timer.getTimeElapsed())
        
#         if timer.maxTimeReached():
#             print("Max Time Reached")
    
# main()
    