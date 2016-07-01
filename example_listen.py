# Example robot control change btDash and btDot into the values for your robot
# find the bluetooth adress of your robot with the command: hcitool lescan

# Dash will turn to the sound he hears and then drives 40cm towards it

from robot import *

btDash = "d4:75:30:ab:02:56" # change these to your robots bt addres
btDot = "D0:C5:55:9F:C5:C4"

dash = robot(btDash)
dash.reset()

def example():    # turn towards sound
  sd = 0
  while not (sys.stdin in select.select([sys.stdin], [], [], 0)[0]):
    if sd != dash.soundDirection:
      dash.turn(dash.soundDirection)
      time.sleep(3)
      dash.drive(400)
    sd = dash.soundDirection

print("Press {enter} to stop demo")
example()
dash.disconnect()