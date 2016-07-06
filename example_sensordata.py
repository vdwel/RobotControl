#Example robot control change btDash and btDot into the values for your robot
#find the bluetooth adress of your robot with the command: hcitool lescan

from robot import *

def main():
    dash = robot(getRobotDevice())
    # Show sensor data
    displaySensorData(dash)
    dash.disconnect()

ble.run_mainloop_with(main)