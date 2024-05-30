from time import sleep
import RPi.GPIO as GPIO
import time
import sys
import os



output_directory = '/home/olosa/mu_code/Vannings'
output_file_path = os.path.join(output_directory, 'data.txt')



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
try:
    original_stdout = sys.stdout
    with open(output_file_path, 'w') as file:
        sys.stdout = file


    if ans == "A" or ans == "a":
        while True:
            while GPIO.input(sensor) == False:
                GPIO.output(relay, True)
                sleep(0.2)
                GPIO.output(relay, False)
                sleep(1)
            else:
                GPIO.output(relay, False)
                print("Sist vannet", date)
    elif ans == "B" or ans == "b":
        while True:
            while GPIO.input(switch) == False:
                GPIO.output(relay, True)
                sleep(0.2)
                GPIO.output(relay, False)
                sleep(1)
            else:
                GPIO.output(relay, False)
                print("Sist vannet", date)

except KeyboardInterrupt:
    sys.stdout = sys.__stdout__
