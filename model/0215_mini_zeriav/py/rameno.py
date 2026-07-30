import sys
sys.path.append("../") 

from lib import *
from lib.utils import *
from lib.tires import *



#-----------------------------------------------------------------------
# rameno, kladka a vystuze
#-----------------------------------------------------------------------

# radius dier pre AURAPOL. 215°C
HR = 4.25/2

#rameno
b5 = Brace(17, hole_rad=HR)
b5.export_step('../parts/' + b5.name)

# kladka
pp1 = Pulley_A(1.5, 0.95)
ax3 = BU_Axe(2, radius=HR)
pp1.D(ax3)
pp1.export_step('../parts/' + b6.name)

# spojka
b6 = Brace(2,1)
b6.export_step('../parts/' + b6.name)

# pomocna os pre zobrazenie
ax1 = BU_Axe(1.5, radius=HR)
ax2 = BU_Axe(1.5, radius=HR)
ax1.export_step('../parts/axis_15')

# nosnik s ozubenym hrebenom
bb  = Beam_Block(2, [False, True, True])
rx  = Rack_Gear(3, 1, 1/4).Rx().BU_Tz(1/2-1/8).BU_Tx(2).BU_Ty(1)

ax1.BU_Tz(1/2).BU_Txy(1+1/2,1/2)
ax2.Rx().BU_T([1/2, 1/2, 1/2])
hh = Hole().BU_T([2+1/2, 1/2,0])
rx.U([bb])
rx.D([ax1, ax2, hh])
rx.export_step('../parts/rack_2')

# podpera
c2 = BU_Cylinder(1,0.95)
c3 = BU_PolyLine([ [0,0], [0, 1/3], [2, 1/3], [2+1/3, 1/3/2], [2,0], [0,0]  ], height=0.95)
c3.BU_Tz(-1/2).BU_Tx(1/4).BU_Ty(-1/3/2)

ax4 = BU_Axe(2, radius=HR)
c2.U(c3)
c2.D(ax4)
c2.export_step('../parts/podpera')


