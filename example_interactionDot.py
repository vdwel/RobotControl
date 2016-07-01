# Example robot control change btDash and btDot into the values for your robot
# find the bluetooth adress of your robot with the command: hcitool lescan

# Dash will turn to the sound he hears and then drives 40cm towards it

from robot import *

btDash = "d4:75:30:ab:02:56" # change these to your robots bt addres
btDot = "D0:C5:55:9F:C5:C4"

dot = robot(btDot)
dot.reset()

running = False

def example():  
  global running
  running = True
  thread.start_new_thread(Disco, ())
  dot.topLight(True)
  while not (sys.stdin in select.select([sys.stdin], [], [], 0)[0]):
    if dot.button0:
        dot.playSound(GOBBLE)
        time.sleep(2)
    if dot.button1:
        dot.playSound(HORSE)
        time.sleep(2)
    if dot.button2:
        dot.playSound(MYSOUND4)
        time.sleep(2)
    if dot.button3:
        dot.playSound(HI)
        time.sleep(2)
    if dot.tilt > 600:
        dot.playSound(UHOH)
        time.sleep(2)
    if dot.lean > 600:
        dot.playSound(DOG)
        time.sleep(2)
    if dot.tilt < -600:
        dot.playSound(FIRESIREN)
        time.sleep(2)
    if dot.lean < -600:
        dot.playSound(JETPLANE)
        time.sleep(3)
  running = False
  time.sleep(0.5)

def Disco():
    global running
    red = 16
    green = 71
    blue = 41
    redStep = 10
    greenStep = -20
    blueStep = 15
    while running:
        time.sleep(0.1)
        red += redStep
        if (red < 0) | (red > 255):
        	red -= redStep
        	redStep = -redStep
        green += greenStep
        if (green < 0) | (green > 255):
        	green -= greenStep
        	greenStep = -greenStep
        blue += blueStep
        if (blue < 0) | (blue > 255):
        	blue -= blueStep
        	blueStep = -blueStep
        dot.colorAll(red, green, blue, red, green, blue, red, green, blue)
        
print("Press {enter} to stop demo")
example()
dot.disconnect()
