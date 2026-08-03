#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:58:15 2024

@author: pf
"""

from lib.base import *
from lib.generic import *
from lib.holes import Hole_Grid

class Beam_Block(Stemfie_X):
    '''
        b = Beam_Block([x,y,z])
        b = Beam_Block(x)        
    '''
    
    def __init__(self, dim=[1,1,1], holes = [True, True, True], center=False):
        Stemfie_X.__init__(self)
        
        if isinstance(dim, list):
            self.x, self.y, self.z = dim
        else:
            self.x = dim
            self.y = 1
            self.z = 1
        
        self.xx = self.x*self.BU
        self.yy = self.y*self.BU
        self.zz = self.z*self.BU
        
        self.name = self.create_name()
        
        self.obj = self.obj.box(self.xx,self.yy,self.zz)
        self.obj = self.obj.translate([self.xx/2, self.yy/2, self.zz/2])
        
        if holes[0] == True:        # x-holes
            hx = Hole_Grid(self.z, self.y, self.x, 1/2, 1/2).Ry(-90).BU_Tx(self.x)
            self.D(hx)
        
        if holes[1] == True:        # y-holes
            hy = Hole_Grid(self.x, self.z, self.y, 1/2, 1/2).Rx(90).BU_Ty(self.y)
            self.D(hy)
        
        if holes[2] == True:        # z-holes
            hz = Hole_Grid(self.x, self.y, self.z, 1/2, 1/2)
            self.D(hz)
            
        if center == True:
            self.BU_T([-self.x/2, -self.y/2, -self.z/2])
            
    def create_name(self):
        s = 'block_B_'
        s = s + self.convert_param(self.x) + '_'
        s = s + self.convert_param(self.y) + '_'
        s = s + self.convert_param(self.z)
        return s 

            
class Beam_U_Block(Stemfie_X):
    def __init__(self, x, y, hx=1/4, hy=1/4, dx=1, dy=1):        
        if hx < 1/4: hx = 1/4
        if hy < 1/4: hy = 1/4
        
        if hx > 1/2: hx = 1/2
        if hy > 1/2: hy = 1/2
        
        b1 = Beam_Block([x, y, hx], [False, False, True])
        b2 = Beam_Block([x, hy, dx], [False, True, False]) 
        b3 = Beam_Block([x, hy, dy], [False, True, False]).BU_Ty(y-hy)  
        b1.U([b2, b3])
        
        hx = Hole_Grid(x, 1, 1).BU_Txy(1/2,1/2) 
        b1.D(hx)
        b1.D(hx.BU_Txy(0,y-1) )
        
        hx = Hole_Grid(x, 1, 1).Rx().BU_T([1/2,1,1/2]) 
        b1.D(hx)
        b1.D(hx.BU_Ty(y-1))        
        
        self.obj = b1.obj
        
class Beam_L_Block(Stemfie_X):
    def __init__(self, x, y, hx=1/4, hy=1/4):        
        if hx < 1/4: hx = 1/4
        if hy < 1/4: hy = 1/4
        
        if hx > 1/2: hx = 1/2
        if hy > 1/2: hy = 1/2
        
        b1 = Beam_Block([x, y, hx], [False, False, False])
        b2 = Beam_Block([x, hy, 1], [False, False, False])  
        b1.U(b2)
        
        hx = Hole_Grid(x, y, 1).BU_Txy(1/2,1/2) 
        b1.D(hx)
        
        hz = Hole_Grid(x, 1, 1).BU_Txy(1/2,1/2) 
        b1.D(hz.Rx().BU_Txy(0,1) )
              
        self.obj = b1.obj



class Beam_H_Block(Stemfie_X):
    def __init__(self, x, y, hx=1/4, hy=1/4):        
        if hx < 1/4: hx = 1/4
        if hy < 1/4: hy = 1/4
        
        if hx > 1/2: hx = 1/2
        if hy > 1/2: hy = 1/2
        
        b1 = Beam_Block([x, y, hx], [False, False, True])
        b2 = Beam_Block([x, hy, 1], [False, True, False]) 
        b3 = Beam_Block([x, hy, 1], [False, True, False]).BU_Ty(y-hy)  
        
        b4 = Beam_Block([y, hy, 1], [False, True, False]).Rz().BU_Tx(hy) 
        b5 = Beam_Block([y, hy, 1], [False, True, False]).Rz().BU_Tx(hy).BU_Tx(x-hy)
        b1.U([b2, b3, b4, b5])
        
        hx = Hole_Grid(x, 1, 1).BU_Txy(1/2,1/2) 
        b1.D(hx)
        b1.D(hx.BU_Txy(0,y-1) )
        
        hx = Hole_Grid(x, 1, 1).Rx().BU_T([1/2,1,1/2]) 
        b1.D(hx)
        b1.D(hx.BU_Ty(y-1))    
        
        hy = Hole_Grid(1, y, 1).BU_T([1/2,1/2,0]) 
        b1.D(hy)
        b1.D(hy.BU_Tx(x-1))
        
        hy = Hole_Grid(1, y, 1).Ry().BU_T([0,1/2,1/2]) 
        b1.D(hy)
        b1.D(hy.BU_Tx(x-1))
        
        self.obj = b1.obj
