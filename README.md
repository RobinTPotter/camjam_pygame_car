# camjam_pygame_car

Got a [cam jam edukit 3](https://camjam.me/?page_id=1035) for my birthday and shoddily stole some of their [code](https://github.com/CamJam-EduKit/EduKit3/blob/master/CamJam%20Edukit%203%20-%20RPi.GPIO/Code/7-pwm2.py) and turned it into a class and added [pygame](https://www.pygame.org/docs/ref/joystick.html) and used the [retropie](https://github.com/RetroPie/RetroPie-Setup/wiki) setup script to add my bluetooth controller. I will not cheapen this entry and lower myself to advertising which make, suffice it to say it was inexpensive and I have already taken it apart to solder a bit which came off when dropped.

This was created for a raspberry pi zero w. Use stretch rather than stretch lite and save yourself a bit of hassle.

For added hassle, configure wlan0 as wireless access point and code on the bus with your Pi in your top pocket. Take care, however, prolonged use can singe a nipple.

during the course of developming this I have had cause to alter the [udev rules](http://www.reactivated.net/writing_udev_rules.html#syntax) that were applied by retropie when correctly registing my joypad/stick.

the above site was invaluable to my head around udev. the default rule that RetroPie adds is too general and, because I wanted to trigger a script on device connecting, was firing 3 times. if you need to create a rule, make sure your device is connected and try to find it on the path /sys/devices/, clues may be found in /dev also. then running the udevadm utility:

```
udevadm info -a -p /sys/devices/platform/pcspkr/input/input1
```

you can find the top level specific device you need followed by its parents:

```
looking at device '/devices/platform/pcspkr/input/input1':
KERNEL=="input1"
SUBSYSTEM=="input"
DRIVER==""
ATTR{name}=="PC Speaker"
ATTR{phys}=="isa0061/input0"
ATTR{uniq}==""
ATTR{properties}=="0"
```
after the "looking at" line, these are the "filters" that identify the device so along with the directive to say whether the rule acts when "add" or "remove" action occurs, and, you describe what you want to happen the rule might become:

```
ACTION=="add", KERNEL=="input1", SUBSYSTEM=="input", DRIVER=="", ATTR{name}=="PC Speaker", ATTR{phys}=="isa0061/input0", ATTR{uniq}=="", ATTR{properties}=="0", RUN+="/home/pi/alarm_bells.sh"
```

the really big thing that you may happen accross is the fact that when udev starts, the filesystem is completely read only, and that is how it remembers it untill you restart udev. i.e. you cannot write to any part of the system regardless of who you are. I set up a root crontab to restart the udev service every two mins.

after that i was able to set a rule that ran (once) when the device was connected, this caused a python loop getting events off the pygame event queue which shutdown the system when start and select buttons are pressed together.




