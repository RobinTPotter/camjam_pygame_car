"""initializes RPi.GPIO, assuming installed, sets the pins for motor controls for
the CamJam EduKit3
"""

import RPi.GPIO as GPIO  # Import the GPIO Library

print ('set up GPIO pins')
# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

print ('robot class definition')

class Robot():
    """Control class for camjam edukit 3 robot motorcar"""

    def __init__(self):

        print ('set up GPIO')
        # Set the GPIO modes
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        print ('initializing class variables')

        # How many times to turn the pin on and off each second
        self.frequency = 10
        # How long the pin stays on each cycle, as a percent
        self.duty_cycle_A = 30
        self.duty_cycle_B = 30
        # Setting the duty cycle to 0 means the motors will not turn
        self.stop = 0

        # less wiggle room for tank centre joystick false dead spot
        self.tank_tolerance = 1

        print ('initialize GPIO pins')

        # Set the GPIO Pin mode to be Output
        GPIO.setup(pinMotorAForwards, GPIO.OUT)
        GPIO.setup(pinMotorABackwards, GPIO.OUT)
        GPIO.setup(pinMotorBForwards, GPIO.OUT)
        GPIO.setup(pinMotorBBackwards, GPIO.OUT)

        print ('setting initial PWM frequency')

        #must do this before set stop
        self.set_frequency(20)
        
        print ('start software PWM')        
        
        # Start the software PWM with a duty cycle of 0 (i.e. not moving)
        self.pwmMotorAForwards.start(self.stop)
        self.pwmMotorABackwards.start(self.stop)
        self.pwmMotorBForwards.start(self.stop)
        self.pwmMotorBBackwards.start(self.stop)
        
        print ('inititalied robot')

    # Set the GPIO to software PWM at 'frequency' Hertz
    def set_frequency(self,freq):
        """change the frequency of the PWM controlling the motor"""
        
        self.frequency = freq
        self.pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, freq)
        self.pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, freq)
        self.pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, freq)
        self.pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, freq)
        print ('frequecy set to {0} on both motors'.format(freq))

    # Turn all motors off
    def stopmotors(self):
        """stop the motors, sets the duty cycle (percentage of cycle is on) to stop value (0)"""
        
        self.pwmMotorAForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.stop)
        print ('all motors set to {0}'.format(self.stop))

    # Turn both motors forwards
    def forwards(self):
        """sets the duty cycle of both motors in the forward setting to default value duty_cycle_A and B"""
        
        self.pwmMotorAForwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorABackwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.duty_cycle_B)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.stop)

    # Turn both motors backwards
    def backwards(self):
        """sets the duty cycle of both motors in the backward setting to default value duty_cycle_A and B"""
        
        self.pwmMotorAForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorBForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.duty_cycle_B)

    # Turn left
    def left(self):
        """sets the duty cycle of both motors in the backward / forwards setting to default value duty_cycle_A and B"""
        self.pwmMotorAForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorBForwards.ChangeDutyCycle(self.duty_cycle_B)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.stop)

    # Turn Right
    def right(self):
        """sets the duty cycle of both motors in the forwards / backward setting to default value duty_cycle_A and B"""
        
        self.pwmMotorAForwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorABackwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.duty_cycle_B)

    # Turn Right
    def tank(self,duty_cycle_A,duty_cycle_B):
        """tank control function, used to set forwards or backwards depending on positive of negative of either cycle value sent"""
        
        if duty_cycle_A>self.tank_tolerance:
            self.pwmMotorAForwards.ChangeDutyCycle(duty_cycle_A)
        elif duty_cycle_A<-self.tank_tolerance:            
            self.pwmMotorABackwards.ChangeDutyCycle(abs(duty_cycle_A))
        else:
            self.pwmMotorAForwards.ChangeDutyCycle(self.stop)
            self.pwmMotorABackwards.ChangeDutyCycle(self.stop)
        
        if duty_cycle_B>self.tank_tolerance:
            self.pwmMotorBForwards.ChangeDutyCycle(duty_cycle_B)
        elif duty_cycle_B<-self.tank_tolerance:            
            self.pwmMotorBBackwards.ChangeDutyCycle(abs(duty_cycle_B))
        else:
            self.pwmMotorBForwards.ChangeDutyCycle(self.stop)
            self.pwmMotorBBackwards.ChangeDutyCycle(self.stop)
    
    def goodbye(self):
        """used to reset and remove GPIO pipes created in filesystem"""        
        
        GPIO.cleanup()
        
if __name__ == '__main__':
    print ('Robot object should be imported')
