#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:03:35 2024

@author: pf

Pulley 
Pulley_Holder
"""
from numpy import pi, sin, cos
from lib.common import *
from lib.base import *
from lib.beams import *
from lib.holes import Hole_List, Hole


from lib import *
from lib.utils import *

class Pulley_A(Stemfie_X):
    '''
    Plna kladka
    '''
    
    def __init__(self, diam=1, thick=1, dp=1/2):
        '''
        diam  - priemer
        thick - hrubka
        dp    - odsadenie vnutra kladky 
        '''
        
        self.diam = diam
        self.thick = thick
        
        Stemfie_X.__init__(self) 
        
        d1 = self.diam*self.BU       # vonkajsi priemer
        d2 = d1-dp*self.BU           # vnutorny priemer kladky
        h  = self.thick*self.BU      # hrubka kladky 
        
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
        
        hh = Hole(2, self.HRX)  # otvor pre hriadel
        self.D(hh)
        self.name = self.create_name()
        
    def create_name(self):
        dd = self.convert_param(self.diam)
        tt = self.convert_param(self.thick)
        return 'pulley_A_'+dd+'_'+tt


class Pulley_B(Stemfie_X):
    '''
    Kladka s vnutornym vybranim
    '''
    
    def __init__(self, diam=3, thick=1, dp=1/2, dh=1/4, rh=[0.8]):
        '''
        diam  - priemer
        thick - hrubka kladky
        dp    - odsadenie vnutorneho priemeru
        dh    - hrubka vnutra 
        rh    - pole polomerov otvorov
        '''
        if diam < 3: diam = 3
        self.diam = diam
        self.thick = thick
        
        Stemfie_X.__init__(self) 
        
        d1 = diam*self.BU       # vonkajsi priemer
        d2 = d1-dp*self.BU      # vnutorny priemer kladky
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
        
        # vnutorne vybranie
        cc = BU_Cylinder(1, 1).BU_Tz(1/2)                # uchytenie osi
        cd = BU_Cylinder(diam-dp-3/10, 1).BU_Tz(1/2+dh)
        self.D(cd)
        self.U(cc)
        hh = Hole(2, 2.1)#.BU_Tz(1/2)
        self.D(hh)
        
        # diery po obvode
        N = 8
        ph = np.pi*2/N
        hole_grid = []
        for r in rh:
            for i in range(N):
                dx = r*self.BU*np.cos(ph*i)
                dy = r*self.BU*np.sin(ph*i)
                hole_grid.append([dx,dy])

        hr = BU_Component()
        hr.obj = hr.obj.pushPoints(hole_grid) 
        hr.obj = hr.obj.circle(self.HR)
        hr.obj = hr.obj.extrude(20)
        hr.BU_Tz(-1/2)
        self.D(hr)
        
        self.name = self.create_name()
    
    def create_name(self):
        dd = self.convert_param(self.diam)
        tt = self.convert_param(self.thick)
        return 'pulley_B_'+dd+'_'+tt


class Pulley_C(Stemfie_X):
    '''
    Kladka s vnutornym vybranim a ramenami
    '''
    
    def __init__(self, diam=3, thick=1, dp=1/2, dh=1/4, rh=[1]):
        '''
        '''
        if diam < 3: diam = 3
        self.diam = diam
        self.thick = thick
        
        Stemfie_X.__init__(self) 
        
        d1 = diam*self.BU       # vonkajsi priemer
        d2 = d1-dp*self.BU      # vnutorny priemer kladky
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
        
        # vnutorne vybranie
        cc = BU_Cylinder(1, 1).BU_Tz(1/2)                # uchytenie osi
        cd = BU_Cylinder(diam-dp-1/2, 1).BU_Tz(1/2)
        self.D(cd)
        self.U(cc)
        
        # luce kladky
        for i in range(6):
            bx = Beam_Block([self.diam/2, 0.8, dh], holes = [False,False, False], center=False)
            bx.BU_Tx(-1/2).BU_Ty(-8/10/2).Rz(60*i)
            self.U(bx)
            
        # otvory v lucoch
        N = 6
        ph = np.pi*2/N
        hole_grid = []
        for r in rh:
            for i in range(N):
                dx = r*self.BU*np.cos(ph*i)
                dy = r*self.BU*np.sin(ph*i)
                hole_grid.append([dx,dy])
        self.obj = self.obj.edges("|Z").fillet(1)
        
        hr = BU_Component()        # pomocny komponent pre pole montaznych dier
        hr.obj = hr.obj.pushPoints(hole_grid) 
        hr.obj = hr.obj.circle(self.HR)
        hr.obj = hr.obj.extrude(20)
        hr.BU_Tz(-1/2)
        self.D(hr)
                
        hh = Hole(2, self.HRX)
        self.D(hh)
        
        self.name = self.create_name()
    
    def create_name(self):
        dd = self.convert_param(self.diam)
        tt = self.convert_param(self.thick)
        return 'pulley_C_'+dd+'_'+tt


#-----------------------------------------------------------------------

class Pulley_Holder_A(Stemfie_X):
    '''
    Base - 1 BU Block
    '''
    def __init__(self, height):
        Stemfie_X.__init__(self)

        h = height*self.BU
        p2 = Beam_Block([1, 1, 1/2], [False,False,False])
        
        p1 = BU_Component()
        p1.obj = (p1.obj
            .moveTo(  0,  0)
            .lineTo( self.BU,  0)
            .lineTo( self.BU,  h)
            .threePointArc( [5, 5+h], [0, h] ) # absolutne suradnice
            .close()
            .extrude(self.BU/2)
            )
        hr = []
        for i in range(height):
            hr.append([1/2,i+1])
        h1 = Hole_List(hr)
        p1.D(h1)
        p1.Rx().BU_Ty(1/2)
        self.U([p1,p2])
        h2 = Hole(3/4).BU_Txy([1/2, 1/2])        
        self.D(h2)


class Pulley_Holder_02(Stemfie_X):
    '''
    Base - 1 BU Block
    '''
    def __init__(self, height):
        Stemfie_X.__init__(self)
        
        h = height*self.BU
        p2 = Beam_Block([2, 1, 1/2], [False,False,False])
        
        p1 = BU_Component()
        p1.obj = (p1.obj
            .moveTo(  0,  0)
            .lineTo( self.BU*2,  0)
            .lineTo( self.BU*2,       self.BU*height)
            .lineTo( self.BU*(2-1/2), self.BU*(height+1/2) ) 
            .lineTo( self.BU*(  1/2), self.BU*(height+1/2) )
            .lineTo( self.BU*(    0), self.BU*(height)     )   
            .close()
            .extrude(self.BU/2)
            )
        h1 = Hole(2).BU_Txy(1, height )    # diera pre hriadel
        p1.D(h1)
        if height > 1:
            hr = []
            for i in range(height):
                hr.append([1/2, i])
                hr.append([1/2+1, i])
            h2 = Hole_List(hr)
            p1.D(h2)
        p1.Rx().BU_Ty(1/2)
        self.U([p1,p2])
        h2 = Hole_List( [ [1/2,1/2], [1/2+1, 1/2] ], 3/4)#.BU_Txy([1/2, 1/2])        
        self.D(h2)
        
        
