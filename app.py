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
        
        # calculate coefficients for mathematical func
        self.__a = height/(upper-lower)
        self.__b = height*(1 - upper/(upper-lower))
    
    def height_at(self, depth):
        # mathematical func that describes the cuboard
        result = self.__a * depth + self.__b
        if result > self.height:
            result = self.height
        return result
    
    def data(self):
        d = -self.__b/(2*self.__a)
        w = self.width
        h = self.height_at(d)
        if h >= self.height:
            d = self.upper
        return {"Height": h, "Width": self.width, "Depth": d, "Angle": self.angle,"Area": h*d, "Volume": h*w*d}

class Box():
    
    def __init__(self,height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
    
    def fit(self, cupboard):
        if ( (self.width < cupboard.width and self.height < cupboard.height_at(self.depth)) or
             (self.depth < cupboard.width and self.height < cupboard.height_at(self.width)) ):
            return True
        else:
            return False

print("The Cupboard\n############")
cupboard = Cupboard(
        float(input("Height:      ")),
        float(input("Width:       ")),
        float(input("Lower Depth: ")),
        float(input("Upper Depth: "))
    )
print("It is angled by {} degrees".format(
        np.degrees(cupboard.data()["Angle"])
    ))

print("\nWhats the maximum possible box volume?")
print("Height x Width x Depth: {:.2f} x {:.2f} x {:.2f}".format(
        cupboard.data()["Height"],
        cupboard.data()["Width"],
        cupboard.data()["Depth"])
    )
    
print("Volume:                 {:.2f}".format(cupboard.data()["Volume"]))
print("Cut-through area:       {:.2f}".format(cupboard.data()["Area"]))
print("")

while(True):
    print("Box Dimensions\n##############")
    box = Box(
            float(input("Height:      ")),
            float(input("Width:       ")),
            float(input("Depth:       "))
        )
    
    if box.fit(cupboard):
        print("Does it fit? YES!")
    else:
        print("Does it fit? NO!")
    
    print("\nTo exit type 'exit'. To continue press 'Enter'.")
    if input().lower() == "exit":
        break
