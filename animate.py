from shape.SnakedCube import SnakedCube
from animation.CubeRain import CubeRain
from animation.CubeBloom import CubeBloom
from animation.CubeSphere import CubeSphere
from animation.Firework import Firework
from animation.Laser import Laser
from animation.LaserUp import LaserUp
from animation.WaveSpiral import WaveSpiral
from animation.CubeGameOfLife import CubeGameOfLife
from bibliopixel.drivers.PiWS281X import PiWS281X
import sys

#create biblio pixel driver and led
thread     = False   # display updates to run in background thread
brightness = 100     # brightness 0-255
x          = 8    # number of leds in the team name
y          = 8    # number of leds in the timer section
z          = 8     # number of leds in for a single number
driver     = PiWS281X(x*y*z)
layout     = SnakedCube(driver, x, y, z)

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
# speed      = 2 # higher the number, slower it is
# color      = (0,255,255)
# anim       = CubeRain(layout, tail=tail, growthRate=growthRate, speed=speed, color=color, clouds=True)
# anim.run()

# sphere
speed = 5 # higher the number, slower it is
anim = CubeSphere(layout, speed=speed)
anim.run()

# fireworks
# anim = Firework(layout)
# anim.run()

# laser
# speed = 5 # higher the number, slower it is
# anim  = Laser(layout, speed=speed)
# anim.run()

# laser up
# speed = 2 # higher the number, slower it is
# anim  = LaserUp(layout, speed=speed)
# anim.run()

# game of lifeW
# anim = CubeGameOfLife(layout)
# anim.run()

# bloom
# anim = CubeBloom(layout)
# anim.run()

# wave spiral
# anim = WaveSpiral(layout)
# anim.run()
