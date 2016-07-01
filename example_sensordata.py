#Example robot control change btDash and btDot into the values for your robot
#find the bluetooth adress of your robot with the command: hcitool lescan

from robot import *

btDash = "d4:75:30:ab:02:56"
btDot = "D0:C5:55:9F:C5:C4"

dash = robot(btDash)
dash.reset()

# Show sensor data
displaySensorData(dash)

dash.disconnect()
