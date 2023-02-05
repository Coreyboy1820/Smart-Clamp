from machine import Pin, ADC

adc = ADC(Pin(27, mode=Pin.IN))

print(adc.read())