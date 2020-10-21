from bibliopixel.layout import *
from bibliopixel.animation import Animation

class CubeAnimation(Animation):

    _led = None

    def __init__(self, led):
        #The base class MUST be initialized by calling super like this
        super(Animation, self).__init__()
        self._led = led

    # override to write out word for each frame in the animation
    def step(self, amt = 1):
      self._led.set(1,1,1,(255,0,0))