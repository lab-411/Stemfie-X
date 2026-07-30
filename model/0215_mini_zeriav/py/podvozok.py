'''
mini-zeriav 

verzia 2.0
zostava podovzku
'''


import sys
sys.path.append("../") 

from lib import *
from lib.utils import *
from lib.tires import *

#-----------------------------------------------------------------------
# podvozok a kolesa
#-----------------------------------------------------------------------

# radius dier pre AURAPOL. 215°C
HR = 4.25/2

b1 = Brace(9, hole_rad=HR)             # 2x bocnica
b2 = Beam_Block(3)                     # 1x priecny nosnik


# uprava nosnika kabiny pre os otacania kabiny
# zvecsenie otvorov pre os, oba v strede
b3  = Beam_Block([3,2,1])                   # 1x nosnik kabiny
ax1 = BU_Axe(3,radius=HR).BU_Tx(1.5).BU_Ty(0.5)
ax2 = BU_Axe(3,radius=HR).BU_Tx(1.5).BU_Ty(1.5)
b3.D([ax1,ax2])
ax3 = BU_Axe(5)
ax2.export_step("../parts/axis_3")

b1.export_step("../parts/" + b1.name)
b2.export_step("../parts/" + b2.name)
b3.export_step("../parts/" + b3.name)

# vymedzenie kabiny
b6 = Brace(1,1/2, hole_rad=HR )
b6.export_step('../parts/' + b6.name)


# pomocna os pre zobrazenie
ax4 = BU_Axe(3, radius=HR)
ax5 = BU_Axe(6, radius=HR)
ax4.export_step('../parts/axis_30')
ax5.export_step('../parts/axis_60')

# os napravy pre vykreslenie zostavy
ax3 = BU_Axe(5)
ax3.export_step("../parts/axis_5")

t = Tire_01(3,1.5)
t.tire.export_step('../parts/tire_T_01_03_15')
t.disc.export_step('../parts/tire_D_01_03_15')


