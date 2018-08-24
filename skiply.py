#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 ACTIGITAL SASU

import requests
import time
import json
import sys

#import des parametres skiply
poll_interval = 5

#import correct library according to box version
import counter as counter
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# Commande LED 1
GPIO.setup(14, GPIO.OUT)

# Commande LED 2
GPIO.setup(15, GPIO.OUT)

# Commande LED 3
GPIO.setup(17, GPIO.OUT)

# Commande LED 4
GPIO.setup(18, GPIO.OUT)

ForceUrl = str(sys.argv[1])
ForceOutput = [1,2,3,4]

#configuration du debug

class Dashboard():

    def __init__(self):
        self.output_state = counter.FixOutput()
        self.parsefix()

        while True:
            self.boucle()
            time.sleep(poll_interval)
            self.parsefix()

    def boucle(self):
        # mise à jour des sorties fixes
        if len(ForceOutput) > 0:
            for fix_output in ForceOutput:
                self.output_state.set_output(fix_output,self.fix_values[str(fix_output)])

    def parsefix(self):
        #logging.info('avant le parsing')
        parametrescharges = True
        while parametrescharges:
            try:
                req2 = requests.get(ForceUrl)
                response2 = req2.text
                self.fix_values = json.loads(response2)
                parametrescharges = False
            except:
                self.connection_errors = 1
                led1 = GPIO.input(14)
                led2 = GPIO.input(15)
                led3 = GPIO.input(17)
                led4 = GPIO.input(18)
                time.sleep(1)
                GPIO.output(14, not led1)
                GPIO.output(15, not led2)
                GPIO.output(17, not led3)
                GPIO.output(18, not led4)
                time.sleep(1)
                GPIO.output(14, led1)
                GPIO.output(15, led2)
                GPIO.output(17, led3)
                GPIO.output(18, led4)
                time.sleep(1)
                GPIO.output(14, not led1)
                GPIO.output(15, not led2)
                GPIO.output(17, not led3)
                GPIO.output(18, not led4)
                time.sleep(1)
                GPIO.output(14, led1)
                GPIO.output(15, led2)
                GPIO.output(17, led3)
                GPIO.output(18, led4)
                time.sleep(1)
                GPIO.output(14, not led1)
                GPIO.output(15, not led2)
                GPIO.output(17, not led3)
                GPIO.output(18, not led4)
                time.sleep(1)
                GPIO.output(14, led1)
                GPIO.output(15, led2)
                GPIO.output(17, led3)
                GPIO.output(18, led4)
                parametrescharges = True

if __name__ == '__main__':
    Dashboard()
