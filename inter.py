#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import requests

InputUrl = "https://url.skiply.eu/feuin"

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

def my_callback(channel):
    if not GPIO.input(27):
        print("un evenement s'est produit")
        try:
            req3 = requests.get(InputUrl)
            #response3 = req3.text
        except:
            self.connection_errors = 1

#ici on ajoute une tempo de 75 ms pour eviter l'effet rebond
GPIO.add_event_detect(27, GPIO.RISING, callback=my_callback, bouncetime=500) 
#votre programme ici

#if GPIO.input(27):
#    print('Input was HIGH')
#else:
#    print('Input was LOW')

time.sleep(50)
