from shape.SnakedCube import SnakedCube
from animation.CubeRain import CubeRain
from animation.CubeBloom import CubeBloom
from animation.CubePulse import CubePulse
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
# fps = 24
# color      = (0,255,0)
# anim       = CubeRain(layout, tail=tail, growthRate=growthRate, color=color)
# anim.run(fps=fps)

# rain drops
# tail       = 1 # tail of rain animation
# growthRate = 1 # how many rain drops
# fps = 24
# color      = (0,255,255)
# anim       = CubeRain(layout, tail=tail, growthRate=growthRate, color=color, clouds=True)
# anim.run(fps=fps)

# sphere
# fps = 24
# max_radius = z / 2 # the most the circle will expand to
# anim = CubeSphere(layout, max_radius=max_radius)
# anim.run(fps=fps)

# fireworks
# fps = 24
# anim = Firework(layout)
# anim.run(fps=fps)

# pulse
fps = 24
anim = CubePulse(layout)
anim.run(fps=fps)

# laser
# fps = 24
# anim  = Laser(layout)
# anim.run(fps=fps)

# laser up
# fps = 24
# anim  = LaserUp(layout)
# anim.run(fps=fps)

# game of life
# fps = 24
# anim = CubeGameOfLife(layout)
# anim.run(fps=fps)

# bloom
# fps = 24
# anim = CubeBloom(layout)
# anim.run(fps=fps)

# wave spiral
# fps = 24
# anim = WaveSpiral(layout)
# anim.run(fps=fps)
