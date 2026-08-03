#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:10:45 2024

@author: pf

Hisotry:
260719 - doplneny parameter radius pre nastavenie velkosti otvoru
"""

from lib.base import *


class Common_Hole(Stemfie_X):
    def __init__(self, length=1, radius=HR_BASE):
        Stemfie_X.__init__(self)
        self.length = length*self.BU
        self.HR = radius


class Hole(Common_Hole):
    
    def __init__(self, length=1, radius=HR_BASE):
        Common_Hole.__init__(self, length)
        self.obj = self.obj.circle(self.HR)
        self.obj = self.obj.extrude(self.length)


class Hole_List(Common_Hole):
    # x,y - in BU units
    # hole_list = [ [x1,y1], [x2,y2] ... ]
    def __init__(self, hole_list, length=1, radius=HR_BASE):

        Common_Hole.__init__(self, length, radius)
        hole_list = np.array(hole_list)*self.BU
        
        self.obj = self.obj.pushPoints(hole_list) 
        self.obj = self.obj.circle(self.HR)
        self.obj = self.obj.extrude(self.length)

    
class Hole_Grid(Common_Hole):
    
    def __init__(self, dim_x, dim_y, length=1, offs_x=0, offs_y=0, offs_z=0, radius=HR_BASE):
        Common_Hole.__init__(self, length, radius)
        
        if dim_x < 1: dim_x = 1
        if dim_y < 1: dim_y = 1
        
        hole_grid = []
        for i in range(int(dim_x)):
            for j in range(int(dim_y)):
                hole_grid.append([i,j])
        
        hole_grid = np.array(hole_grid)*self.BU
        self.obj = self.obj.pushPoints(hole_grid) 
        self.obj = self.obj.circle(self.HR)
        self.obj = self.obj.extrude(self.length)
        self.BU_Tx(offs_x).BU_Ty(offs_y).BU_Tz(offs_z)


class Hole_Slot(Common_Hole):
    
        def __init__(self, size, height=1/4, center=False, radius=HR_BASE):
            Common_Hole.__init__(self, height, radius)
            if size < 1:
                size = 1
                
            bs = (
                cq.Sketch()
                .arc( (                0, 0), self.HR, 0.0, 360.0)
                .arc( ( (size-1)*self.BU, 0), self.HR, 0.0, 360.0)
                .hull()
            )
            self.obj = self.obj.placeSketch(bs)
            self.obj = self.obj.extrude(self.length)
