from shape.cube import Cube
from animation.Rain import RainBow
from bibliopixel.drivers.PiWS281X import PiWS281X
import sys

#create biblio pixel driver and led
thread     = False   # display updates to run in background thread
brightness = 100     # brightness 0-255
x          = 8    # number of leds in the team name
y          = 8    # number of leds in the timer section
z          = 8     # number of leds in for a single number
driver     = PiWS281X(8*8*8)
layout     = Cube(driver, 8, 8, 8)
anim       = RainBow(led)
anim.run()
