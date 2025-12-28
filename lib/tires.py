#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Pnematiky a disky
'''
from lib import *
class Tire_01(Stemfie_X):
    '''
    Pnematika so zadanymi parametrami.
    Pouzitie
    q = Tire_01()
    q.tire
    q.disc
    '''
    def __init__(self, t0=3.5, t1=2, s0=1, ch=1.5, N=20, h0=1/2):
        '''
        t0 - vonkajsi priemer pneumatiky
        t1 - vnutorny priemer pneumatiky
        ch - skosenie a rozsirenie pneumatiky, presah voci disku
        N  - pocet zarezov na dezene
        h0 - odsadenie disku  
        '''
        Stemfie_X.__init__(self)
        #---------------------------------------------------------------
        # pneumatika
        s1 = s0+2*ch/BU                     # korekcia sirky pnematiky o skosenie
        tr = BU_Cylinder(t0, s1)            # pneumatika
        p2 = BU_Cylinder(t1, s1)            # vnutorny otvor
        tr.D(p2)                            # rozdiel p1-22
        tr.obj= tr.obj.faces().chamfer(ch)  # hrany
        tr.Rx().BU_Ty(-s0/2)                # rotacia do roviny XY

        gamma = np.pi*2/N                   # dezen
        ds = cq.Workplane('ZX')
        for n in range(N):
            hx = np.cos(gamma*n)*t0/2*BU
            hy = np.sin(gamma*n)*t0/2*BU
            ds = ds.moveTo(hx,hy)
            ds = ds.cylinder(s0*BU+2*ch, ch)
        ds = ds.translate([0,-s0/2*BU,0]) 
        tr.obj = tr.obj.cut(ds)
        self.tire = tr
        
        #---------------------------------------------------------------
        # disk
        cc = ch/2/BU
        p = [ [0, s0+h0], [1/2,s0+h0], [1/2, s0], [t1/2, s0],
              [t1/2, 0], [t1/2+cc, -cc], [3/8+cc, -cc], 
              [3/8, 0], [3/8, 1/2], [1/8, 3/4], [0, 3/4] 
        ]
        br = BU_Bar(s0+h0).Rx().BU_Ty(-(1-h0)/2)
        self.disc = BU_PolyRot(p, 360).BU_Ty(-1)
        self.disc.D([br]) 

        
