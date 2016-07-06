# Dash will drive around, trying to avoid obstacles while constantly turning his head
# Example not working yet

from robot import *
import kbhit


def main():
    global dash
    dash = robot(getRobotDevice())
    kb = kbhit.KBHit()

    STOP = 0
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

    k_in = ''
    status = STOP
    idle = 0
    while (k_in != 'x'):
        print("Key not pressed")  # Do something
        if kb.kbhit():  # If a key is pressed:
            k_in = kb.getch()  # Detect what key was pressed
            print("You pressed ", k_in, "!")  # Do something
    kb.set_normal_term()
    dash.disconnect()

ble.run_mainloop_with(main)