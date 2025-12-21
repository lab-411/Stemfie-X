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
# <font color='navy'> <b> Návrh komponentov</b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: prg_100
```
Pri návrhu vlastných konštrukcií často potrebujeme upraviť a modifikovať štandardné diely alebo vytvárať nové diely. Je zrejmé, že nie je možné vytvoriť univerzálny katalóg dielov, možnosti stavebnice *Stemfie-X* sú rozsiahle, a je preto vhodnejšie požadované diely a ich varianty vytvoriť "na mieru" pomocou programu. 

## <font color='purple'> <b> Štruktúra knižnice </b></font>

Knižnicu *Stemfie-X* tvorí sada tried implementovaná pomocou knižnice *CadQuery*. Diely stavebnice je možné vytvárať v jednom kroku volaním funkcií s parametrami dielov, nové diely je možné tvoriť z iných dielov pomocou jednoduchých logických operácií (prienik, rozdiel, zjednotenie). Pre generovanie štandardných ako aj odvodených dielov stavebnice postačujú triedy knižnice *Stemfie-X*, pokročílí uživatelia ale môžu využiť všetky možnosti knižnice [CadQuery](https://cadquery.readthedocs.io/en/latest/) a jazyka Python. 

Pre tvorbu špeciálnych komponentov je možné triedy knižnice rozšírovať dedením a pridávaním ďalších špecifických vlastností. Štruktúru knižnice *Stemfie-X* zobrazuje nasledujúci diagram

```{code-cell} ipython3  
:tags: ["remove-cell"]

s = r'''
@startuml
hide footbox
scale 2

class Assembly #Khaki
class Workplane #Khaki

Assembly  --o Construct
Construct -> "Stemfie-X"
Workplane --o "Stemfie-X"  


"Stemfie-X" <|-- "Beam_Block"
"Stemfie-X" <|--- "Braces"
"Stemfie-X" <|--- "Holes"
"Stemfie-X" <|---- "BU_Components"

"BU_Components" <|-- "BU_Cube"
"BU_Components" <|-- "BU_Cylinder"
"BU_Components" <|-- "BU_Polyline"
"BU_Components" <|-- "BU_Bar"

"Holes" <|-- "Hole"
"Holes" <|-- "Hole_List"
"Holes" <|-- "Hole_Grid"
"Holes" <|-- "Hole_Slot"

"Braces" <|-- "Brace"
"Braces" <|-- "Brace_Arc"
"Braces" <|-- "Brace_Circle"


class "Stemfie-X" {
BU 
HR
self.obj
BU_Tx() BU_Tx() BU_Tz()
BU_Txy() BU_T() T()
Rx() Ry() Rz() 
Mx() Mx() Mz()
MKx() MKy() MKz() 
D()
U()
I()
copy()
}

class "Construct" {
self.name
self.obj
}

class Holes{
self.length
}

@enduml
'''

fp = open('./jar/prg_101.pnl', 'w')
fp.write(s)
fp.close()

import os
_ = os.system("java -jar ./jar/plantuml.jar ./jar/prg_101.pnl") 

```

```{figure} ./jar/prg_101.png
:width: 800px
:name: stm_0102

Štruktúra tried knižnice Stemfie-X 
```

## <font color='purple'> <b> Použitie </b></font>

Pre generovanie podkladov pre 3D tlač štandardných komponentov je potrebné importovať knižnicu `lib` a vygenerovať želaný komponent vytvorením objektu danej triedy. Vytvorený komponent exportujeme do súboru typu *.step* alebo *.stl*. Vygenerovaný komponent je možné skontrolovať vo vhodnom 3D prehliadači napr. [f3d](https://f3d.app/).

```{code-cell} ipython3  
from lib import *
w2 = Wheel(2)
_ = w2.export_step('./step/wheel_02_14_12')
```

```{figure} ./img/wheel_02_14_12_1.png
:width: 350px
:name: stm_0103

Vygenerovaný diel stavebnice v prehliadači *f3d*. 
```

## <font color='purple'> <b> Transformácie objektov </b></font>

Metódy triedy *Stemfie_X* predstavujú v zjednodušenej podobe základné operácie na manipuláciu s objektmi v 3D priestore.
Pomocou týchto operácií môžete upravovať základné komponenty a vytvárať zložené alebo odvodené komponenty.

### <font color='brown'> <b> Posun </b></font>

Posuny objektu v smeroch osí súradnicovej sústavy

    BU_Tx(n)                      # posun objektu v smere x,y,z v jednotkách BU 
    BU_Ty(n)
    BU_Tz(n)
    BU_Txy([x,y])  BU_Txy(x,y)
    BU_Tyz([x,y])  BU_Tyz(y,z)
    BU_Tzx([z,x])  BU_Tzx(z,x)
    BU_T([x,y,z])  BU_T(x,y,z)
    
    Tx(d)                         # posun objektu v jednotkách [mm] 
    Ty(d)
    Tz(d)
    T([x,y,z])     T(x,y,z)
  
### <font color='brown'> <b> Rotácia </b></font>

Rotácie objektu okolo osí súradnicivej sústavy. Veľkosť uhla je v stupňoch.

    Rx(angle)
    Ry(angle)
    Rz(angle)

### <font color='brown'> <b> Zrkadlenie </b></font> 

Zrkadlenie objektu podľa osí súradnicivej sústavy.

    Mx()       # zrkadlenie objektu
    My()
    Mz()
    
    MKx()      # zrkadlenie s kopírovaním
    MKy()
    MKz()  

### <font color='brown'> <b> Logické operácie </b></font>

Pre vytváranie zložených objektov sú definované základné logické operácie. 

    U(c)   U([c1,c2 ...])     union
    D(c)   D([c1,c2 ...])     difference
    I(c)   I([c1,c2 ...])     intersection  

## <font color='purple'> <b> Vytvorenie zloženého objektu </b></font>

S využitím knižnice základných komponentov a transformačných metód môžeme vytvárať zložené objekty. Najskôr vytvoríme jednotlivé objekty, pomocou transformačných vzťahov ich posunieme do správnej pozícia a nakoniec ich logickou operáciou zjednotíme do finálneho objektu.

```{code-cell} ipython3  
from lib import *                         # U-Shape Beam Block
b1 = Beam_Block([3,1,1])                  # components, rotating and shifting
b2 = Beam_Block([3,1,1]).Ry()
b3 = Beam_Block([2,1,1]).Ry(-180).BU_Tx(1)

b1.U([b2,b3])                             # b1 = b1 + b2 + b3
b1.Rx(45).Ry(15)                          # rotate for view

show(b1, 400, 200)
```
