import RPi.GPIO as GPIO  # Import the GPIO Library

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
        self.frequency = freq
        self.pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, freq)
        self.pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, freq)
        self.pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, freq)
        self.pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, freq)
        print ('frequecy set to {0} on both motors'.format(freq))

    # Turn all motors off
    def stopmotors(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.stop)
        print ('all motors set to {0}'.format(self.stop))

    # Turn both motors forwards
    def forwards(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorABackwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.duty_cycle_B)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.stop)

    # Turn both motors backwards
    def backwards(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorBForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.duty_cycle_B)

    # Turn left
    def left(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorABackwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorBForwards.ChangeDutyCycle(self.duty_cycle_B)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.stop)

    # Turn Right
    def right(self):
        self.pwmMotorAForwards.ChangeDutyCycle(self.duty_cycle_A)
        self.pwmMotorABackwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBForwards.ChangeDutyCycle(self.stop)
        self.pwmMotorBBackwards.ChangeDutyCycle(self.duty_cycle_B)

    # Turn Right
    def tank(self,duty_cycle_A,duty_cycle_B):
        if duty_cycle_A>self.tank_tolerance:
            self.pwmMotorAForwards.ChangeDutyCycle(duty_cycle_A)
        elif duty_cycle_A<self.tank_tolerance:            
            self.pwmMotorABackwards.ChangeDutyCycle(duty_cycle_A)
        else:
            self.pwmMotorAForwards.ChangeDutyCycle(stop)
            self.pwmMotorABackwards.ChangeDutyCycle(stop)
        
        if duty_cycle_B>self.tank_tolerance:
            self.pwmMotorBForwards.ChangeDutyCycle(duty_cycle_B)
        elif duty_cycle_B<self.tank_tolerance:            
            self.pwmMotorBBackwards.ChangeDutyCycle(duty_cycle_B)
        else:
            self.pwmMotorBForwards.ChangeDutyCycle(stop)
            sself.pwmMotorBBackwards.ChangeDutyCycle(stop)
    
    def goodbye(self):
        GPIO.cleanup()
        
if __name__ == '__main__':
    print ('Robot object should be imported')