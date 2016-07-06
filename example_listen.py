# Dash will turn to the sound he hears and then drives 40cm towards it

from robot import *
import time

def example():    # turn towards sound
  sd = 0
  while not (sys.stdin in select.select([sys.stdin], [], [], 0)[0]):
    if sd != dash.soundDirection:
      dash.turn(dash.soundDirection)
      time.sleep(3)
      dash.drive(400)
    sd = dash.soundDirection

def main():
    global dash
    dash = robot(getRobotDevice())
    print("Press {enter} to stop demo")
    example()
    dash.disconnect()

ble.run_mainloop_with(main)
