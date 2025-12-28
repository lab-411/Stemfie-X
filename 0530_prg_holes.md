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
# <font color='navy'> <b> Montážne otvory </b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: holes_201
```

Pre vytváranie montážnych dier, štrbín a drážok je v *Stemfie-X* vytvorená trieda *Hole*. Táto generuje pomocné objekty, ktoré sú potom od vopred vytvorených dielov odčítané pomocou logickéj operácie *diffrence* `D()`. Štrbinu využívame aj pri konštrukciách, kde pri dieloch pod uhlom sa montážny otvor nenachádza v rastri **BU**. Princíp tvorby otvorov je zrejmý z nasledujúceho obrázku.

```{figure} ./img/hole_build.png
:width: 500px
:name: holes_202

Postup vytvárania otvorov v dieloch,
```


## <font color='purple'> <b> Funkcie </b></font>

    Hole(length)
    Hole_List(hole_list, length)
    Hole_Grid(dim_x, dim_y, length, offs_x, offs_y, offs_z)
    Hole_Slot(size, height, center)
    
    Parametre       Default   Popis 
    --------------------------------------------------------------
    length          1         dĺžka diery v BU
    hole_list                 zoznam pozícií dier v BU [[x1,y1], [x2,y2] ... ]
    dim_x, dim_y              rozmery pola dier v BU
    offs_x          1         posun pola dier v smere osi X v BU 
    offs_y          1         posun pola dier v smere osi Y v BU 
    offs_z          1         posun pola dier v smere osi Z v BU 
    size                      dĺžka štrbiny v BU
    height          1/4       výška štrbiny v BU
    center          False     umiestnenie štrbiny v strede sur. sustavy
            
### <font color='brown'> <b> Príklady použitia </b></font>

    bs = Brace(5, holes=False)          # brace without holes
    hh = Hole_Slot(3)                   # slot
    hs = Hole_List([ [3,0], [4,0]] )    # holes
    bs.D([hh, hs])                      # difference 

```{code-cell} ipython3  
:tags: ["remove-cell"]
from lib import *
                                    # Brace with slot and holes
bs = Brace(5, holes=False)          # brace without holes
hh = Hole_Slot(3)                   # slot
hs = Hole_List([ [3,0], [4,0]] )    # holes
bs.D([hh, hs])                      # difference 
convert_to_image(bs, './src/0520a')
```

```{figure} ./src/0520a.png
:width: 200px

Jednoducha spojka
```


```{code-cell} ipython3  
from lib import *
bs = Brace(6, holes=False)          # brace without holes
hh = Hole_Slot(4).BU_Tx(1)          # slot + shift
hs = Hole_List([ [0,0], [5,0]] )    # holes
bs.D([hh, hs])              # difference 
convert_to_image(bs, './src/0520b')
```

```{figure} ./src/0520b.png
:width: 250px

Jednoducha spojka
```

```{code-cell} ipython3  
from lib import *
c = BU_Cube([4,4,1/4], False)
h = Hole_Grid( 4,2 , 1, 1/2, 1/2)
c.D(h)
convert_to_image(c, './src/0520c')
```

```{figure} ./src/0520c.png
:width: 150px

Jednoducha spojka
```
