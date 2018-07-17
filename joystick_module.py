"""provides favorite joystick and controls to main code, acts as config also (!)"""

import time  # Import the Time library
import pygame

print ('inititalizing pygame and jostick API')

pygame.init()
pygame.joystick.init()

# jostick settings (todo move to config)

joystick_name = 'GEN GAME S5'
STOP_BUTTON = 10 #None
LEFT_UP_DOWN_AXIS = 0
RIGHT_UP_DOWN_AXIS = 2

# joystick control parameters (todo move to config)

# max possible cycle percentage
DUTY_CYCLE_REMAP_MAX = 80


print ('find joystick')
print ('testing for favourite named stick {0}'.format(joystick_name))

joystick = None

for jn in range(pygame.joystick.get_count()):
    j = pygame.joystick.Joystick(jn)
    print(j.get_name())
    if j.get_name()==joystick_name: joystick = j

if joystick is None:
    print ('joystick {0} is not found'.format(joystick_name))
else:
    joystick.init()
    print ('found {0}'.format(joystick.get_name()))
    print ('get_numaxes {0}'.format(joystick.get_numaxes()))
    print ('get_numballs {0}'.format(joystick.get_numballs()))
    print ('get_numbuttons {0}'.format(joystick.get_numbuttons()))
    print ('get_numhats {0}'.format(joystick.get_numhats()))
    if STOP_BUTTON is None:
        print ('press stop button will be used as stop button')
        #STOP_BUTTON
        done = False
        while done==False:
            for event in pygame.event.get(): # User did something                
                if event.type == pygame.JOYBUTTONDOWN:
                    STOP_BUTTON = event.button
                    print ('stop button defined as {0}, you can enter this in your config if you want'.format(STOP_BUTTON))
                    time.sleep(1)
                    done = True


if __name__ == '__main__':
    print ('joystick should be imported, and any button config you want')
