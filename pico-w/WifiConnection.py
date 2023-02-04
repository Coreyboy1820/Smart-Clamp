import rp2
import network
import ubinascii
import machine
import urequests as requests
import time
import ujson

class WiFiConnection:
    def __init__(self, ssid, pw):
        self.ssid = ssid
        self.pw = pw
        
    def connect(self):
        rp2.country('US')

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
        print('mac = ' + mac)

        wlan.connect(self.ssid, self.pw)

        timeout = 10
        while timeout > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            timeout -= 1
            print('Waiting for connection...')
            time.sleep(1)
          
        def blink_onboard_led(num_blinks):
            led = machine.Pin('LED', machine.Pin.OUT)
            for i in range(num_blinks):
                led.on()
                time.sleep(.2)
                led.off()
                time.sleep(.2)

        wlan_status = wlan.status()
        blink_onboard_led(wlan_status)

        if wlan_status != 3:
            raise RuntimeError('Wi-Fi connection failed')
        else:
            print('Connected')
            status = wlan.ifconfig()
            print('ip = ' + status[0])
            
    def post(self, url, json_data):
        requests.post(url, json=json_data)