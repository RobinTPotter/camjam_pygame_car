#! /usr/bin/python3

import time  # Import the Time library
import pygame
import sys

# inititalize pygame
from joystick_module import joystick, STOP_BUTTON, LEFT_UP_DOWN_AXIS, RIGHT_UP_DOWN_AXIS

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
            
            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                if 'button' in event.dict: print("Joystick button {0} pressed".format(event.button))
                if event.button == STOP_BUTTON:
                        done = True
                
            if event.type == pygame.JOYBUTTONUP:
                if 'button' in event.dict: print("Joystick button {0} released".format(event.button))

            if event.type == pygame.JOYAXISMOTION:
                print ('did thing with axis {0}'.format(event.dict))                
                
                left = joystick.get_axis(LEFT_UP_DOWN_AXIS) * DUTY_CYCLE_REMAP_MAX
                right = joystick.get_axis(RIGHT_UP_DOWN_AXIS) * DUTY_CYCLE_REMAP_MAX
                
                robot.tank(
                    int(left),
                    int(right)
                )

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
