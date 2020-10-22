from shape.snaked_cube import SnakedCube
from animation.CubeRain import CubeRain
from animation.CubeGameOfLife import CubeGameOfLife
from bibliopixel.drivers.PiWS281X import PiWS281X
import sys

#create biblio pixel driver and led
thread     = False   # display updates to run in background thread
brightness = 100     # brightness 0-255
x          = 8    # number of leds in the team name
y          = 8    # number of leds in the timer section
z          = 8     # number of leds in for a single number
driver     = PiWS281X(8*8*8)
layout     = SnakedCube(driver, 8, 8, 8)

# matrix movie animation
# tail       = 4 # tail of rain animation
# growthRate = 1 # how many rain drops
# speed      = 2 # higher the number, slower it is
# color      = (0,255,0)
# anim       = CubeRain(layout, tail=tail, growthRate=growthRate, speed=speed, color=color)
# anim.run()

# rain drops
# tail       = 1 # tail of rain animation
# growthRate = 1 # how many rain drops
# speed      = 1 # higher the number, slower it is
# color      = (0,255,255)
# anim       = CubeRain(layout, tail=tail, growthRate=growthRate, speed=speed, color=color)
# anim.run()

# game of lifeW
anim       = CubeGameOfLife(layout)
anim.run()

