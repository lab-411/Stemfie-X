---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# <font color='navy'> <b> Spirograf </b> </font>

```{figure} ./img/banner.png
:width: 800px
```

```{figure} ./model/1020_spirograf/img/spirograf_demo.jpg
:width: 600px
```


S využitím knižnice pre návrh ozubených kolies možeme programom vytvoriť diely pre jednoduchý spirograf. Návrhom ozubených koles s rôznym počtom zubov môžeme dosiahnúť rôznu periódu pri ktorej sa budú krivky opakovať. 

## <font color='purple'> <b> Návrh </b></font>

### <font color='brown'> <b> Základňa spirografu </b></font>

```{code-cell} ipython3  
from lib import *
from lib.utils import *
rg = Ring_Gear(90, 1/2, 1/4+1/8)
bs = BU_Cube([10, 10, 1/4]).BU_Tz(1/4/2)  
cc = BU_Cylinder(9+1/4,1, hole=False, center=True) 

ar = array([ [-4,-4], [-4,-3], [-3,-4],
              [5, 5], [ 5, 4], [ 4, 5], 
              [5,-4], [ 5,-3], [ 4,-4],
              [-4,5], [-4, 4], [-3, 5]]) -[1/2,1/2]

hh = Hole_List(ar)

bs.D([cc, hh])
bs.U([rg])
convert_to_image(bs, './src/sp_base_90')

#bs.export_step('sp_base_90')
```

```{figure} ./src/sp_base_90.png
:width: 250px

Základňa spirografu
```

### <font color='brown'> <b> Ozubené kolesá </b></font>

```{code-cell} ipython3  
sg = Spur_Gear(50, bore=2.5)
c2 = BU_Cylinder(4+1/2, 1/2, hole=False, center=True).BU_Tz(1/2) 
sg.D(c2)

dp = 60/180*pi
arr = []
for i in range(6,22):
    x = (i*0.092)*cos(i*dp)
    y = (i*0.092)*sin(i*dp)
    arr.append( BU_Cylinder(.25, 1, hole=False, center=True).BU_Txy(x,y) )

for i in range(6):
    x = (1.55)*cos(i*dp + pi/6)
    y = (1.55)*sin(i*dp + pi/6)
    arr.append( BU_Cylinder(1, 1, hole=False, center=True).BU_Txy(x,y) )   

sg.D(arr)
convert_to_image(sg, './src/sp_gear_50')

#sg.export_step('sp_gear_50')
```

```{figure} ./src/sp_gear_50.png
:width: 150px

Ozubené koleso, 50 zubov
```


```{code-cell} ipython3  
sg = Spur_Gear(40, bore=2.5)
c2 = BU_Cylinder(3+2/4, 1/2, hole=False, center=True).BU_Tz(1/2) 
sg.D(c2)

dp = 60/180*pi
arr = []
for i in range(6,22):
    x = (i*0.07)*cos(i*dp)
    y = (i*0.07)*sin(i*dp)
    arr.append( BU_Cylinder(.25, 1, hole=False, center=True).BU_Txy(x,y) )

for i in range(6):
    x = (1.22)*cos(i*dp + pi/6)
    y = (1.22)*sin(i*dp + pi/6)
    arr.append( BU_Cylinder(0.8, 1, hole=False, center=True).BU_Txy(x,y) )   

sg.D(arr)
convert_to_image(sg, './src/sp_gear_40')

#sg.export_step('sp_gear_40')
```

```{figure} ./src/sp_gear_40.png
:width: 150px

Ozubené koleso, 40 zubov
```

```{code-cell} ipython3  
sg = Spur_Gear(65, bore=2.5)
c2 = BU_Cylinder(5+1/2+1/8, 1/2, hole=False, center=True).BU_Tz(1/2) 
sg.D(c2)

dp = 60/180*pi
arr = []
for i in range(6,22):
    x = (i*0.12)*cos(i*dp)
    y = (i*0.12)*sin(i*dp)
    arr.append( BU_Cylinder(.25, 1, hole=False, center=True).BU_Txy(x,y) )

for i in range(6):
    x = (1.9)*cos(i*dp + pi/6)
    y = (1.9)*sin(i*dp + pi/6)
    arr.append( BU_Cylinder(1.4, 1, hole=False, center=True).BU_Txy(x,y) )   

sg.D(arr)
convert_to_image(sg, './src/sp_gear_65')

#sg.export_step('sp_gear_65')
```

```{figure} ./src/sp_gear_65.png
:width: 180px

Ozubené koleso, 65 zubov
```

## <font color='purple'> <b> Diely </b></font>

```{list-table}
:header-rows: 1

* - Počet
  - Popis
  - Farba
  - Súbor (step)
* - 1
  - Základňa spirografu, 90 zubov
  - modrá
  - [sp_base_90](./model/1020_spirograf/parts/sp_base_90.step)
* - 1
  - Ozubené koleso, 40 zubov
  - modrá
  - [sp_gear_40](./model/1020_spirograf/parts/sp_gear_40.step)
* - 1
  - Ozubené koleso, 50 zubov
  - modrá
  - [sp_gear_50](./model/1020_spirograf/parts/sp_gear_50.step)
* - 1
  - Ozubené koleso, 65 zubov
  - modrá
  - [sp_gear_65](./model/1020_spirograf/parts/sp_gear_65.step)
```
