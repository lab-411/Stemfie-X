import sys
sys.path.append("../../../../Stemfie-X/") 

from lib import *
from lib.utils import *

# podvozok

b1 = Brace(9).Rx()
b2 = Beam_Block(3).Rz()
b3 = Beam_Block([3,3,1/4], [False, False, True])
b4 = Beam_Block([3,1,2], [False, True, True])
b5 = Brace(15).Rx()
#w2 = Wheel(2)
c1 = BU_Cylinder()
b6 = Beam_U_Block(5,3)
b7 = Beam_U_Block(2,3)

b8 = BU_Polyline([ [0,0], [5,0], [5,4], [2,4], [0,1], [0,0] ], 1/4)
hh = Hole_List( [[0,0], [1,0], [2,0], [3,0], [4,0], [4,1], [4,2], [4,3], [3,3], [2,3]]).BU_Tx(1/2).BU_Ty(1/2)
bb = BU_Polyline([ [2/3,1], [3.5,1], [3.5,3], [2,3], [2/3,1]], 1/2)
b8.D([hh,bb ])

b1.export_step("b1")
b2.export_step("b2")
b3.export_step("b3")
b4.export_step("b4")
b5.export_step("b5")
b6.export_step("b6")
b7.export_step("b7")
c1.export_step("c1")

b8.export_step("b8")

