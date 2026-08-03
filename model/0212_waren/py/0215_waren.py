# 21.10.2025
# diely pre velky most nosnik typu Waren
#
# viewer
# f3d --watch --bg-color 1,1,1 --grid-absolute coupler_32.step

import sys
sys.path.append("../../../") 

from lib import *
from lib.utils import *


# T-spojka
b1 = Brace(3)
b2 = Brace(2).Rz().BU_Tx(1)
b1.U(b2)
b1.export_step('../parts/brace_T_03_02')

# horna vystuha
b4 = Beam_U_Block(1, 5, 1/4, 1/2)   # 4x3 BU U-Shape plate 
b4.export_step('../parts/block_U_01_05_14_12')

# spojka - platna
b5 = Brace_Plate(3, 2, center=False)
b5.export_step('../parts/brace_P_03_02_14')

# sikme vystuhy
b6 = Brace(11)
h2 = Hole_Slot(2, 3/4)
h3 = Hole_Slot(2, 3/4).BU_Tx(9)
b6.D([h2,h3])
b6.export_step('../parts/brace_B_11_07_02')


# spojky a vystuhy
b7 = Brace(8)
b7.export_step('../parts/' + b7.name)

b8 = Brace(4)
b8.export_step('../parts/' + b8.name)

b9 = Brace(3)
b9.export_step('../parts/' + b9.name)


