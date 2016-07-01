# Example robot control change btDash and btDot into the values for your robot
# find the bluetooth adress of your robot with the command: hcitool lescan

# Dash will drive around, trying to avoid obstacles while constantly turning his head

from robot import *
import kbhit

btDash = "d4:75:30:ab:02:56" # change these to your robots bt addres
btDot = "D0:C5:55:9F:C5:C4"

dash = robot(btDash)
dash.reset()

kb = kbhit.KBHit()

STOP = 0
FORWARD = 1
BACKWARD = 2
LEFT = 3
RIGHT = 4


k_in=''
status = STOP
idle = 0
while(k_in != 'x'): 
    print("Key not pressed") #Do something
    if kb.kbhit(): #If a key is pressed:
        k_in = kb.getch() #Detect what key was pressed
        print("You pressed ", k_in, "!") #Do something
kb.set_normal_term()

dash.disconnect()
