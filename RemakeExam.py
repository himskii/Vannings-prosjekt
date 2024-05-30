from time import sleep
import RPi.GPIO as GPIO
import time


timestamp = time.time()
date = time.ctime(timestamp)


GPIO.setmode(GPIO.BCM)


relay = 17
sensor = 27
switch = 22



GPIO.setup(relay, GPIO.OUT)
GPIO.setup(switch, GPIO.IN) 
GPIO.setup(sensor, GPIO.IN)

print("Vil du bruke en switch, eller en fuktighets sensor?")
print("Skriv A for Sensor, og B for switch.")
ans = input()

if ans == "A" or ans == "a":
    while True:
        while GPIO.input(sensor) == False:
            GPIO.output(relay, True) 
            sleep(0.2) #PÅ
            GPIO.output(relay, False)
            sleep(1) #AV
        else:
            GPIO.output(relay, False)
elif ans == "B" or ans == "b":
    while True:
        while GPIO.input(switch) == False:
            GPIO.output(relay, True)
            sleep(0.2) #PÅ
            GPIO.output(relay, False)
            sleep(1) #AV
        else:
            GPIO.output(relay, False)

