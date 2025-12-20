# 21.10.2025
# diely pre velky most nosnik typu Waren
#
# viewer
# f3d --watch --bg-color 1,1,1 --grid-absolute coupler_32.step

import sys
sys.path.append("/home/pf/ownCloud/Share-Notebooks/9920-Jupyter-Book/0110_stemfie_x/") 
 
from lib import *

class Coupler_32(Stemfie_X):
    def __init__(self, scr=False, FC=False):   
        Stemfie_X.__init__(self) 
        self.obj = Brace_Plate(3, 2, center=False).obj
        s1 = array([  [0,1],  [1,0],  [1,1], [2,1] ]) 
        h1 = Hole_List(s1)
        h2 = Hole_Slot(1+1/2, 1/2).Rz(45) 
        h3 = Hole_Slot(1+1/2, 1/2).Rz(135) .BU_Tx(2)
        self.D([h1, h2, h3])
h1 = Coupler_32()
h1.export_step('../parts/coupler_X_03_02')

# T-spojka
b1 = Brace(3)
b2 = Brace(2).Rz().BU_Tx(1)
b1.U(b2)
b1.export_step('../parts/brace_T_03_02')

# vystuha
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
