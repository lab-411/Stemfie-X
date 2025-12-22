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

## <font color='purple'> <b> Vytváranie objektov </b></font>

Pre generovanie podkladov pre 3D tlač štandardných komponentov je potrebné importovať knižnicu `lib` a vygenerovať želaný komponent vytvorením objektu danej triedy.

```{code-block} python
:caption: Vytváranie objektov

b1 = Brace(5)            # vytvorenie nov0ho objektu 
q1 = Beam([1/2, 3, 3])
w2 = Wheel(2)
```

## <font color='purple'> <b> Export objektov </b></font>

Export objektov do súborov typu *.step* alebo *.stl* pre generovanie podkladov pre 3D tlač je pomocou funkcií 

    object.export_step(file_name)
    object.export_stl(file_name)
    
      file_name - textový reťazec (string), bez prípony

Náhlad objektu vo formáte *.png* vygenerujeme pomocou funkcie 

    convert_to_image(object, file_name, ax, ay, az)
    
      object    - vygenerovaný stemfie komponent
      file_name - textový reťazec (string), bez prípony
      ax,ay,az  - poloha view-pointu pre náhlad na objekt
    
Nasledujúci fragment programu ukazuje použitie funkcií pre export objektov

```{code-block} python
:caption: Export objektov

b1.export_step('brace_B_05')
q1.export_stl('beam_B_12_03_03_111')

convert_to_image(w2, 'wheel')
```

## <font color='purple'> <b> Transformácie objektov </b></font>

Pri vytváraní nových komponentov stavebnice alebo tvorbe zostáv potrebujeme s objektami manipulovať v 3D priestore. Metódy triedy *Stemfie_X* pre manipuláciu s objektami sú zjednodušenou formou operácií z knižnice *CadQuery*. Všeobecný formát transformácií  má tvar

    object = object.operation( <param ...> )

Každá transformáciu vracia referenciu na transformovaný objekt, takže je možné transformácie reťaziť

    objec = object.operation_1(<param ...>).operation_2(<param>)  ... 


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

## <font color='purple'> <b> Použitie </b></font>

S využitím knižnice základných komponentov a transformačných metód môžeme vytvárať zložené objekty. Najskôr vytvoríme jednotlivé objekty, pomocou transformačných vzťahov ich posunieme do správnej pozícia a nakoniec ich logickou operáciou zjednotíme do finálneho objektu.

```{code-block} python
:caption: Použitie transformácií na vytvorenie zloženého objektu
                       
b1 = Brace(8, 1/4).BU_Tx(-(3+1/2))  # spojka v rovine XY a presun do stredu 
c1 = BU_Cylinder(1).BU_Tz(1/2+1/4)  # valec a presun nad spojku
c1=  c1.BU_Tx(3+1/2)                # presun valca na konec spojky
c2 = c1.MKy()                       # vytvorenie druheho valca zrkadlenim v osi Y s kopiou

b1.U([c1,c2])                       # zjednotenie objektov
```


```{figure} ./img/b1_f3d.png
:width: 400px

Vygenerovaný zložený objekt.
```
