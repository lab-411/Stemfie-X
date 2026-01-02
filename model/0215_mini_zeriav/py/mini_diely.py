import sys
sys.path.append("../../../") 

from lib import *
from lib.utils import *
from lib.tires import *

#-----------------------------------------------------------------------
# podvozok a kolesa
#-----------------------------------------------------------------------

b1 = Brace(9).Rx()
b2 = Beam_Block(3).Rz()
b1.export_step("brace_B_09")
b2.export_step("block_B_03")

t = Tire_01(3,1.5)
t.tire.export_step('tire_T_01_03_15')
t.disc.export_step('tire_D_01_03_15')

#-----------------------------------------------------------------------
# kabina 
#-----------------------------------------------------------------------
# kabina
b8 = BU_PolyLine([ [0,0], [5,0], [5,4], [2,4], [0,1], [0,0] ], 1/4)
hh = Hole_List( [[0,0], [1,0], [2,0], [3,0], [4,0], [4,1], [4,2], [4,3], [3,3], [2,3]]).BU_Tx(1/2).BU_Ty(1/2)
bb = BU_PolyLine([ [2/3,1], [3.5,1], [3.5,3], [2,3], [2/3,1]], 1/2)
b8.D([hh,bb ])

# strecha a podlaha
b6 = Beam_U_Block(5,3, hy=1/2)
b7 = Beam_U_Block(2,3, hy=1/4)

b6.export_step("block_U_05_03")
b7.export_step("block_U_02_03")
b8.export_step("block_X_05_04")

#-----------------------------------------------------------------------
# rameno, kladka a vystuze
#-----------------------------------------------------------------------
b5 = Brace(15).Rx()

pp = Pulley_A(1.5, 0.9)

c1 = BU_Cylinder(1,1.5)
ax = BU_Axe(3)
c1.D(ax)

c3 = BU_Cylinder(1, 1/2).BU_Tz(1/2).Rx()
c4 = BU_Cylinder(1, 1).BU_Tz(1/2).Rx()

w1=Wheel_A(2)
w1.D(ax)

w2=Wheel(1,1/4,1/2)
w2.D(ax)

w1.export_step('wheel_A_15_14')
w2.export_step('wheel_B_02_14')
c1.export_step('base_C_01_15')
c3.export_step('base_C_01_12')
c4.export_step('base_C_01_01')
b5.export_step("brace_B_15")
pp.export_step('pulley_A_15')





ct = Construct('tire_disc')
ct.add(t.tire, "black")
ct.add(t.disc, "khaki")
ct.export_step()


