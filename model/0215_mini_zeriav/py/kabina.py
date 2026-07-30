import sys
sys.path.append("../") 

from lib import *
from lib.utils import *
from lib.tires import *


HR = 4.25/2

#-----------------------------------------------------------------------
# kabina 
#-----------------------------------------------------------------------
# kabina
b8 = BU_PolyLine([ [0,0], [5,0], [5,4], [2,4], [0,1], [0,0] ], 1/4)
hh = Hole_List( [[0,0], [1,0], [2,0], [3,0], [4,0], [4,1], [4,2], [4,3], [3,3], [2,3]]).BU_Tx(1/2).BU_Ty(1/2)
bb = BU_PolyLine([ [2/3,1], [3.5,1], [3.5,3], [2,3], [2/3,1]], 1/2)
b8.D([hh,bb ])
b8.export_step("../parts/block_X_05_04")

# strecha a podlaha
b6 = Beam_U_Block(5,3, hy=1/2)
b7 = Beam_U_Block(2,3, hy=1/4)
b6.export_step("../parts/block_U_05_03")
b7.export_step("../parts/block_U_02_03")


#-----------------------------------------------------------------------
# rameno, kladka a vystuze
#-----------------------------------------------------------------------
#b5 = Brace(17)
#b5.export_step("../parts/brace_B_17")

#pp = Pulley_A(1.5, 0.9)
#pp.export_step('../parts/pulley_A_15')
#c1 = BU_Cylinder(1,1.5)
#ax = BU_Axe(3)
#c1.D(ax)
#c1.export_step('../parts/base_C_01_15')

#c3 = BU_Cylinder(1, 1/2).BU_Tz(1/2)
#c4 = BU_Cylinder(1, 1).BU_Tz(1/2)
#c3.export_step('../parts/base_C_01_12')
#c4.export_step('../parts/base_C_01_01')


ax = BU_Axe(3,radius=HR)
pp = BU_Axe(3,radius=1).BU_Tx(0.75)
w1 = Wheel_A(2)
w1.D([ax, pp])
w1.export_step('../parts/wheel_A_15_14')

w2=Wheel(1,1/4,1/2)
w2.D(ax)
w2.export_step('../parts/wheel_B_02_14')

c1 = BU_Cylinder(1,1.5)
ax = BU_Axe(3, radius=4.35/2)
c1.D(ax)
c1.export_step('../parts/base_C_01_13')

c2 = BU_Cylinder(1,1.25)
ax = BU_Axe(3, radius=4.35/2)
c2.D(ax)
c2.export_step('../parts/base_C_01_13')



