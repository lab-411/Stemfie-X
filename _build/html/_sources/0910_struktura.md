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
# <font color='navy'>  Štruktúra knižnice  </font>

Knižnica je tvorená hierarchiou tried odvodenej z knižnica *CadQuery*. Pre tvorbu špeciálnych komponentov je možné triedy knižnice rozšírovať dedením a pridávaním ďalších špecifických vlastností. Štruktúru knižnice *Stemfie-X* zobrazuje nasledujúci diagram

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
