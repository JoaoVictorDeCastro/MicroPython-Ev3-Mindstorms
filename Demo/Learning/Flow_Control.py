#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here. - Initialization Process

ev3 = EV3Brick()
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, wheel_diameter=55.5, axle_track=104)

# Write your program here.

#Loop - Forever

while True:

#Loop - Condition 

while robot.distance() <300:
    robot.drive(250,0)
robot.stop
left.brake()
right.brake()

#If e Else - Condition

while True:
    if Button.CENTER in ev3.buttons.pressed():
        robot.straight(-200)
        robot.straight(200)
    elif Button.RIGHT in ev3.buttons.pressed():
        robot.straight(-300)
        robot.straight(300)
    else:
        robot.straight(200)
        robot.straight(-200)
while robot.distance() >= 500: 
    robot.drive(-200,0)
robot.stop()
right.brake()
left.brake()

#Wait 

wait(2000)