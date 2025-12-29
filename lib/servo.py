#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model for small servo 9g, servo holder and gears
"""

from lib.common import *
from lib.base import *
from lib.beams import *
from lib.holes import Hole_List, Hole
from lib.construct import *
from lib.gears import *


class Servo_9g(Stemfie_X):
    def __init__(self, fc=False):  
        '''
         Parameters
        ----------
        fc : True / False
             False  - create Cadquery step file
             True   - create assebled FreeCad step file
        ''' 
        Stemfie_X.__init__(self)     

        # servo body
        s1 = 12.5   # width
        d1 = 23.0   # length
        v1 = 22.8   # height
        bb = cq.Workplane("XY" , origin=(0,0,0))
        bb = bb.box(s1, d1, v1)
        bb = bb.edges().fillet(0.25)
        
        # holder, fastening
        s2 = 12.5 
        v2 = 2.75 
        d2 = 32.5 
        h2 = 3
        dr = cq.Workplane("XY" , origin=(0,0,0))
        dr = dr.box(s2, d2, v2)
        dr = dr.edges("|Z").fillet(0.5)
        dr = dr.translate([0, 0, -v2/2 + v1/2  - h2])
        
        # big cylinder
        h3 = 5.5
        r3 = 12.5 / 2
        cy = cq.Workplane("XY" , origin=(0,0,0))
        cy = cy.cylinder(height=h3, radius=r3 )
        cy = cy.edges(">Z").fillet(0.25)
        cy = cy.translate([0, d1/2-r3, h3/2 + v1/2  ])
        
        # axis
        h4 = 4.3
        r4 = 4.8 / 2
        cz = cq.Workplane("XY" , origin=(0,0,0))
        cz = cz.cylinder(height=h4, radius=r4 )
        cz = cz.translate([0, d1/2-r3, v1/2 + h4/2 + h3 ])
        
        # small cylinder
        h5 = 5.5
        r5 = 5 / 2
        cw = cq.Workplane("XY" , origin=(0,0,0))
        cw = cw.cylinder(height=h5, radius=r5 )
        cw = cw.edges(">Z").fillet(0.25)
        cw = cw.translate([0, 0, v1/2  + h3/2 ])
        
        # fixing holes
        h6 = 30
        r6 = 2.3 / 2
        c1 = cq.Workplane("XY" , origin=(0,0,0))
        c1 = c1.cylinder(height=h6, radius=r6 )
        c1 = c1.translate([0, d1/2 + 2.5, v1/2 - 5])
        
        c2 = cq.Workplane("XY" , origin=(0,0,0))
        c2 = c2.cylinder(height=h6, radius=r6 )
        c2 = c2.translate([0, -d1/2 - 2.5, v1/2 - 5])
        
        # cutting holes
        dr = dr.cut(c1)
        dr = dr.cut(c2)
     
        # shift to the coordinate system
        dy = -d1/2 + r3
        dz = -v1/2 - h5
        cz = cz.translate([0, dy, dz])
        cy = cy.translate([0, dy, dz])
        cw = cw.translate([0, dy, dz])
        dr = dr.translate([0, dy, dz])
        bb = bb.translate([0, dy, dz])
        
        
        if fc==False:
            #-----------------------------------------------------------
            # cadquery object
            #-----------------------------------------------------------
            bb = bb.union(dr)
            bb = bb.union(cy)
            bb = bb.union(cz)
            bb = bb.union(cw)
            self.obj = bb
            self.obj = self.obj.rotate([0,0,0], [0,1,0], 90)
        else:
            #-----------------------------------------------------------
            # assembly object -> FreeCAD STEP
            #-----------------------------------------------------------
            servo = cq.Assembly()  
            servo.add(cz, color=cq.Color("yellow"))
            servo.add(cy, color=cq.Color("steelblue"))
            servo.add(cw,color=cq.Color("steelblue"))
            servo.add(dr, color=cq.Color("lightblue"))
            servo.add(bb,color=cq.Color("lightblue"))
            self.obj = servo

       
class Servo_9g_Holder(Stemfie_X):
    def __init__(self):   
        Stemfie_X.__init__(self)          

        b = BU_Cube([1,3.5,2-1/4-1/8], center=False).BU_T([-2, - 3.5/2,0])
        h = Hole_List([ [0, -1], [0, 0], [0, 1] ], length = 1/2).BU_Tx(-1-1/2)
        w = BU_Cube([1+1/2, 2.38, 1.25], center=True).BU_Tz(1).BU_Tx(-1-1/2) 
        c1 = BU_Cylinder(0.15, 3, hole=False).Ry().BU_Tz(1).BU_Ty(2.8/2).BU_Tx(-2)
        c2 = BU_Cylinder(0.15, 3, hole=False).Ry().BU_Tz(1).BU_Ty(-2.8/2).BU_Tx(-2)
        b.D([c1, c2, w, h])
        self.obj = b.obj


class Servo_9g_Gear(Stemfie_X):
    def __init__(self, ds):   
        '''
        Ozubene koleso na servo s odsadenim
        ds - servo axis 
        '''
        Stemfie_X.__init__(self)  
        sg = Spur_Gear(20, bore=2)

        d1 = 0.5
        h1 = 0.25
        c1 = BU_Cylinder( d1, h1, hole=False).BU_Tz(h1/2)

        d2 = 0.24
        h2 = 0.2
        c2 = BU_Cylinder(d2, h2, hole=False).BU_Tz(h1 + h2/2)

        d3 = ds                             # servo axe
        h3 = 0.5
        c3 = BU_Cylinder(d3, h3, hole=False).BU_Tz(h1 + h2 + h3/2)

        d4 = 1
        h4 = 0.25
        c4 = BU_Cylinder(d4, h4, hole=False).BU_Tz(1/2+h4/2)

        c1.U([c2, c3])
        sg.U(c4)
        sg.D(c1)
        self.obj = sg.obj


class Servo_9g_Gear_Inv(Stemfie_X):
    def __init__(self, ds):   
        '''
        Alternativa - ozubene koleso na servo bez odsadenia k servu 
        ds - priemer osi serva 
        '''
        Stemfie_X.__init__(self)  
        sg = Spur_Gear(20, bore=2.2)

        d1 = 0.7            # spevnenie pre skrutku
        h1 = 0.22
        c1 = BU_Cylinder( d1, h1, hole=False).BU_Tz(1/2 + h1/2)

        d3 = ds             # odsadenie pre nasadenie na os serva
        h3 = 0.35
        c3 = BU_Cylinder(d3, h3, hole=False).BU_Tz(h3/2)

        d4 = 0.22           # diera pre skrutku      
        h4 = 2
        c4 = BU_Cylinder(d4, h4, hole=False)
        
        sg.U(c1)
        sg.D([c3,c4])
        self.obj = sg.obj
