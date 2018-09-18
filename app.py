#!/usr/bin/python3
#
# Test if it fits into a cupboard
#

import numpy as np

class Cupboard():
    
    def __init__(self, height, width, lower, upper):
        self.height = height
        self.width = width
        self.lower = lower
        self.upper = upper
        self.angle = np.arctan(height/(lower-upper))
        
        self.__a = height/(upper-lower)
        self.__b = height*(1 - upper/(upper-lower))
    
    def height_at(self, depth):
        return self.__a * depth + self.__b
    
    def max(self):
        d = -self.__b/(2*self.__a)
        h = self.height_at(d)
        w = self.width
        return {"Height": h, "Width": self.width, "Depth": d,"Area": h*d, "Volume": h*w*d}

class Box():
    
    def __init__(self,height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
    
    def fit(self, cupboard):
        if (self.width > cupboard.width and
                self.depth > cupboard.width):
            return False
        elif (self.height > cupboard.height_at(self.depth) and
                self.height > cupboard.height_at(self.width)):
            return False
        else:
            return True

c = Cupboard(26,50,54,32)
b = Box(31.9,50,27)
