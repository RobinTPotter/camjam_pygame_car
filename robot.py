#! /usr/bin/python3

import time  # Import the Time library
import pygame
import sys

# inititalize pygame
from joystick_module import joystick, STOP_BUTTON, LEFT_UP_DOWN_AXIS, \
    RIGHT_UP_DOWN_AXIS, DUTY_CYCLE_REMAP_MAX

if joystick is None:
    print ('joystick is none')
    sys.exit(1)

from robot_module import Robot
robot = Robot()
time.sleep(0.5)

done = False
if True: #try:    
    while done==False:         

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT:
                done = True # Flag that we are done so we exit this loop

            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION
            #   JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                if 'button' in event.dict: print("Joystick button {0} pressed".format(event.button))
                if event.button == STOP_BUTTON:
                        done = True

            if event.type == pygame.JOYBUTTONUP:
                if 'button' in event.dict: print("Joystick button {0} released".format(event.button))

            # axes found on such as dual shock controller. value 
            # "get_axes" comeout like a continuous number from -1 to 1
            if event.type == pygame.JOYAXISMOTION:
                print ('did thing with axis {0}'.format(event.dict))                
                
                #getting the value of the "left" axis
                _left = joystick.get_axis(LEFT_UP_DOWN_AXIS)
                
                #finding the sign of the left value +/-1
                if _left!=0.0: _lsign = _left/abs(_left)
                else: _lsign = 1
                    
                #create the left value, this is squared to give a more graceful remap
                #this is because sqareing a number makes it positive
                left = -_lsign*_left*_left * DUTY_CYCLE_REMAP_MAX
                
                #getting the value of the "right" axis
                _right = joystick.get_axis(RIGHT_UP_DOWN_AXIS) 
                
                #finding the sign of the right value +/-1
                if _right!=0.0: _rsign = _right/abs(_right)
                else: _rsign = 1
                    
                #create the righht value, this is squared to give a more graceful remap
                right = -_rsign*_right*_right * DUTY_CYCLE_REMAP_MAX
                
                robot.tank(
                    int(left),
                    int(right)
                )

            # a hat is like the directional buttons on a joypad.
            # only option for original ps one, or snes like controller
            # value comes out like a tuple.
            if event.type == pygame.JOYHATMOTION:
                print ('did thing with hat {0}'.format(event.dict))
                if event.value==(0,1):
                    robot.forwards()
                elif event.value==(0,-1):
                    robot.backwards()
                elif event.value==(1,0):
                    robot.right()
                elif event.value==(-1,0):
                    robot.left()
                elif event.value==(0,0):
                    robot.stopmotors()

#except Exception as e:
#    print ('grr #monday {0}'.format(e))

robot.goodbye()
