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
# <font color='navy'> <b> Základné bloky </b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: stmx_112
```

```{figure} ./img/image_base.png
:width: 800px
:name: stmx_110

```

Základnými blokmi stavebnice sú jednoduché tvary ako hranoly, valce, tyče. Používajú ako základ pre konštrukciu zložených dielov alebo ako dištančné prvky. Pomocou logických operácií (zjednotenie, prienik, rozdiel) môžeme z nich vytvátať komplikovanejšie objekty. Neobsahujú montážne otvory, tie je možné doplniť pomocou triedy `Hole` z knižnice. 

## <font color='purple'> <b> Funkcie </b></font>

Knižnica základných komponentov s rozmermi zadávanými v **BU** jednotkách. Parameter **center** určuje, či komponent bude umiestnený v strede súradnicovej sústavy, čo je výhodné pri konštrukcii osovo symetrických dielov. 

    BU_Cube([x,y,z], center)                           # kocka / hranol
    BU_Cylinder(diameter, height, angle, hole, center) # valec
    BU_PolyLine([ [x1,y1], [x2,y2], ...], height)      # mnohouholník, extrudovaný
    BU_PolyRot([ [x1,y1], [x2,y2], ...], angle)        # mnohouholník, rotovaný
    BU_Cone(diam1, diam2, height, angle, center)       # kužel
    BU_Sphere(diameter, angle1, angle2, center)        # gula [ToDo]
    
    Parametre       Default   Popis 
    --------------------------------------------------------------
    x,y,z           1,1,1     rozmery 
    height          1/4       výška
    length          1         dĺžka 
    diameter        1         priemer
    hole            True      radiálny montážny otvor
    angle           360       uhol v stupňoch
    [xn,yn]                   súradnica bodu
    center          True      poloha v strede súradnicovej sústavy 
    
```{admonition} Základné bloky
:class: tip
Funkcie pre tvorbu základných blokov sú založené na zjednodušenom rozhraní k objektom z knižnice [CadQuery](https://cadquery.readthedocs.io). V prípade potreby konštrukcie komplikovanejších objektov na základe špeciálnych požiadaviek, napríklad skosené alebo zaoblené hrany, môžeme použiť priamo objekty a metódy knižnice *CadQuery*.   
```

### <font color='brown'> <b> Značenie dielov </b></font>

    base_t_p1_p2_p3_ ...                p1 ... pn  počet parametrov  
                                                   závisí od typu komponentu

    t  - typ komponentu                 pn - parameter, v BU jednotkách alebo uhle v stupnoch (ppp)
         B - cube                            01 =    1 BU            
         C - cylinder                           ...
         P - polyline                        10 =   10 BU
         R - polyrot                         12 =  1/2 BU 
         Q - sphere                          14 =  1/4 BU
         N - cone                            34 =  3/4 BU
         X - user defined                    ...
                                  
         
## <font color='purple'> <b> Príklady použitia </b></font>


    b1 = BU_Cube([1, 1.5, 2])     
    b2 = BU_Cylinder(1,2, hole=True, center=False)  
    b3 = BU_Cylinder(1.5,2, hole=False, center=False, angle=270) 
    b4 = BU_Cone(0.25, 1.5, 2 )
    

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

bc  = BU_Cube([1, 1.5, 2])                                     # base_B_03_02_01  3x2x1 BU cube
by1 = BU_Cylinder(1,2, hole=True, center=False)                # base_C_01_01
by2 = BU_Cylinder(1.5,2, hole=False, center=False, angle=270)  # base_C_01_02_270
br  = BU_Cone(0.25, 1.5, 2 ).Rx(180).BU_Tz(-4)
bc.U([by1.BU_Tx(2), by2.BU_Tx(4.5),  br.BU_Tx(6)]  )
convert_to_image(bc, './src/img_0535a')
```

```{figure} ./src/img_0535a.png
:width: 450px

Jednoduché bloky.
```

    q = [ [0,0], [1,0], [1,1], [2,1], [2,0], [3,0], [3,2], [0,2], [0,0]]
    b1 = BU_PolyLine(q, 1/2)
    b2 = BU_PolyRot(q, 90)


```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

q = [ [0,0], [1,0], [1,1], [2,1], [2,0], [3,0], [3,2], [0,2], [0,0]]
b1 = BU_PolyLine(q, 1/2)
b2 = BU_PolyRot(q, 90)
b1.U(b2.BU_Tx(4))
convert_to_image(b1, './src/img_0535b')
```

```{figure} ./src/img_0535b.png
:width: 350px

Extrudované a rotované bloky.
```
