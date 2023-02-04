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