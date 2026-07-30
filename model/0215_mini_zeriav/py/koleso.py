import sys
sys.path.append("../") 

from lib import *
from lib.utils import *
from lib.tires import *

#-----------------------------------------------------------------------
# podvozok a kolesa
#-----------------------------------------------------------------------

class M3(Stemfie_X):
    '''
    Pnematika so zadanymi parametrami.
    Pouzitie
    q = Tire_01()
    q.tire
    q.disc
    '''
    def __init__(self, length):
        '''
        length - dlzka zavitu
        '''
        Stemfie_X.__init__(self)
        #---------------------------------------------------------------
        
        r = BU_Cylinder(2.8/BU,1,hole=False) 
        r.BU_Tz(-length/2)
        
        x = 6/BU
        h = BU_Cylinder(6/BU,x,hole=False) 
        h.BU_Tz(x/2)
        
        r.U(h)
        self.obj = r.obj
        
        
        
m3 = M3(1)
m3.export_step('../parts/m3')


t = Tire_02(3,1.5)
m3.BU_Tz(0.2).BU_Tx(0.35).BU_Ty(-0.3)
t.disc.D(m3)

#t.tire.export_step('../parts/tire_T2_01_03_15')
t.disc.export_step('../parts/tire_D2_01_03_15')




