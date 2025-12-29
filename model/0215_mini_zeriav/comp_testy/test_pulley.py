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


pp = Pulley_03(6, 0.9, rh=[1,2])
print(pp.name)
pp.export_step('pull_01_15')
