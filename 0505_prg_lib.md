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
# <font color='navy'> Knižnica   </font>

```{figure} ./img/banner.png
:width: 800px
:name: prg_100
```

Pri návrhu vlastných konštrukcií často potrebujeme upraviť a modifikovať štandardné diely alebo vytvárať nové diely. Je zrejmé, že nie je možné vytvoriť univerzálny katalóg dielov, možnosti stavebnice *Stemfie-X* sú rozsiahle, a je preto vhodnejšie požadované diely a ich varianty vytvoriť "na mieru" pomocou programu v jazyku *Python* a knižnicu *Stemfie-X*. 

Knižnicu *Stemfie-X* tvorí sada tried implementovaná pomocou knižnice *CadQuery*. Diely stavebnice je možné vytvárať v jednom kroku volaním funkcií s parametrami dielov, nové diely je možné tvoriť z iných dielov pomocou jednoduchých logických operácií (prienik, rozdiel, zjednotenie). Pre generovanie štandardných ako aj odvodených dielov stavebnice postačujú triedy knižnice *Stemfie-X*, pokročílí uživatelia ale môžu využiť všetky možnosti knižnice [CadQuery](https://cadquery.readthedocs.io/en/latest/) a jazyka *Python*. 



## <font color='purple'> Vytváranie objektov </font>

Pre generovanie podkladov pre 3D tlač štandardných komponentov je potrebné importovať knižnicu `lib` a vygenerovať želaný komponent vytvorením objektu danej triedy.

```{code-block} python
:caption: Vytváranie objektov
from lib import *           # import kniznice
b1 = Brace(5)               # vytvorenie noveho komponentu - spojky o velkosti 5 BU
b1.export_step(b1.name)     # export spojky vo formate step pre 3D tlac
```

## <font color='purple'> Transformácie objektov </font>

Pri vytváraní nových komponentov stavebnice alebo tvorbe zostáv potrebujeme s objektami manipulovať v 3D priestore. Metódy triedy *Stemfie_X* pre manipuláciu s objektami sú zjednodušenou formou operácií z knižnice *CadQuery*. Všeobecný formát transformácií  má tvar

    object = object.operation( <param ...> )

Každá transformáciu vracia referenciu na transformovaný objekt, takže je možné transformácie reťaziť

    objec = object.operation_1(<param ...>).operation_2(<param>)  ... 


### <font color='brown'> Lineárny posun </font>

Posuny objektu v smeroch osí súradnicovej sústavy

    BU_Tx(n)                      # posun objektu v smere x,y,z v jednotkách BU 
    BU_Ty(n)
    BU_Tz(n)
    BU_Txy([x,y])  BU_Txy(x,y)    # posun v dvoch osiach v jednotkách BU
    BU_Tyz([x,y])  BU_Tyz(y,z)
    BU_Tzx([z,x])  BU_Tzx(z,x)
    
    BU_T([x,y,z])  BU_T(x,y,z)    # všeobecný posun v jednokách BU    
    
    Tx(d)                         # posun objektu v jednotkách [mm] 
    Ty(d)
    Tz(d)
    
    T([x,y,z])     T(x,y,z)      # všeobecný posun v [mm]
    
  
### <font color='brown'> Rotácia </font>

Rotácie objektu okolo osí súradnicivej sústavy. Veľkosť uhla je v stupňoch.

    Rx(angle)
    Ry(angle)
    Rz(angle)

### <font color='brown'>  Zrkadlenie </font> 

Zrkadlenie objektu podľa osí súradnicivej sústavy.

    Mx()       # zrkadlenie objektu
    My()
    Mz()
    
    MKx()      # zrkadlenie s kopírovaním
    MKy()
    MKz()  

### <font color='brown'>  Logické operácie </font>

Pre vytváranie zložených objektov sú definované základné logické operácie - zjednotenie, rozdiel a prienik. 

    U(c)   U([c1,c2 ...])     union
    D(c)   D([c1,c2 ...])     difference
    I(c)   I([c1,c2 ...])     intersection  

### <font color='brown'>  Príklad </font>

S využitím knižnice základných komponentov a transformačných metód môžeme vytvárať zložené objekty. Najskôr vytvoríme jednotlivé objekty, pomocou transformačných vzťahov ich posunieme do správnej pozícia a nakoniec ich logickou operáciou zjednotíme do finálneho zloženého objektu.

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

## <font color='purple'> Export objektov </font>

Export objektov do súborov typu *.step* alebo *.stl* pre generovanie podkladov pre 3D tlač je pomocou funkcií 

    object.export_step(file_name)
    object.export_stl(file_name)
    
      file_name - textový reťazec (string), bez prípony

Náhlad objektu vo formáte *.png* vygenerujeme pomocou funkcie 

    convert_to_image(object, file_name, ax, ay, az)
    
      object    - vygenerovaný stemfie komponent
      file_name - textový reťazec (string), bez prípony
      ax,ay,az  - poloha view-pointu pre náhlad na objekt
    
Nasledujúci programu ukazuje použitie funkcií pre export objektov

```{code-block} python
:caption: Export objektov

b1.export_step('brace_B_05')
q1.export_stl('beam_B_12_03_03_111')

convert_to_image(w2, 'wheel')
```
