import sys
sys.path.append("../") 

from lib import *
from lib.utils import *
from lib.tires import *

HR_AXIS  = 4.1/2 

#b1 = Brace(3, hole_rad=HR_AXIS)                # bocnica
#b1.export_step(b1.name)


bb = Beam_Block(8, [False, True, True])

ax1 = BU_Axe(2, center=False).BU_T([1/2+1,1/2, -1/2])
ax2 = ax1.copy().Rx().BU_Ty(1)

ax3 = BU_Axe(2, center=False, radius=HR_AXIS).BU_T([1/2+2,1/2, -1/2])
ax4 = ax3.copy().Rx().BU_Ty(1)

ax5 = BU_Axe(2, center=False, radius=4.2/2).BU_T([1/2+3,1/2, -1/2])
ax6 = ax5.copy().Rx().BU_Ty(1)

ax7 = BU_Axe(2, center=False, radius=4.25/2).BU_T([1/2+4,1/2, -1/2])
ax8 = ax7.copy().Rx().BU_Ty(1)

ax9 = BU_Axe(2, center=False, radius=4.3/2).BU_T([1/2+5,1/2, -1/2])
ax10 = ax9.copy().Rx().BU_Ty(1)

ax11 = BU_Axe(2, center=False, radius=4.35/2).BU_T([1/2+6,1/2, -1/2])
ax12 = ax11.copy().Rx().BU_Ty(1)

ax13 = BU_Axe(2, center=False, radius=4.4/2).BU_T([1/2+7,1/2, -1/2])
ax14 = ax13.copy().Rx().BU_Ty(1)

bb.U([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, ax13, ax14])
bb.export_step('bb_test')
