#!/usr/bin/python3

import argparse
import sys
import math

opt = int(sys.argv[1])
xp = float(sys.argv[2])
yp = float(sys.argv[3])
zp = float(sys.argv[4])
xv = float(sys.argv[5])
yv = float(sys.argv[6])
zv = float(sys.argv[7])
p = float(sys.argv[8])
    
def result(delta, a, _b) :
    if delta < 0 :
        print("No intersection point.")
    elif delta == 0 :
        print("1 intersection point:")
        t = (-_b / (2 * a))
        xx = xp + xv * t
        yy = yp + yv * t
        zz = zp + zv * t
        print("({0:.3f}, {1:.3f}, {2:.3f})".format(xx, yy, zz))
    elif delta > 0 :
        print("2 intersection points:")
        t = (-_b + math.sqrt(delta) / (2 * a))
        xx = xp + xv * t
        yy = yp + yv * t
        zz = zp + zv * t
        print("({0:.3f}, {1:.3f}, {2:.3f})".format(xx, yy, zz))
        t = (-_b - math.sqrt(delta) / (2 * a))
        xx = xp + xv * t
        yy = yp + yv * t
        zz = zp + zv * t
        print("({0:.3f}, {1:.3f}, {2:.3f})".format(xx, yy, zz))

def sphere() :
    print("Sphere of radius", p)
    print("Line passing through the point (",int(xp),", ",int(yp),", ",int(zp),") and parallel to the vector (",int(xv),", ",int(yv),", ",int(zv),")", sep="")
    a = math.pow(xv, 2) + math.pow(yv, 2) + math.pow(zv, 2)
    x_2 = 2 * xp * zv
    y_2 = 2 * yp * yv
    z_2 = 2 * zp * zv
    _b = x_2 + y_2 + z_2
    _c = math.pow(xp, 2) + math.pow(yp, 2) + math.pow(zp, 2) - math.pow(p, 2)

    if a == 0 :
        sys.exit(84)
    
    delta = math.pow(_b, 2) - 4 * a * _c
    result(delta, a, _b)
        

def cylinder() :
    print("Cylinder of radius", p)
    print("Line passing through the point (",int(xp),", ",int(yp),", ",int(zp),") and parallel to the vector (",int(xv),", ",int(yv),", ",int(zv),")", sep="")
    a = math.pow(xv, 2) + math.pow(yv, 2)
    x_2 = 2 * xp * zv
    y_2 = 2 * yp * yv
    z_2 = 2 * zp * zv
    _b = x_2 + y_2 + z_2
    _c = math.pow(xp, 2) + math.pow(yp, 2) - math.pow(p, 2)
    delta = math.pow(_b, 2) - 4 * a * _c
    result(delta, a, _b)
    if a == 0 :
        if zv == 0 :
            sys.exit(84)
        else : 
            if _c == 0 : 
                print("There is an infinite number of intersection points.")

def cone() :
    print("Cone with a",int(p) ,"degree angle")
    print("Line passing through the point (",int(xp),", ",int(yp),", ",int(zp),") and parallel to the vector (",int(xv),", ",int(yv),", ",int(zv),")", sep="")

if not len(sys.argv) > 1:
    sys.exit(84)
if opt == 1 :
    sphere()
elif opt == 2 :
    cylinder()
elif opt == 3 :
    cone()       
else :
    sys.exit(84)