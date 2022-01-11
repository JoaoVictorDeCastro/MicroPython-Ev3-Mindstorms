#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.

ev3 = EV3Brick()
left = Motor(Port.B)
rigt = Motor(Port.C)
rigt_medium = Motor(Port.A)
left_medium = Motor(Port.D)
color_left = ColorSensor(Port.s1)
color_right = ColorSensor(Port.s4)
recognize = ColorSensor(Port.s3) 
gyro = GyroSensor(Port.s2)

# Write your program here.
