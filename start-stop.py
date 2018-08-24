#!/usr/bin/python

# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO
import os
import time

# On passe en mode d'adressage par numero GPIO et pas par pin
GPIO.setmode(GPIO.BCM)

#Maintien de la tension
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, True)

# Commande LED 1
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, True)

# Commande LED 2
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, False)

# Commande LED 3
GPIO.setup(17, GPIO.OUT)

# Commande LED 4
GPIO.setup(18, GPIO.OUT)

# Bouton Off (1 = bouton relache)
GPIO.setup(5, GPIO.IN)
# Bouton RESET
GPIO.setup(21, GPIO.IN)

# LED ON
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)

drapeau=1

while drapeau==1:
    if (GPIO.input(5) and drapeau==1):
        drapeau = 0
        GPIO.setup(4, GPIO.OUT)
        GPIO.output(4, False)
        GPIO.output(14, True)
        GPIO.output(15, True)
        GPIO.output(17, True)
        GPIO.output(18, True)
        call(['sudo','shutdown','-h','now'], shell=False)
    if (GPIO.input(21)==0 and drapeau==1):
        drapeau = 0
        GPIO.output(14, True)
        GPIO.output(15, True)
        GPIO.output(17, True)
        GPIO.output(18, True)
        call('reboot', shell=False)
    time.sleep(0.1)
#loop() # Run the loop function to keep script running
