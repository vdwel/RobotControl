# Example robot control change btDash and btDot into the values for your robot
# find the bluetooth adress of your robot with the command: hcitool lescan

# Dash will drive around, trying to avoid obstacles while constantly turning his head

from robot import *

btDash = "d4:75:30:ab:02:56" # change these to your robots bt addres
btDot = "D0:C5:55:9F:C5:C4"

dash = robot(btDash)
dash.reset()

running = False

def example():
  global running
  running = True
  thread.start_new_thread(shakeHead, ())
  thread.start_new_thread(Disco, ())
  while not (sys.stdin in select.select([sys.stdin], [], [], 0)[0]):
      dash.setWheelSpeed(200)
      while (dash.leftDistanceSensor < 7) & (dash.rightDistanceSensor < 7) & (not (sys.stdin in select.select([sys.stdin], [], [], 0)[0])):
        pass
      if dash.leftDistanceSensor < dash.rightDistanceSensor:
        dash.turn(-90,1000)
      else:
        dash.turn(90,1000)
      time.sleep(1)
  running = False
  dash.stopWheels()
  dash.reset()
  time.sleep(2)
      
def shakeHead():
    global running
    step = 45
    pos = 90
    while running:
        pos += step
        if (pos < -90) | (pos > 90):
            pos -= (2* step)
            step = -step
        dash.moveHeadY(0)
        dash.moveHeadX(pos)
        time.sleep(1)

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
        dash.colorAll(red, green, blue, red, green, blue, red, green, blue)
        
print("Press {enter} to stop demo")
example()
dash.disconnect()