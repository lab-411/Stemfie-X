import sys
sys.path.append("../../../") 

from lib import *
from lib.utils import *

#-----------------------------------------------------------------------
# zakladna doska

rg = Ring_Gear(90, 1/2, 1/4+1/8)
bs = BU_Cube([10, 10, 1/4]).BU_Tz(1/4/2)  
cc = BU_Cylinder(9+1/4,1, hole=False, center=True) 

ar = array([ [-4,-4], [-4,-3], [-3,-4],
              [5, 5], [ 5, 4], [ 4, 5], 
              [5,-4], [ 5,-3], [ 4,-4],
              [-4,5], [-4, 4], [-3, 5]]) -[1/2,1/2]

hh = Hole_List(ar)

bs.D([cc, hh])
bs.U([rg])
bs.export_step('../parts/sp_base_90')

#-----------------------------------------------------------------------
# koleso 40 zubov
sg = Spur_Gear(40, bore=2.5)
c2 = BU_Cylinder(3+2/4, 1/2, hole=False, center=True).BU_Tz(1/2) 
sg.D(c2)

dp = 60/180*pi
arr = []
for i in range(6,22):
    x = (i*0.07)*cos(i*dp)
    y = (i*0.07)*sin(i*dp)
    arr.append( BU_Cylinder(.25, 1, hole=False, center=True).BU_Txy(x,y) )

for i in range(6):
    x = (1.22)*cos(i*dp + pi/6)
    y = (1.22)*sin(i*dp + pi/6)
    arr.append( BU_Cylinder(0.8, 1, hole=False, center=True).BU_Txy(x,y) )   

sg.D(arr)
sg.export_step('../parts/sp_gear_40')

#-----------------------------------------------------------------------
# koleso 50 zubov
sg = Spur_Gear(50, bore=2.5)
c2 = BU_Cylinder(4+1/2, 1/2, hole=False, center=True).BU_Tz(1/2) 
sg.D(c2)

dp = 60/180*pi
arr = []
for i in range(6,22):
    x = (i*0.092)*cos(i*dp)
    y = (i*0.092)*sin(i*dp)
    arr.append( BU_Cylinder(.25, 1, hole=False, center=True).BU_Txy(x,y) )

for i in range(6):
    x = (1.55)*cos(i*dp + pi/6)
    y = (1.55)*sin(i*dp + pi/6)
    arr.append( BU_Cylinder(1, 1, hole=False, center=True).BU_Txy(x,y) )   

sg.D(arr)
sg.export_step('../parts/sp_gear_50')

#-----------------------------------------------------------------------
# koleso 65 zubov

sg = Spur_Gear(65, bore=2.5)
c2 = BU_Cylinder(5+1/2+1/8, 1/2, hole=False, center=True).BU_Tz(1/2) 
sg.D(c2)

dp = 60/180*pi
arr = []
for i in range(6,22):
    x = (i*0.12)*cos(i*dp)
    y = (i*0.12)*sin(i*dp)
    arr.append( BU_Cylinder(.25, 1, hole=False, center=True).BU_Txy(x,y) )

for i in range(6):
    x = (1.9)*cos(i*dp + pi/6)
    y = (1.9)*sin(i*dp + pi/6)
    arr.append( BU_Cylinder(1.4, 1, hole=False, center=True).BU_Txy(x,y) )   

sg.D(arr)
sg.export_step('../parts/sp_gear_65')
