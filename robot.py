#! /usr/bin/python3

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library
import pygame

# inititalize pygame
print ('inititalizing pygame and jostick API')

pygame.init()
pygame.joystick.init()



print ('find joystick')

joystick_name = 'GEN GAME S5'

print ('testing for favourite named stick {0}'.format(joystick_name))

joystick = None

for jn in range(pygame.joystick.get_number()):
    j = pygame.joystick.Joystick(jn)
    if j.get_name() is joystick_name: joystick = j

if joystick is None:
    print ('joystick {0} is not found'.format(joystick_name))
else:
    print ('found {0}'.format(joystick.get_name()))


print ('set up GPIO')

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


print ('set up GPIO pins')

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7


print ('robot class definition')

class Robot():

    def __init__(self):

        print ('initializing class variables')

        # How many times to turn the pin on and off each second
        self.frequency = 20
        # How long the pin stays on each cycle, as a percent
        self.duty_cycle_A = 30
        self.duty_cycle_B = 30
        # Setting the duty cycle to 0 means the motors will not turn
        self.stop = 0

        print ('initialize GPIO pins')

        # Set the GPIO Pin mode to be Output
        GPIO.setup(pinMotorAForwards, GPIO.OUT)
        GPIO.setup(pinMotorABackwards, GPIO.OUT)
        GPIO.setup(pinMotorBForwards, GPIO.OUT)
        GPIO.setup(pinMotorBBackwards, GPIO.OUT)

        print ('setting initial PWM frequency')

        #must do this before set stop
        self.set_frequency()
        
        print ('start software PWM')        
        
        # Start the software PWM with a duty cycle of 0 (i.e. not moving)
        self.pwmMotorAForwards.start(stop)
        self.pwmMotorABackwards.start(stop)
        self.pwmMotorBForwards.start(stop)
        self.pwmMotorBBackwards.start(stop)
        
        print ('inititalied robot')
        

    # Set the GPIO to software PWM at 'frequency' Hertz
    def set_frequency(self,frequency):            
        self.pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, frequency)
        self.pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, frequency)
        self.pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, frequency)
        self.pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, frequency)
        print ('frequecy set to {0} on both motors'.format(frequency))

    # Turn all motors off
    def stopmotors(self):
        self.pwmMotorAForwards.ChangeDutyCycle(stop)
        self.pwmMotorABackwards.ChangeDutyCycle(stop)
        self.pwmMotorBForwards.ChangeDutyCycle(stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(stop)
        print ('all motors set to {0}'.format(stop))

    # Turn both motors forwards
    def forwards(self):
        pwmMotorAForwards.ChangeDutyCycle(self.duty_cycle_A)
        pwmMotorABackwards.ChangeDutyCycle(self.stop)
        pwmMotorBForwards.ChangeDutyCycle(self.duty_cycle_B)
        pwmMotorBBackwards.ChangeDutyCycle(self.stop)

    # Turn both motors backwards
    def backwards(self):
        pwmMotorAForwards.ChangeDutyCycle(self.stop)
        pwmMotorABackwards.ChangeDutyCycle(self.duty_cycle_A)
        pwmMotorBForwards.ChangeDutyCycle(self.stop)
        pwmMotorBBackwards.ChangeDutyCycle(self.duty_cycle_B)

    # Turn left
    def left(self):
        pwmMotorAForwards.ChangeDutyCycle(self.stop)
        pwmMotorABackwards.ChangeDutyCycle(self.duty_cycle_A)
        pwmMotorBForwards.ChangeDutyCycle(self.duty_cycle_B)
        pwmMotorBBackwards.ChangeDutyCycle(self.stop)

    # Turn Right
    def right(self):
        pwmMotorAForwards.ChangeDutyCycle(self.duty_cycle_A)
        pwmMotorABackwards.ChangeDutyCycle(self.stop)
        pwmMotorBForwards.ChangeDutyCycle(self.stop)
        pwmMotorBBackwards.ChangeDutyCycle(self.duty_cycle_B)

    # Turn Right
    def tank(self,duty_cycle_A,duty_cycle_B):
        if duty_cycle_A>0:
            pwmMotorAForwards.ChangeDutyCycle(duty_cycle_A)
        elif duty_cycle_A<0:            
            pwmMotorABackwards.ChangeDutyCycle(duty_cycle_A)
        else:
            pwmMotorAForwards.ChangeDutyCycle(stop)
            pwmMotorABackwards.ChangeDutyCycle(stop)
        
        if duty_cycle_B>0:
            pwmMotorBForwards.ChangeDutyCycle(duty_cycle_B)
        elif duty_cycle_B<0:            
            pwmMotorBBackwards.ChangeDutyCycle(duty_cycle_B)
        else:
            pwmMotorBForwards.ChangeDutyCycle(stop)
            pwmMotorBBackwards.ChangeDutyCycle(stop)
        


 

GPIO.cleanup()