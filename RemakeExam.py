from time import sleep
import RPi.GPIO as GPIO
import time


timestamp = time.time()
date = time.ctime(timestamp)

value = 0
newValue = 0

GPIO.setmode(GPIO.BCM)


relay = 17
sensor = 27
switch = 22
switch2 = 23

GPIO.setup(switch2, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(sensor, GPIO.IN)

print("Vil du bruke en switch, eller en fuktighets sensor?")
print("Skriv A for Sensor, og B for switch.")
ans = input()

if ans == "A" or ans == "a":

        while GPIO.input(sensor) == False:
            GPIO.output(relay, True)

        while GPIO.Input(sensor) == True:
            GPIO.output(relay, False)
elif ans == "B" or ans == "b":

        while GPIO.input(switch) == False:
            GPIO.output(relay, True)
            value = (newValue + 1)

        while GPIO.input(switch) == True:
            GPIO.output(relay, False)


