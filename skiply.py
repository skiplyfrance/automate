#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 ACTIGITAL SASU

import requests
import time
import json
import sys
import pygame

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

# Commande IN 1
GPIO.setup(27, GPIO.IN)

# Commande IN 2
GPIO.setup(23, GPIO.IN)

# Commande IN 3
GPIO.setup(22, GPIO.IN)

# Commande IN 4
GPIO.setup(24, GPIO.IN)

ForceUrl = str(sys.argv[1])
InputUrl = str(sys.argv[2])
ForceOutput = [1,2,3,4]

#configuration du debug

class Dashboard():

    def __init__(self):
        pygame.init()
        self.output_state = counter.FixOutput()
        self.parsefix()
        GPIO.add_event_detect(27, GPIO.FALLING, callback=self.detect_input, bouncetime=2000) 
        self.song = pygame.mixer.Sound('jingle.ogg')

        while True:
            self.boucle()
            time.sleep(poll_interval)
            self.parsefix()

    def boucle(self):
        # mise à jour des sorties fixes
        old_14 = GPIO.input(14)
        old_15 = GPIO.input(15)
        old_17 = GPIO.input(17)
        old_18 = GPIO.input(18)
        if len(ForceOutput) > 0:
            for fix_output in ForceOutput:
                self.output_state.set_output(fix_output,self.fix_values[str(fix_output)])
        if GPIO.input(14) > old_14 or GPIO.input(15) > old_15 or GPIO.input(17) > old_17 or GPIO.input(18) > old_18:
            self.song.play()

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

    def detect_input(self,channel):
        time.sleep(0.5)
        if not GPIO.input(channel):
            try:
                req3 = requests.get(InputUrl)
                #response3 = req3.text
            except:
                self.connection_errors = 1

if __name__ == '__main__':
    Dashboard()
