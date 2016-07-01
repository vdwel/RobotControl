# RobotControl
A simple python library to control Dash and Dot robots from Wonder Workshop.

This python library has been developed by using the AdaFruit BlueFruit LE sniffer to capture communication between the iPad and the Robots.

It might contain errors or might not work anymore in future release of the robot firmware.

Using this library is at your own risk.

Usage:
from robot import *

Create a robot object like:
dash = robot('bluetooth adress from your robot')

Execute commands to the robot like:
dash.command(arg1, arg2, arg..)

For debugging, show all sensor data with the command:
displaySensorData(robot) #where robot is your robot object

Read sensor data like:
value = dash.sensor

When finished use the command: dash.disconnect()
Otherwise the gatttool keeps running in the background and you might not be able to connect anymore.
If this happens you kan kill the gatttool with the commandline: killall gatttool

Supported commands:
* connect()
* disconnect()
* reset()
* playSound(const sound)
  sound is a sound from the list below
* playBeep(int tone, int time in ms)
  can also be used without the tone and time
* drive(int distance in mm, int time in ms)
* setWheelSpeed(int speed, int turnspeed)
  speed is between -400 and 400
  turnspeed is between -500 and 500
* stopWheels()
* turn(int degrees, int time in ms)
* moveHeadY(int degrees)
  -7 < degrees > 22
* moveHeadX(int degrees)
  -135 < degrees > 135
* colorFront(int red, int green, int blue)
* colorLeftEar(int red, int green, int blue)
* colorRightEar(int red, int green, int blue)
* colorAll(int redFront, int greenFront, int blueFront, int redLeft, int greenLeft, int blueLeft, int redRight, int greenRight, int blueRight)
* topLight(bool on)
* tailLight(bool on)
* eyeLights(int intensity, 12bit integer)
  Each bit represents a led, bit0 is top led, bit1 is led right from top led (when facing the robot)

Available sensordata:
* leftDistanceSensor (int)
* rightDistanceSensor (int)
* rearDistanceSensor (int)
* button0 (bool)
* button1 (bool)
* button2 (bool)
* button3 (bool)
* tilt (int)
* lean (int)
* soundLevel (int)
* clap (booL)
* headX (int)
* headY (int)
* leftWheel (int)
* rightWheel (int)
* zRotationAcceleration (int)
* deltaZRotationAcceleration (int)
* deltaXRotationAcceleration (int)
* deltaYRotationAcceleration (int)
* zAcceleration (int)
  between -2040 and +2040
* soundDirection (int)
* leftSensorSeesDot (bool)
* rightSensorSeesDot (bool)
* unknown1 (int)

Sounds:
* HI
* HUH
* UHOH
* OKAY
* SIGH
* TADA
* WEE
* BYE
* HORSE
* CAT
* DOG
* DINOSAUR
* LION
* GOAT
* CROCODILE
* ELEPHANT
* FIRESIREN
* TRUCKHORN
* CARENGINE
* CARTIRESQUEEL
* HELICOPTER
* JETPLANE
* BOAT
* TRAIN
* BEEPS
* LASERS
* GOBBLE
* BUZZ
* AYYAIYAI
* SQUEEK
* MYSOUND1
* MYSOUND2
* MYSOUND3
* MYSOUND4
* MYSOUND5
