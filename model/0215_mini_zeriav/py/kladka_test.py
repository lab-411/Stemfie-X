#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:58:15 2024

@author: pf

Viewer:
    f3d --watch --bg-color 1,1,1 --grid-absolute <name>.step

Color names:
    https://cadquery.readthedocs.io/en/latest/assy.html#assembly-colors
"""

import sys
sys.path.append("../") 

from lib import *
from lib.utils import *

#from lib.pulley import *

class Pulley_01(Stemfie_X):
    '''
    Plna kladka
    '''
    
    def __init__(self, diam=1, thick=1, diam2=1/2):
        Stemfie_X.__init__(self) 
    
        d1 = diam*self.BU       # vonkajsi priemer
        d2 = d1-diam2*self.BU   # vnutorny priemer kladky
        h  = thick*self.BU      # hrubka kladky 
        
        # lava a prava strana kladky
        p1 = BU_Component()
        p1.obj = (p1.obj
            .circle(d1/2)
            .workplane(offset=h/2)
            .circle(d2/2)
            .loft(combine = True)
        )
        
        p2 = BU_Component()
        p2.obj = (p2.obj
            .circle(d2/2)
            .workplane(offset=h/2)
            .circle(d1/2)
            .loft(combine = True)
            .translate([0,0,h/2])
        )
        self.U([p1,p2])
        #self.T([0,0,-h/2])
        
        # specifikacia podla priemerov kladiek
        cc = BU_Cylinder(1, 1).BU_Tz(1/2)
        #cd = BU_Cylinder(0.5, 1).BU_Tz(1/2)
        #self.D(cd)
        hh = Hole(2, 2.1)#.BU_Tz(1/2)
        self.D(hh)


class Pulley_02(Stemfie_X):
    '''
    Plna kladka
    '''
    
    def __init__(self, diam=1, thick=1, diam2=1/2):
        Stemfie_X.__init__(self) 
    
        d1 = diam*self.BU       # vonkajsi priemer
        d2 = d1-diam2*self.BU   # vnutorny priemer kladky
        h  = thick*self.BU      # hrubka kladky 
        
        # lava a prava strana kladky
        p1 = BU_Component()
        p1.obj = (p1.obj
            .circle(d1/2)
            .workplane(offset=h/2)
            .circle(d2/2)
            .loft(combine = True)
        )
        
        p2 = BU_Component()
        p2.obj = (p2.obj
            .circle(d2/2)
            .workplane(offset=h/2)
            .circle(d1/2)
            .loft(combine = True)
            .translate([0,0,h/2])
        )
        self.U([p1,p2])
        #self.T([0,0,-h/2])
        
        # specifikacia podla priemerov kladiek
        cc = BU_Cylinder(1, 1).BU_Tz(1/2)
        cd = BU_Cylinder(2+4/10, 1).BU_Tz(1/2+1/4)
        self.D(cd)
        self.U(cc)
        hh = Hole(2, 2.1)#.BU_Tz(1/2)
        self.D(hh)
        
        N = 8
        dp = np.pi*2/N
        hole_grid = []
        for i in range(N):
            dx = self.BU*np.cos(dp*i)
            dy = self.BU*np.sin(dp*i)
            hole_grid.append([dx,dy])

        hr = BU_Component()
        hr.obj = hr.obj.pushPoints(hole_grid) 
        hr.obj = hr.obj.circle(self.HR)
        hr.obj = hr.obj.extrude(10)
        hr.BU_Tz(-1/2)
        self.D(hr)

pp = Pulley_01(1.5, 0.9)
pp.export_step('pull_01_15')
