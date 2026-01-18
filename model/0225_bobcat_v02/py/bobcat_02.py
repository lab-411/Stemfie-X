'''
Diely pre Bobcat - nakladac

f3d --watch --background-color 1,1,1 --grid-absolute  <your file-name>.step
'''

import sys
sys.path.append("../../../")

from lib import *
from lib.utils import *
from lib.tires import *

#-----------------------------------------------------------------------
# podvozok a kolesa
#-----------------------------------------------------------------------

b1 = Brace(5)
b2 = Beam_Block(3)
b1.export_step("../parts/brace_B_05")
b2.export_step("../parts/block_B_03")

t = Tire_01(3,1.5)
t.tire.export_step('../parts/tire_T_01_03_15')
t.disc.export_step('../parts/tire_D_01_03_15')

#-----------------------------------------------------------------------
# podlaha kabiny a kryt motora
#-----------------------------------------------------------------------

# strecha a podlaha
b6 = Beam_U_Block(7,3, hy=1/4)
b7 = Beam_U_Block(2,3, hy=1/4)

b6.export_step("../parts/block_U_07_03")
b7.export_step("../parts/block_U_02_03")

#-----------------------------------------------------------------------
# kabina
#-----------------------------------------------------------------------

# zadna stena kabiny
y1 = BU_Cube([3+1/2, 1, 1/4], center=True).BU_Tz(1/4/2)
yh = Hole_List( [[0,0] ]).BU_Tz(-1/2)
y1.D(yh)

y2 = BU_Cube([2.5, 1/2, 2], center=True).BU_Tz(1+1/4).BU_Ty(1/4)
y3 = BU_Cube([2, 1/2, 2-1/4], center=True).BU_Tz(1+1/8).BU_Ty(1/4)
y1.U([y2])
y1.D(y3)

y1.export_step("../parts/user_Y_35_01")

# boky kabiny - pravy
y10 = BU_PolyLine([ [-1, 1/4], [3,1/4], [3,4+1/4], [0,4+1/4], [-1,1], [-1,1/4] ], 1/4)
y11 = BU_PolyLine([ [0, 1], [2.5,1], [2.5,4], [0+1/4,4], [-2/3,1] ], 1/2)
y10.D(y11)
y12 = BU_Cube([4, 3/4, 1/2], center=False).BU_Tz(1/4).BU_Ty(1/4).BU_Tx(-1)
y10.U(y12)
yh = Hole_List([ [1/2,0], [1+1/2,0], [2+1/2,0],  [3+1/2,0] ]).Rx().BU_Tz(1/4).BU_Ty(3/4).BU_Tx(-1)
y10.D(yh)
y10.export_step("../parts/user_P_03_14")

# boky kabiny - lavy
y20 = BU_PolyLine([ [-1, 1/4], [3,1/4], [3,4+1/4], [0,4+1/4], [-1,1], [-1,1/4] ], 1/4)
y21 = BU_PolyLine([ [0, 1], [2.5,1], [2.5,4], [0+1/4,4], [-2/3,1] ], 1/2)
y20.D(y21)
y22 = BU_Cube([4, 3/4, 1/2], center=False).BU_Tz(-2/4).BU_Ty(1/4).BU_Tx(-1)
y20.U(y22)
yh = Hole_List([ [1/2,0], [1+1/2,0], [2+1/2,0],   [3+1/2,0]  ]).Rx().BU_Tz(0).BU_Ty(3/4).BU_Tx(-1)
y20.D(yh)
y20.export_step("../parts/user_P_03_24")

# strecha
y30 = BU_Cube([2, 3, 1/4], center=True).BU_Tz(1/4/2)
y31 = BU_Cube([2.5, 3.5+1/4, 1/4], center=True).BU_Tz(1/4+1/4/2).BU_Ty(1/4)
y30.U(y31)
y30.export_step("../parts/user_S_20_40")

#-----------------------------------------------------------------------
# predna maska
#-----------------------------------------------------------------------

y40 = BU_Cube([2+1/2, 1, 3/4], center=True).BU_Tz(1/2+1/4/2)
y41 = BU_PolyLine([ [0,0], [1/2,0], [1/2,1], [0,0]], 3).Rz().Ry().BU_Tx(-1-1/2).BU_Ty(-1)
y40.U(y41)
yh4 = Hole_List( [[0,0], [-1,0], [1,0] ]).BU_Tz(0)
y40.D(yh4)
y40.export_step("../parts/user_S_32_10")


#-----------------------------------------------------------------------
# bocnica
#-----------------------------------------------------------------------

b8 = BU_PolyLine([ [-1/2,0], [7,0], [7,2], [5,2], [4.5,1], [0,1], [-1/2,0] ], 1/4)
hh = Hole_List( [[0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [6,1], [5,1]]).BU_Tx(1/2).BU_Ty(1/2)

b8.D([hh ])
b8.export_step("../parts/block_X_07_04")

#-----------------------------------------------------------------------
# radlica, rameno  a drziak radlice
#-----------------------------------------------------------------------
# radlica
phi=70
r0 = BU_PolyLine([ [0, -1-1/2], [0, 1+1/2], [sin(phi/180*pi)*3.0, -1.5+cos(phi/180*pi)*3] ], 1/4).Ry(-90).BU_Tx(3.5).BU_Tz(1/4).MKy()
r1 = BU_Cube([7, 3, 1/4], center=True).BU_Tz(1/4/2)

xh = Hole_List( [[1,0], [0,0], [-1,0] ]).BU_Tx(3.5).BU_Ty(1)
r2 = BU_Cube([7, 3, 1/4], center=False)
r2.D(xh)
r2.Rx(phi).BU_Tz(1/4).BU_Ty(-1-1/2).BU_Tx(-3.5)

r3 = BU_Cylinder(1/2,7, angle=270, hole=False).Rz(180).Ry().BU_Tz(1/2/2).BU_Ty(-1.5)
r1.U([r0,r2,r3])
r1.export_step("../parts/user_R_35_01")


# drziak radlice - spodok
x1 = BU_Cube([3+1/2, 1, 1/4], center=True).BU_Tz(1/4/2)
# bocne ucho + kopia
x2 = BU_Cube([1, 1, 1/2], center=True).BU_Tz(1/2/2).BU_Tx(3/2-1/4)
x3 = BU_Cylinder(1,1, hole=False).Ry().BU_Tz(1/2).BU_Tx(3/2-1/4)
xd = BU_Axe(2).Ry().BU_Tz(1/2).BU_Tx(1+1/2)
hh = Hole(1/2).BU_Tx(1)
x2.U([x3])
x2.D([xd,hh])
x2.MKy()

xh = Hole_List( [[1,0], [0,0], [-1,0] ]).BU_Tz(-1/2)
x1.D(xh)
x1.U([x2]).Rz()
x1.export_step("../parts/user_X_35_01")


# ramena radlice, lava a prava strana
b9 = Brace(7)
c10 = BU_Cylinder(1, 3/4).BU_Tz(1/2).BU_Tx(6)
b9.U(c10)
b10 = Brace(4)
c11 = BU_Cylinder(1, 3/4).BU_Tz(1/2).BU_Tx(3)
b10.U(c11)
b10.Rz(120)
b9.U(b10)
b9.export_step("../parts/user_H_07_04_L")
b9.Mx()
b9.export_step("../parts/user_H_07_04_R")
