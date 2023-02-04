import Button.py

def buttonDemo():
    button = Button(2)
    while(True):
        time.sleep(.5)
        print(button.read())

buttonDemo()