#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:58:15 2024

@author: pf

Viewer:
    f3d --watch --bg-color 1,1,1 --grid-absolute <name>.step

Color names:
    https://cadquery.readthedocs.io/en/latest/assy.html#assembly-colors
"""

import sys
sys.path.append("../../../../Stemfie-X/") 

from lib import *
from lib.utils import *

from lib.wheels import *


w1=Wheel(1, 1/4, 0).BU_Tz(-1/4)
h=3/4                   # vyska uchytenia
d=3/4                   # dlzka uchytenie
z=1/4   # 1/3 nezasahuje do hriadele, 1/3 zasahuje
cc = BU_Cylinder(1,h, 180, False). BU_Tz(h/2)
bb = BU_Cube([1,d,h]). BU_Tz(h/2).BU_Ty(-d/2)
ax = BU_Cylinder(4.1/BU,3*h, 360, False)

m3h = BU_Cylinder(0.6, 1/4, hole=False).BU_Tz(3/4/2+1/8)
m3s = BU_Cylinder(0.3, 1-1/4, hole=False)#.BU_Tz(-1/2)
m3m = BU_Cylinder(0.6, 1/4, hole=False).BU_Tz(-3/4/2-1/8)
m3h.U([m3s, m3m]).Ry().BU_Tz(h/2).BU_Ty(-1/3)#+1/8+1/32)


s1 = BU_Cube([0.06,1,1]).BU_Tz(1/2).BU_Ty(-1/2)
s2 = BU_Cube([1,1+1/4,0.05]).BU_Tz(0.05/2).BU_Tx(1/2).BU_Ty(-1/2)

cc.U([bb])
cc.D([ax,m3h,s1,s2])
cc.U(w1)
cc.export_step('uchytenie')

#m3h.export_step('m3')




#bc = BU_Cube([1,3/4,d]).BU_Tz(-d/2).BU_Ty(-1/2)
#c1 = BU_Cube([1,2,.025]).BU_Tz(-0.025/2).BU_Tx(-0.5)
#c2 = BU_Cube([.05,1,1]).BU_Tz(-1/2).BU_Ty(-1/2)
#c3 = BU_Bar(2)

#s1 = BU_Cylinder(0.6, 1/4, hole=False)
#s2 = BU_Cylinder(0.3, 1, hole=False).BU_Tz(-1/2)
#s1.U(s2).Ry(-90).Rz(180).BU_Tx(1/2).BU_Tz(-0.4).BU_Ty(-1/2)

#w1.U([bc])
#w1.D([c1, c2, c3,s1])
#w1.export_step('w12')
