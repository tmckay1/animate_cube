from bibliopixel.layout import *
from bibliopixel.animation import Animation

class CubeAnimation(Animation):

    def __init__(self, layout, **kwds):
        #The base class MUST be initialized by calling super like this
        super().__init__(layout, **kwds)

    # override to write out word for each frame in the animation
    def step(self, amt = 1):
      self.layout.set(2,1,1,(255,0,0))