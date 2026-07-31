#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:05:31 2024

@author: pf

History:
260719 - doplneny atribut pre priemer otvorov 
"""

from numpy import pi,sin,cos,abs

from lib.base import *
from lib.generic import *
from lib.holes import Hole_List

class Braces(Stemfie_X):
    def __init__(self):
        Stemfie_X.__init__(self)
    

class Brace(Braces):
    '''
    Zakladna spojka s definovanou dlzkou a hrubkou.
    '''
    
    def __init__(self, size, height=1/4, holes=True, center=False, hole_rad=HR_BASE):
        Braces.__init__(self)
        
        self.size = size
        self.height = height
        self.holes = holes
        self.name = self.create_name()
        
        if size > 1:
            bs = (
                cq.Sketch()
                .arc( (                0, 0), self.BU/2, 0.0, 360.0)
                .arc( ( (size-1)*self.BU, 0), self.BU/2, 0.0, 360.0)
                .hull()
            )
            self.obj = self.obj.placeSketch(bs)
            self.obj = self.obj.extrude(height*self.BU)
            
            if holes==True:
                h = np.zeros( [size, 2])
                for i in range(size):
                    h[i][0] = i
                
                hole_list = Hole_List(h, height, hole_rad)
                self = self.D(hole_list)
                
            if center==True:
                self.BU_Tx( -(size-1)/2 ).BU_Tz(-height/2)
                
        else:
            self.obj = BU_Cylinder(1, height).obj
            self.BU_Tz(height/2)
            
            if holes==True:
                self.D(Hole(height))
                
            if center==True:
                self.BU_Tz(-height/2)

    def create_name(self):
        s = 'brace_B_'
        s = s + self.convert_param(self.size) + '_'
        s = s + self.convert_param(self.height)
        return s    
            
            
                
class Brace_Arc(Braces):
    
    def __init__(self, r, angle, height=1/4, num_holes=4, center=False, hole_rad=HR_BASE):
        '''
        angle - 0...180 deg
        '''

        Braces.__init__(self)
        
        self.r = r
        self.angle = angle
        self.height = height
        self.num_holes = num_holes
        self.name = self.create_name()
        
        alpha = abs(angle/180*pi)   # deg -> rad 
        
        d = self.BU/2               # brace width
        r = r*self.BU               # radius
        height = height*self.BU
        
        if alpha >= pi:              # angle max  = pi
            alpha = pi
        
        # I.kvadrant
        beta = pi/2+alpha             # end angle
        
        # II kvadrant
        if (alpha > pi/2) and (alpha <= pi*3/4):
            beta = -alpha
        
        if alpha > pi*3/4:
            beta = -(alpha-pi/2)

        dx  = cos(alpha)
        dy  = sin(alpha)
        
        dx2 = cos(alpha/2)
        dy2 = sin(alpha/2)
        
        rdx = cos(beta)*d
        rdy = sin(beta)*d

        self.obj = ( 
                self.obj
               .moveTo(r-d, 0)
                
                # pociatocny obluk
               .threePointArc( (r, -d), (r+d, 0) )
                
                # vonkajsi obluk
               .threePointArc( (dx2*(r+d), dy2*(r+d) ), (dx*(r+d), dy*(r+d) ) )
                
                # koncovy obluk
               .threePointArc( (dx*r+rdx, dy*r+rdy), (dx*(r-d), dy*(r-d)) )
                
                # vnutorny obluk
               .threePointArc( (dx2*(r-d), dy2*(r-d) ), (r-d, 0 ) )
            
               .close()
               )
        
        # doplnenie vnutornych montaznych otvorov
        if num_holes > 1:
            self.HR = hole_rad
            gamma = alpha / (num_holes-1)
            for n in range(num_holes):
                hx = cos(gamma*n)*r
                hy = sin(gamma*n)*r
                self.obj = self.obj.moveTo(hx,hy)
                self.obj = self.obj.circle(self.HR)
        
        # vutvorenie komponentu
        self.obj = self.obj.extrude(height)
        
        if center==True:
            self.Tz(-height/2)
            
    def create_name(self):
        s = 'brace_A_'
        s = s + self.convert_param(self.r) + '_'
        s = s + self.convert_param(self.height) + '_'
        s = s + self.convert_param(self.num_holes) + '_'
        s = s + f'{int(self.angle):03d}'
        return s 
            

class Brace_Circle(Braces): 
    
    def __init__(self, r, height=1/4, num_holes=4, center=False, hole_rad=HR_BASE):
        Braces.__init__(self)
        
        self.r = r
        self.height = height
        self.num_holes = num_holes
        self.name = self.create_name()
        
        self.HR = hole_rad
        
        if r<1: r = 1
        if num_holes < 1: num_holes = 1
        
        d = self.BU/2
        r = r*self.BU
        height = height*self.BU
        
        self.obj = ( 
                self.obj
               .moveTo(0, 0)
               .circle(r-d)
               .circle(r+d)
                )
        
        # doplnenie vnutornych montaznych otvorov
        if num_holes > 1:
            self.HR = hole_diam
            gamma = pi*2/ (num_holes)
            for n in range(num_holes):
                hx = cos(gamma*n)*r
                hy = sin(gamma*n)*r
                self.obj = self.obj.moveTo(hx,hy)
                self.obj = self.obj.circle(self.HR)
               
        # vytvorenie komponentu
        self.obj = self.obj.extrude(height) 
        
        if center==True:
            self.BU_Tz(-height/2)
            
    def create_name(self):
        s = 'brace_C_'
        s = s + self.convert_param(self.r) + '_'
        s = s + self.convert_param(self.height) + '_'
        s = s + self.convert_param(self.num_holes)
        return s 


class Brace_Plate(Braces):
    
    def __init__(self, x=3, y=3, height=1/4, holes=True, center=False, hole_rad=HR_BASE):
        Braces.__init__(self)
        
        self.xx = x
        self.yy = y
        self.height = height
        self.name = self.create_name()
        
        xx = (x-1) * self.BU
        yy = (y-1) * self.BU
        if (x & y) > 1:
            bs = (
                cq.Sketch()
                .arc( (0, 0), self.BU/2, 0.0, 360.0)
                .arc( (xx, 0), self.BU/2, 0.0, 360.0)
                .arc( (0, yy), self.BU/2, 0.0, 360.0)
                .arc( (xx, yy), self.BU/2, 0.0, 360.0)
                .hull()
            )
            
            self.obj = cq.Workplane("XY")
            self.obj = self.obj.placeSketch(bs)
            self.obj = self.obj.extrude(height*self.BU)
           
            if holes==True:                
                hole_list = Hole_Grid(x,y, height,0,0,0, hole_rad)
                self = self.D(hole_list)
                
            if center==True:
                self.BU_Tx( -(x-1)/2 ).BU_Tz(-height/2)
                self.BU_Ty( -(y-1)/2 ).BU_Tz(-height/2)
                
        else:
            if x==1 or y==1:
                self.obj = Brace( max(x,y), height, holes, center).obj
            if y==1:
                self.Rz()
                
    def create_name(self):
        s = 'brace_P_'
        s = s + self.convert_param(self.xx) + '_'
        s = s + self.convert_param(self.yy) + '_'
        s = s + self.convert_param(self.height)
        return s             
                
