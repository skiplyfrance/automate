import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#On map les sorties
MappingOut = {}

# Configuration des sorties

# Sortie puissance 1
GPIO.setup(13, GPIO.OUT)
MappingOut[1] = 13

# Sortie puissance 2
GPIO.setup(16, GPIO.OUT)
MappingOut[2] = 16

# Sortie puissance 3
GPIO.setup(6, GPIO.OUT)
MappingOut[3] = 6

# Sortie puissance 4
GPIO.setup(12, GPIO.OUT)
MappingOut[4] = 12

# Commande LED 1
GPIO.setup(14, GPIO.OUT)
MappingOut[5] = 14

# Commande LED 2
GPIO.setup(15, GPIO.OUT)
MappingOut[6] = 15

# Commande LED 3
GPIO.setup(17, GPIO.OUT)
MappingOut[7] = 17

# Commande LED 4
GPIO.setup(18, GPIO.OUT)
MappingOut[8] = 18

# LED ON
GPIO.setup(7, GPIO.OUT)
MappingOut[9] = 7
            
class FixOutput():

    def set_output(self,output,value):
        GPIO.output(MappingOut[int(output)], value)
        GPIO.output(MappingOut[int(output) + 4], value)
