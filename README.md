# DoesItFit
## Does it?
Let's imagine a common problem: You've got a closet with an angled side (or an angled room wall) and you have no idea whether your box (or cupboard) is fitting inside or not. Instead of calculating it with mathematical functions you could just type in your dimensions and try out different box sizes. Wouldn't it be great?

This program tells you if it's fitting! But remember: It also tests if it fits by rotating around the z-axis.

## Ready to go!
Just run the python program via command line. Enter your closet dimensions. Immediatly you get the optimum values.
Now you're inside an infinite loop, where you can type in box dimensions and let them test.
The program tells you whether it fits or not.

## Extend it!
DoesItFit is usable as a python3 module. To initialize it run the code below.
```python
import doesItFit

cupboard = doesItFit.Outer(height, width, lower depth, upper depth)
box = doesItFit.Inner(height, width, depth)
```

To get the maximum height at a specific depth of the cupboard, run the following command:
```python
cupboard.height_at(depth)
```

To get the values of a maximized volume, run this code. It gives back a dictionary with the keys "height", "width", "depth", "angle", "area" and "volume".
```python
cupboard.data()
```

To test if the box fits inside, type:
```python
box.fit(cupboard)
```
