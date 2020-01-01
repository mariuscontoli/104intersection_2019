#!/usr/bin/python3

import argparse
import sys
import math

opt = int(sys.argv[1])
xp = int(sys.argv[2])
yp = int(sys.argv[3])
zp = int(sys.argv[4])
xv = int(sys.argv[5])
yv = int(sys.argv[6])
zv = int(sys.argv[7])
p = int(sys.argv[8])

def sphere() :
    print("Sphere of radius", p)
    print("Line passing through the point (",xp,", ",yp,", ",zp,") and parallel to the vector (",xv,", ",yv,", ",zv,")", sep="")
    a = math.pow(xv, 2) + math.pow(yv, 2) + math.pow(zv, 2)
    x_2 = 2 * xp * zv
    y_2 = 2 * yp * yv
    z_2 = 2 * zp * zv
    _b = x_2 + y_2 + z_2
    _c = math.pow(xp, 2) + math.pow(yp, 2) + math.pow(zp, 2) - math.pow(p, 2)

    if a == 0 :
        sys.exit(84)

def cylinder() :
    print("Cylinder of radius", p)
    a = math.pow(xv, 2) + math.pow(yv, 2)
    x_2 = 2 * xp * zv
    y_2 = 2 * yp * yv
    z_2 = 2 * zp * zv
    _b = x_2 + y_2 + z_2
    _c = math.pow(xp, 2) + math.pow(yp, 2) - math.pow(p, 2)
    if a == 0 :
        if zv == 0 :
            sys.exit(84)
        else : 
            if _c == 0 : 
                print("Line passing through the point (",xp,", ",yp,", ",zp,") and parallel to the vector (",xv,", ",yv,", ",zv,")", sep="")
                print("There is an infinite number of intersection points.")
            else :
                print("Line passing through the point (",xp,", ",yp,", ",zp,") and parallel to the vector (",xv,", ",yv,", ",zv,")", sep="")
                print("No intersection point.")

if not len(sys.argv) > 1:
    sys.exit(84)
if opt == 1 :
    sphere()
elif opt == 2 :
    cylinder()
    ## elif args.flag == 3 :
    ## cone()       
else :
    sys.exit(84)