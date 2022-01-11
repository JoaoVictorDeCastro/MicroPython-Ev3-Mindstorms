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
medium_motor = Motor(Port.D)
left_wheel = Motor(Port.B)
right_wheel = Motor(Port.C)
robot = DriveBase(left_wheel,right_wheel,wheel_diameter=55.5,axle_track=104)
# Write your program here.
medium_motor.run_target(2000,250)
left_wheel.run_target(3000,390)
robot.turn(110)
robot.turn(-110)
robot.straight(250)
robot.straight(-250)
robot.stop()
left_wheel.break()
right_wheel.break()
for c in range (0,3):
    robot.straight(360)
    robot.stop()
    left_wheel.break()
    right_wheel.break()
