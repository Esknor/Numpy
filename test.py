#!/usr/bin/python
from sympy.plotting import plot3d
from sympy import *
x = Symbol('x')
y = Symbol('y')
plot3d(sin(x*10)*cos(y*5) - x*y, (x, -1, 1), (y, -1, 1), nb_of_points_x=100, nb_of_points_y=100)
#a = Rational(2)**50/Rational(10)**50
#print(a)
