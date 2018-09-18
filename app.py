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
    
    def data(self):
        d = -self.__b/(2*self.__a)
        w = self.width
        h = self.height_at(d)
        if h > self.height:
            d = self.upper
            h = self.height
        return {"Height": h, "Width": self.width, "Depth": d, "Angle": self.angle,"Area": h*d, "Volume": h*w*d}

class Box():
    
    def __init__(self,height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
    
    def fit(self, cupboard):
        if ( self.height > cupboard.height ):
            return False
        
        if ( (self.width < cupboard.width and self.height < cupboard.height_at(self.depth)) or
             (self.depth < cupboard.width and self.height < cupboard.height_at(self.width)) ):
            return True
        else:
            return False

print("The Cupboard\n############")
cupboard = Cupboard(
        int(input("Height:      ")),
        int(input("Width:       ")),
        int(input("Lower Depth: ")),
        int(input("Upper Depth: "))
    )

print("\nThe Box\n#######")
box = Box(
        int(input("Height:      ")),
        int(input("Width:       ")),
        int(input("Depth:       "))
    )
print("\n")

if box.fit(cupboard):
    print("The box does fit inside the cupboard.")
else:
    print("The box does *NOT* fit inside the cupboard.")
print("\n")

print("Values of the greatest volume:")
print("height x width x depth: {:.2f} x {:.2f} x {:.2f}".format(
        cupboard.data()["Height"],
        cupboard.data()["Width"],
        cupboard.data()["Depth"])
    )
print("volume:                 {:.2f}".format(cupboard.data()["Volume"]))
print("cut-through area:       {:.2f}".format(cupboard.data()["Area"]))
