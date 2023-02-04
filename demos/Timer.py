def timerDemo():
    timer = Timer(10)
    while(True):
        time.sleep(.01)
        if not timer.isRunning():
            print("we have started the timer")
            timer.startTimer()

        #logic
        print(timer.getTimeElapsed())
        
        if timer.maxTimeReached():
            print("Max Time Reached")
    
timerDemo()